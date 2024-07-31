from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from courses.services import get_email_list
from users.models import User, Subscriptions
import pytz


@shared_task
def send_information_about_course_update(pk):
    """Отправляет сообщение пользователю об обновлении курса"""
    print("Проверка запуска")
    # subscriptions = Subscriptions.objects.filter(course=pk)

    message, email_list = get_email_list(pk)

    print(f"<<<<<<<<<<<<<<<< {message}, {email_list} >>>>>>>>>>>>>>>")

    # zone = pytz.timezone(settings.TIME_ZONE)
    # current_datetime_4_hours_ago = datetime.now(zone) - timedelta(hours=4)
    # print(f"course= {course},{course.name}")
    # print(f"course.updated_at= {course.updated_at}, > 4h > {current_datetime_4_hours_ago}")
    # print(f"course= {course},{course.name}")
    #
    # email_list = []
    # message = f"Ваш курс {course.name} был обновлен!"
    # for s in subscriptions:
    #     email_list.append(s.user.email)
    #
    #     print(f"email added = {s.user.email}")

    if email_list:
        print(email_list)
        send_mail(
            f"Обновление курса.",
            message,
            EMAIL_HOST_USER,
            email_list
        )
    else:
        print("no emails sended today")
