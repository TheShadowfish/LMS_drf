from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView, ListAPIView

from users.models import User
from users.serializers import UserSerializer


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

