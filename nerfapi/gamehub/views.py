from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class StatusView(APIView):
    def get(self, request):
        content = {'status': 'ok'}
        return Response(content)
