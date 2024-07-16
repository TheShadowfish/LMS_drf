from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from courses.models import Course, Lesson
from courses.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer
from users.permissions import IsModerator


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    # serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CourseCreateSerializer
        return CourseSerializer

    def get_permissions(self):

        if self.request.user.groups.filter(name="Moderators").exists():

            if self.action in ["create", "destroy"]:
                self.permission_classes = (~IsModerator,)
            elif self.action in ["update", "retrieve"]:
                self.permission_classes = (IsModerator,)
        # elif self.action != "create":
        #     self.permission_classes = (IsOwner,)
        return super().get_permissions()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # почему-то удалять запрещает всем пользователям - какая-то особенность DRF?
    # permission_classes = (~IsModerator, IsAuthenticated)

    # а так - работает на модератора и дает удалять простому пользователю
    def get_permissions(self):
        if self.request.user.groups.filter(name="Moderators").exists():
                self.permission_classes = (~IsModerator, IsAuthenticated)
        return super().get_permissions()
