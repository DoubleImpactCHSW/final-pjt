from django.db import models

# Create your models here.
class DepositProducts(models.Model):

    dcls_month = models.IntegerField(default='')
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField() # 금융 회사 명
    fin_prdt_nm = models.TextField() # 금융 상품 명
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.TextField()

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    # 저축금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저출금리
    intr_rate = models.FloatField()
    # 최고 우대 금리
    intr_rate2 = models.FloatField()
    # 저축기간
    save_trm = models.IntegerField()


class SavingProducts(models.Model):
    dcls_month = models.IntegerField()  # 공시 제출월
    fin_prdt_cd = models.TextField(unique=True) # 금융상품 코드
    kor_co_nm = models.TextField()  # 금융 회사 명
    fin_prdt_nm = models.TextField()    # 금융상품명
    etc_note = models.TextField()   # 기타 유의사항
    # 가입 제한(1:제한 없음, 2:서민전용, 3:일부제한)
    join_deny = models.IntegerField()   
    join_member = models.TextField()  # 가입 대상
    join_way = models.TextField()   # 가입 방법
    spcl_cnd = models.TextField()   # 우대 조건
    join_deny = models.TextField()  # 가입 제한

class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    # 저축금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 금리
    intr_rate = models.FloatField(default=0)
    # 최고 우대 금리
    intr_rate2 = models.FloatField()
    # 저축기간
    save_trm = models.IntegerField()