from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileModel
from core.test import getQuest


# Create your views here.

@api_view(['POST'])
def questionGenFromFile(request):
    file = request.FILES["file"]
    form = FileModel.objects.create(file=file)
    file_path = form.file.path
    file_path = file_path.replace("\\", "/")
    # return Response({"path": file_path})
    return Response(getQuest(file_path))