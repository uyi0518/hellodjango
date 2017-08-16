from random import Random
from user.models import  EmailVerifyRecord
from django.core.mail import send_mail
from hellodjango.settings import EMAIL_FROM

from django.core.mail import EmailMessage
from django.template import loader

def random_str(randomlength=8):
    str=''
    chars='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
    length=len(chars)-1
    random=Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str
def send_reg_email(email,send_type='register'):
    email_record=EmailVerifyRecord()
    code=random_str(16)
    email_record.email=email
    email_record.code=code
    email_record.send_type=send_type
    email_record.save()


    if send_type=='register':
        email_title="二大爷注册"
        email_body="请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        # send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        # if send_status:
        #     pass
        html_content=loader.render_to_string("login/email.html", {})
        msg = EmailMessage(email_title,html_content,EMAIL_FROM,[email])
        msg.content_subtype = "html"
        msg.send()