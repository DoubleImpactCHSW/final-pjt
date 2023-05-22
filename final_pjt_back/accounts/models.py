from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import DepositProducts, SavingProducts

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    financial_products = models.CharField(max_length=50,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    
# 상속 받아서 구현해보기
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    # 기본 코드는 다 그대로 쓰고, save_user 만 오버라이딩 하겠다!
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # nickname 필드
        nickname = data.get("nickname")


        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)

        # 닉네임 필드 추가
        if nickname:
            user_field(user, "nickname", nickname)

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True)
    money = models.IntegerField(blank=True)
    salary = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'