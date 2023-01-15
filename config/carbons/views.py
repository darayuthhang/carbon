from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from constants import ApiKey

from django.http import HttpResponse
# Create your views here.
@api_view(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
