from django.db import models


class UserInfoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def create(self, name, psw, email):
        user = UserInfo()
        user.userName = name
        user.userPsw = psw
        user.userEmail = email
        return user


class AddressInfoManager(models.Manager):
    def create(self, adrName, adrPsw, adrEmail):
        adress = UserAddressInfo()
        adress.userName = adrName
        adress.userPsw = adrPsw
        adress.userEmail = adrEmail
        return adress


class UserInfo(models.Model):
    userName = models.CharField(max_length=20)
    userPsw = models.CharField(max_length=40
                               )
    userEmail = models.CharField(max_length=30)
    isValid = models.BooleanField(default=True)
    isActive = models.BooleanField(default=False)

    users = UserInfoManager()
    # 类对象的打印信息
    def __str__(self):
        return self.userName


class UserAddressInfo(models.Model):
    uName = models.CharField(max_length=20)
    uAddress = models.CharField(max_length=100)
    uPhone = models.CharField(max_length=11)
    user = models.ForeignKey('UserInfo')

    address = AddressInfoManager()
