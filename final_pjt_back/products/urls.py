from django.urls import path
from . import views

app_name="products"
urlpatterns = [
    # 정기예금 상품 목록 DB 에 저장
    path('save-deposit-products/', views.save_deposit_products),
    # 정기예금 상품 옵션 DB 에 저장
    path('save-deposit-options/', views.save_deposit_options),
    # 전체 정기예금 상품 목록 출력
    path('deposit-products/', views.deposit_products),
    # 정기적금 상품 목록 DB 에 저장
    path('save-saving-products/', views.save_saving_products),
    # 정기적금 상품 옵션 DB 에 저장
    path('save-saving-options/', views.save_saving_options),
    # 전체 정기적금 상품 목록 출력
    path('saving-products/', views.saving_products),
    # 정기예금 상세
    path('deposit-product-detail/<str:fin_prdt_cd>/', views.deposit_product_detail),
    # 정기적금 상세
    path('saving-product-detail/<str:fin_prdt_cd>/', views.saving_product_detail),
    # 가입 상품 목록에 추가
    path('add/<int:user_id>/<str:fin_prdt_cd>/', views.registered_product),
    # 금리 바꾸기
    path('update-interest-rate/<int:option_id>/', views.update_interest_rate),
]