from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np
from accounts.models import User
from products.models import DepositProducts
from django.contrib.auth.decorators import login_required
from scipy.stats import pearsonr
from collections import Counter
from django.http import HttpResponse

# Create your views here.
def get_similar_users(user_data, current_user_data, top_n):
    correlations = []
    for i, data in enumerate(user_data):
        # 현재 사용자와 다른 사용자들 간의 피어슨 상관계수 계산
        correlation = pearsonr(current_user_data, data)[0]
        correlations.append((i, correlation))

    # 피어슨 상관계수가 가장 높은 사용자들의 인덱스를 가져옴 (자기 자신 제외)
    similar_users_indices = [index for index, _ in sorted(correlations, key=lambda x: x[1], reverse=True)][1:top_n+1]
    
    return similar_users_indices

@login_required
def recommend(request):
    current_user = request.user
    profile = current_user.profile
    age = profile.age or 0
    money = profile.money or 0
    salary = profile.salary or 0
    current_user_data = np.array([age, money, salary])
    print(current_user_data)
    # 모든 사용자의 나이, 금액, 연봉 정보 가져오기
    users = User.objects.select_related('profile').all()
    # print(users)
    user_data = np.array([[user.age or 0, user.money or 0, user.salary or 0] for user in users])
    # print(user_data)
    # 현재 사용자의 인덱스 찾기
    current_user_index = current_user.id
    # print(current_user_index)

    # 비슷한 사용자들 가져오기
    similar_user_indices = get_similar_users(user_data, current_user_data, top_n=1000)
    # print(similar_user_indices)
    # print(similar_users)

    # 유사한 사용자들의 상품 가져오기
    fin_prd = []
    for user_index in similar_user_indices:
        user = users[user_index]
        if user.financial_products:
            products = user.financial_products.split(',')
            fin_prd.extend(products)
    # print(fin_prd)

    # 가장 많이 등장한 상위 10개의 상품을 찾음
    top_fin_prdt = Counter(fin_prd).most_common(10)
    # print(top_fin_prdt)
    
    # 결과 출력
    print("가장 많이 가입된 상품:")
    recommend_prd = []
    for fin_prdt_cd, count in top_fin_prdt:
        recommend_prd.append(fin_prdt_cd)
        print(f"상품 코드: {fin_prdt_cd}, 가입 수: {count}")
    
    return JsonResponse({"recommend_prd": recommend_prd})


def balance(request):
    
    return JsonResponse({'message' : 'okay'})