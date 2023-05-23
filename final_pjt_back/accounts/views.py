from django.shortcuts import render
from .models import User,Profile
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
def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, user_name):
    user = get_object_or_404(User, username=user_name)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    # 프로필 정보 업데이트
    try:
        profile = user.profile
        profile.age = request.data.get('age', profile.age)
        profile.money = request.data.get('money', profile.money)
        profile.salary = request.data.get('salary', profile.salary)
        profile.save()
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user, age=request.data.get('age'), money=request.data.get('money'), salary=request.data.get('salary'))

    # User 모델의 나머지 정보 업데이트
    user.nickname = request.data.get('nickname', user.nickname)
    user.save()

    return Response(serializer.data)