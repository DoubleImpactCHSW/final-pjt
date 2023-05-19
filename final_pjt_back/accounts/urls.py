from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('test/', views.test),
    # 프로필 상세 정보
    path('profile/<int:user_id>/', views.profile),
    # 프로필 상세 정보 수정
    path('profile/update/<int:user_id>/', views.update)
]
