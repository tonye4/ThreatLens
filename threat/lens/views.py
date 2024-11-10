from django.shortcuts import render
from django.http import HttpResponse
# rest 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import LanguageSerializer
from .models import Language

from django.http import JsonResponse

# Create your views here.


def home(request):
    return render(request, 'lens/dashboard.html')


@api_view(['GET'])
def get_languages(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)


def ping(request):
    return JsonResponse({"status": "ok"})

