from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

def home(request):
    return render(request,'index.html',{})

class ApiHome(APIView):
    def get(self,request):
        return Response("Hello DRF")
