from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def test(request):
    return JsonResponse({ 'message': 'okay' })

@api_view(['GET'])
def get_user_id(request):
    return JsonResponse({'user_id' : request.user.id})