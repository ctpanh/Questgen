from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuestionModel
from .serializers import FileSerializer, TextSerializer
from drf_spectacular.utils import extend_schema
from core.handle_input import *


# Create your views here.


@extend_schema(
        request=FileSerializer,
        responses={204: None},
        methods=["POST"]
    )

@api_view(['POST'])
def questionGenFromFile(request):
    language = request.data["language"]
    file = request.FILES.get("file")
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    type_input = request.data["quest_type"]

    if not file:
        return Response({"error": "No file uploaded."}, status=400)
    # Create a model instance to store the file
    form = QuestionModel.objects.create(file=file, easy=easy_num, medium=med_num, hard=hard_num, quest_type=type_input, language=language)
    # Get the context from the uploaded file
    file_path = form.file.path.replace("\\", "/")
    load_file(file_path)

    questions = genquests(language, type_input, easy_num, med_num, hard_num)

    if type_input == 'tf':
        return Response(extract_tfq(questions))
    return Response(extract_mcq(questions))

@extend_schema(
        request=TextSerializer,
        responses={204: None},
        methods=["POST"]
    )
@api_view(['POST'])
def questionGenFromText(request):
    language = request.data["language"]
    context = request.data["text"]
    easy_num = int(request.data["easy"])
    med_num = int(request.data["medium"])
    hard_num = int(request.data["hard"])
    type_input = request.data["quest_type"]

    QuestionModel.objects.create(text=context, easy=easy_num, medium=med_num, hard=hard_num, quest_type=type_input, language=language)

    load_context(context=context)

    questions = genquests(language, type_input, easy_num, med_num, hard_num)

    if type_input == 'tf':
        return Response(extract_tfq(questions))
    return Response(extract_mcq(questions))