from celery import task
from django.core.mail import send_mail
from django.conf import settings


@task
def send(uid, uemail):
    # 注册时发送激活邮件
    msg = '<br/><a href="http://127.0.0.1:8000/User/active%s/">点击激活</a>' % uid
    send_mail('天天生鲜用户注册激活', '', settings.EMAIL_FROM, [uemail], html_message=msg)

@task
def send_reset(uid, uemail):
    # 密码重置邮件
    msg = '<br/><a href="http://127.0.0.1:8000/User/reset_show%s/">点击重置密码</a>' % uid
    send_mail('天天生鲜用户重置密码', '', settings.EMAIL_FROM, [uemail], html_message=msg)