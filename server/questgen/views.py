from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileModel
from core.gen_questions import getQuest
import os
import json


# Create your views here.

json_path = "jsonsave/tmp.json"

@api_view(['POST'])
def questionGenFromFile(request):
    file = request.FILES["file"]
    form = FileModel.objects.create(file=file)
    file_path = form.file.path
    file_path = file_path.replace("\\", "/")
    # return Response({"path": file_path})
    response_data = getQuest(file_path)
    with open(json_path, 'w') as json_file: 
        json.dump(response_data, json_file)
    return Response({"success"})

@api_view(['GET'])
def get_all_questions(request):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    questions = [item["question"] for item in data]
    return Response({"questions": questions})

@api_view(['GET'])
def get_all_answers(request):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    answers = [item["answer"] for item in data]
    return Response({"answers": answers})

@api_view(['GET'])
def get_both(request):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    qa_list = [{"question": item["question_statement"], "answer": item["answer"]} for item in data["questions"]]

    return Response(qa_list)