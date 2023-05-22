from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    dcls_month = models.IntegerField(default='')
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
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
    dcls_month = models.IntegerField()
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.TextField()

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