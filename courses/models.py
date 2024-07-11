from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="course/preview",
        verbose_name="Превью",
        help_text="Загрузите превью курса (картинка)",
        **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса", **NULLABLE
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


"""
Урок:
название,
описание,
превью (картинка),
ссылка на видео.
"""


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    # уроков, которые не входят ни в какой курс быть по логике не должно
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Введите курс",
        related_name="lessons",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока", **NULLABLE
    )
    preview = models.ImageField(
        upload_to="lesson/preview",
        verbose_name="Превью",
        help_text="Загрузите превью урока (картинка)",
        **NULLABLE
    )
    video_url = models.CharField(
        **NULLABLE,
        max_length=300,
        verbose_name="Ссылка на видео урока",
        help_text="Укажите ссылку на видео урока"
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name
