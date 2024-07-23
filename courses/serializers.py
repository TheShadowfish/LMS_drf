from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from courses.models import Course, Lesson
from courses.validators import VideoUrlValidator
from users.models import Subscriptions


class LessonSerializer(ModelSerializer):
    validators = [VideoUrlValidator(field='video_url')]

    # serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Lesson.objects.all())

    class Meta:
        model = Lesson
        fields = "__all__"

    def create(self, validated_data):
        course = validated_data.pop("course")

        course_item = Course.objects.filter(pk=course)
        course_item.save()

        lesson_item = Lesson.objects.create(**validated_data)

        return lesson_item


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    subscriptions = SerializerMethodField(read_only=True)



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

    def get_subscriptions(self, obj):

        owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

        user_pk = owner.get_value("pk")
        # return (f"user_pk {user_pk}, owner {owner}, user {CurrentUserDefault}")

        return [
            f"{s.course}-(pk={s.course.pk}{bool(s.last_date < s.course.updated_at) * ' Курс обновлен!'}),"
            for s in Subscriptions.objects.filter(course=obj).filter(user=CurrentUserDefault).order_by("last_date")
        ]

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "preview",
            "description",
            "owner",
            "count_lessons",
            "lessons",
            "created_at",
            "updated_at",
            "subscriptions"
        )


class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
