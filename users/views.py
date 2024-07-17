from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import User, Payments
from users.permissions import IsUserOwner
from users.serializers import UserSerializer, PaymentsSerializer, LimitedUserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ermission_classes = (IsUserOwner, IsAuthenticated)

    def get_serializer_class(self):
        if self.request.method == 'GET' and self.get_object() != self.request.user:
            return LimitedUserSerializer
        return UserSerializer

    def update(self, request, *args, **kwargs):
        if self.get_object() != request.user:
            return Response({'detail': 'You do not have permission to edit this user.'}, status=403)
        return super().update(request, *args, **kwargs)




class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOwner,)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()



# payments


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    """
    Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:

    - менять порядок сортировки по дате оплаты,
    - фильтровать по курсу или уроку,
    - фильтровать по способу оплаты.
    """

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("course", "lesson", "payment_method_is_cash")
    ordering_fields = ("date_of_payment",)


class PaymentsRetrieveAPIView(RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsUpdateAPIView(UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyAPIView(DestroyAPIView):
    queryset = Payments.objects.all()
