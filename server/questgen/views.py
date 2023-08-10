from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuestionModel
from .serializers import FileSerializer, TextSerializer
from core.generate_questions import get_questions, load_txt
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
    file = request.FILES.get("file")
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    type_input = request.data["type"]
    
    if not file:
        return Response({"error": "No file uploaded."}, status=400)
    
    # Create a model instance to store the file (assuming you have a model named 'FileModel')
    form = QuestionModel.objects.create(file=file, easy=easy_num, medium=med_num, hard=hard_num, quest_type=type_input)
    # Get the context from the uploaded file
    file_path = form.file.path.replace("\\", "/")
    context = load_txt(file_path)
    
    # Generate the questions using the 'get_questions' function
    easy_questions, medium_questions, hard_questions = get_questions(context, type_input, easy_num, med_num, hard_num)
    
    response_data = {
        "easy": easy_questions,
        "medium": medium_questions,
        "hard": hard_questions
    }
    
    return Response(response_data)

@extend_schema(
        request=TextSerializer,
        responses={204: None},
        methods=["POST"]
    )
@api_view(['POST'])
def questionGenFromText(request):
    context = request.data["text"]
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    type_input = request.data["type"]

    easy_questions, medium_questions, hard_questions = get_questions(context, type_input, easy_num, med_num, hard_num)
    
    response_data = {
        "easy": easy_questions,
        "medium": medium_questions,
        "hard": hard_questions
    }
    
    return Response(response_data)