from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, \
    UpdateAPIView

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# как создать пользователя через Postman чтобы пароль зашифровался как при обычном создании пользователя?
# интересно конечно, хотя домашку примут и без этого.
# PS просто создать с нешифрованым паролем получилось

# class UserCreateAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDestroyAPIView(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# payments


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


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


