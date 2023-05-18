from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import DepositProducts, SavingProducts
from .serializers import DepositProductsSerializer,DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer
import requests
from django.db.models import Max
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
# Create your views here.

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
API_KEY=settings.API_KEY
@api_view(['GET'])
def api_test(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        # 금융회사 코드 : 은행
        'topFinGrpNo': '020000',
        'pageNo': 1
        
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response': response})



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(URL, params=params).json()

    # products = response['result']['baseList']
    # serializer = DepositProductsSerializer(data=products, many=True)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    
    options = response['result']['optionList']
    for item in options:
        for key in item.keys():
            if item.get(key) is None:
                item[key] = -1
        deposit = DepositProducts.objects.get(fin_prdt_cd=item['fin_prdt_cd'])
        serializer = DepositOptionsSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=deposit)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_products(request):
    products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(URL, params=params).json()

    # products = response['result']['baseList']
    # serializer = SavingProductsSerializer(data=products, many=True)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    
    options = response['result']['optionList']
    for item in options:
        for key in item.keys():
            if item.get(key) is None:
                item[key] = -1
        saving = SavingProducts.objects.get(fin_prdt_cd=item['fin_prdt_cd'])
        serializer = SavingOptionsSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=saving)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_products(request):
    products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_product_detail(request,fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_product_detail(request,fin_prdt_cd):
    product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer(product)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registered_product(request,user_id,fin_prdt_cd):
    user = User.objects.get(id=user_id)
    # 유저의 financial_products에 상품 정보 추가
    if user.financial_products:
        user.financial_products += f",{fin_prdt_cd}"
    else:
        user.financial_products = fin_prdt_cd
    user.save()
    return HttpResponse("상품 가입이 완료되었습니다.")