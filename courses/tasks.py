from datetime import datetime, timedelta, timezone

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

    # print(f"<<<<<<<<<<<<<<<< {message}, {email_list} >>>>>>>>>>>>>>>")

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
        print("No emails were sended - no subsriptions")


@shared_task
def block_users_who_was_absent_last_mount(block_absent, timedelta_days):
    # mount_ago = timezone.now().today().date() - timedelta(days=10)

    zone = pytz.timezone(settings.TIME_ZONE)
    mount_ago = datetime.now(zone) - timedelta(days=timedelta_days)

    users_no_login = User.objects.filter(last_login__isnull=True, date_joined__lte=mount_ago)
    users_login = User.objects.filter(last_login__isnull=False, last_login__lte=mount_ago)

    print(f"Users no login: {users_no_login.count()}")
    print(f"Users who was absent last month: {users_login.count()}")
    print(f"Users no login: {users_no_login}")
    print(f"Users who was absent last month: {users_login}")

    if block_absent:
        for users in users_no_login:
            users.is_active = False
            users.save()
        for users in users_login:
            users.is_active = False
            users.save()
