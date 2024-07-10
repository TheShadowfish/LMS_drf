from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonCreateAPIView, LessonDestroyAPIView

router = SimpleRouter()
router.register("", CourseViewSet)


app_name = CoursesConfig.name

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons_retrieve"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lessons_delete"),

]

urlpatterns += router.urls
