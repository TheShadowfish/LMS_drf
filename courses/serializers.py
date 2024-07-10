from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from courses.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'count_lessons',)


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"



