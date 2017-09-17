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
    def get_queryset(self):
        return super().get_queryset().all()

    def create(self, sendName, add, iphone, uid, uNow):
        userAdr = UserAddressInfo()
        userAdr.uName = sendName
        userAdr.uAddress = add
        userAdr.uPhone = iphone
        userAdr.user_id = uid
        userAdr.uNow = uNow
        return userAdr

    def update(self, aid, uNow):
        upadd =UserAddressInfo.address.get(uNow =True)
        upadd.uNow =False
        upadd.save()
        uadd = UserAddressInfo.address.get(id =aid)
        uadd.uNow = uNow
        uadd.save()


class UserInfo(models.Model):
    userName = models.CharField(max_length=20)
    userPsw = models.CharField(max_length=40)
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
    uNow = models.BooleanField(default=False)
    user = models.ForeignKey('UserInfo')

    address = AddressInfoManager()
