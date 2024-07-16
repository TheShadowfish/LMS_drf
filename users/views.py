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

from users.models import User, Payments
from users.permissions import IsUserOwner
from users.serializers import UserSerializer, PaymentsSerializer, LimitedUserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ermission_classes = (IsUserOwner, IsAuthenticated)

    # def get_serializer_class(self):
    #     if self.owner == self.request.user:
    #         return UserSerializer
    #     else:
    #         return LimitedUserSerializer
    #
    # def get_permissions(self):
    #     if self.owner == self.request.user:
    #         self.permission_classes = (IsUserOwner, IsAuthenticated)
    #     else:
    #         self.permission_classes = (IsAuthenticated)
    #
    #     return super().get_permissions()

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = LimitedUserSerializer

    # def get_serializer_class(self):
    #     print(f"IsUserOwner {IsUserOwner().has_object_permission(self.request, self.view, self.obj)}")
    #
    #     if self.user == self.request.user:
    #
    #         user = self.request.user
    #         if user == self.object.mailing.user:
    #
    #         return UserSerializer
    #     else:
    #         return LimitedUserSerializer

    # def get_permissions(self):
    #     if IsUserOwner:
    #         self.permission_classes = (IsUserOwner, IsAuthenticated)
    #     else:
    #         self.permission_classes = (IsAuthenticated)
    #
    #     return super().get_permissions()


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
