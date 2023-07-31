from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileModel
from .serializers import FileSerializer, TextSerializer
from core.gen_questions import getQuestFromFile, getQuestFromText
import os
import json
from drf_spectacular.utils import extend_schema


# Create your views here.

json_path = "jsonsave/tmp.json"

@extend_schema(
        request=FileSerializer,
        responses={204: None},
        methods=["POST"]
    )

@api_view(['POST'])
def questionGenFromFile(request):
    file = request.FILES["file"]
    form = FileModel.objects.create(file=file)
    file_path = form.file.path
    file_path = file_path.replace("\\", "/")
    # return Response({"path": file_path})
    response_data = getQuestFromFile(file_path)
    with open(json_path, 'w') as json_file: 
        json.dump(response_data, json_file)
    return Response({"success"})

@extend_schema(
        request=TextSerializer,
        responses={204: None},
        methods=["POST"]
    )
@api_view(['POST'])
def questionGenFromText(request):
    response_data = getQuestFromText(request.data["text"])
    with open(json_path, 'w') as json_file: 
        json.dump(response_data, json_file)
    return Response({"success"})

@api_view(['GET'])
def get_both(request):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    qa_list = [{"question": item["question_statement"], "answer": item["answer"]} for item in data["questions"]]

    return Response(qa_list)