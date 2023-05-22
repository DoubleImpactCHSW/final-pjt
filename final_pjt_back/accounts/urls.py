from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('test/', views.test),
    # 프로필 상세 정보
    path('profile/<str:user_name>/', views.profile),
    # 프로필 상세 정보 수정
    path('profile/update/<str:user_name>/', views.update)
]
