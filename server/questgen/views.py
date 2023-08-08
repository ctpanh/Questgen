from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileModel
from .serializers import FileSerializer, TextSerializer
from core.generate_questions import generate_questions, get_questions, load_txt
import json
from drf_spectacular.utils import extend_schema


# Create your views here.

json_path = "output_questions.json"

@extend_schema(
        request=FileSerializer,
        responses={204: None},
        methods=["POST"]
    )

@api_view(['POST'])
def questionGenFromFile(request):
    # Get the uploaded file from the request
    file = request.FILES.get("file")
    
    if not file:
        return Response({"error": "No file uploaded."}, status=400)
    
    # Create a model instance to store the file (assuming you have a model named 'FileModel')
    form = FileModel.objects.create(file=file)
    file_path = form.file.path.replace("\\", "/")
    
    # Get the context from the uploaded file
    context = load_txt(file_path)
    
    # Generate the questions using the 'get_questions' function
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    # easy_num = 2
    # med_num = 2
    # hard_num = 2
    easy_questions, medium_questions, hard_questions = get_questions(context, "boolean", easy_num, med_num, hard_num)
    
    response_data = {
        "easy": easy_questions,
        "medium": medium_questions,
        "hard": hard_questions
    }
    
    json_path = "output_questions.json"
    with open(json_path, 'w') as json_file:
        json.dump(response_data, json_file)
    
    return Response({"success": "Questions generated and saved as JSON."})

@extend_schema(
        request=TextSerializer,
        responses={204: None},
        methods=["POST"]
    )
@api_view(['POST'])
def questionGenFromText(request):
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    context = request.data["text"]

    easy_questions, medium_questions, hard_questions = get_questions(context, "boolean", easy_num, med_num, hard_num)
    
    response_data = {
        "easy": easy_questions,
        "medium": medium_questions,
        "hard": hard_questions
    }
    
    json_path = "output_questions.json"
    with open(json_path, 'w') as json_file:
        json.dump(response_data, json_file)
    
    return Response({"success": "Questions generated and saved as JSON."})

@api_view(['GET'])
def get_both(request):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    return Response(data)