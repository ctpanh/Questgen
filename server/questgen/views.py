from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuestionModel
from .serializers import FileSerializer, TextSerializer
from core.generate_questions import get_questions
from drf_spectacular.utils import extend_schema
from core.handle_input import *


# Create your views here.

json_path = "output_questions.json"

@extend_schema(
        request=FileSerializer,
        responses={204: None},
        methods=["POST"]
    )

@api_view(['POST'])
def questionGenFromFile(request):
    # file = request.FILES.get("file")
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    type_input = request.data["type"]
    questions = genquests(type_input, easy_num, med_num, hard_num)

    if type_input == 'tf':
        print(questions)
        print(extract_tfq(questions))
        return Response(extract_tfq(questions))
    return Response(extract_mcq(questions))

@api_view(['POST'])
def questionGenFromFile2(request):
    questions = genquests(question=request.data["question"])
    return Response(questions)


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

@api_view(['POST'])
def test(request):
    file = request.FILES.get("file")
    form = QuestionModel.objects.create(file=file)
    if not file:
        return Response({"error": "No file uploaded."}, status=400)
    # Get the context from the uploaded file
    file_path = form.file.path.replace("\\", "/")
    load_file(file_path)
    return Response({"Success"})