from datetime import datetime, timedelta, timezone

import pytz
from celery import shared_task
from dateutil.relativedelta import relativedelta

from config import settings
from users.models import User


@shared_task
def block_users_who_was_absent_last_mount():

    # zone = pytz.timezone(settings.TIME_ZONE)
    # mount_ago = datetime.now(zone) - timedelta(days=timedelta_days)
    # users_no_login = User.objects.filter(last_login__isnull=True, date_joined__lte=mount_ago)
    # users_login = User.objects.filter(last_login__isnull=False, is_active=True, last_login__lte=mount_ago)

    users_login = User.objects.filter(last_login__isnull=False, is_active=True, last_login=timezone.now() - relativedelta(months=1))
    users_login.update(is_active=False)


    # print(f"Users no login: {users_no_login.count()}")
    # print(f"Users who was absent last month: {users_login.count()}")
    # print(f"Users no login: {users_no_login}")
    # print(f"Users who was absent last month: {users_login}")

    # if block_absent:
    #     for users in users_no_login:
    #         users.is_active = False
    #         users.save()
    #     for users in users_login:
    #         users.is_active = False
    #         users.save()
