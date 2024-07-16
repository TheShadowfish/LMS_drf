from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from courses.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def create(self, validated_data):
        lessons = validated_data.pop("lessons")

        course_item = Course.objects.create(**validated_data)

        lesson_for_create = []

        for ls in lessons:
            lesson_for_create.append(Lesson(**ls, coutse=course_item))

        Lesson.objects.bulk_create(lesson_for_create)
        return course_item

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "preview",
            "description",
            "count_lessons",
            "lessons",
        )
