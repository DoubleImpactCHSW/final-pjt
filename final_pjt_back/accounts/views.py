from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.


@api_view(['GET'])
def test(request):
    return JsonResponse({ 'message': 'okay' })

@api_view(['GET'])
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)