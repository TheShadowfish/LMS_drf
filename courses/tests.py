from rest_framework.reverse import reverse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Lesson, Course
from users.models import User

#
"""
Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.

В тестах используйте метод 
setUp
 для заполнения базы данных тестовыми данными. Обработайте возможные варианты взаимодействия с контроллерами пользователей с разными правами доступа. Для аутентификации пользователей используйте 
self.client.force_authenticate()
. Документацию к этому методу можно найти тут.
"""


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")

        self.course = Course.objects.create(title='Курс номер 1', description='Описание курса номер 1',  owner=self.user)

        video = "https://www.youtube.com/watch?v=uC0jJGfDxtM&list=PLlb7e2G7aSpTFea2FYxp7mFfbZW-xavhL&index=1"

        self.lesson = Lesson.objects.create(title='Урок номер 1', course=self.course , description="описание" , video_url=video, owner=self.user)

        self.client.force_authenticate(user=self.user)


    def test_course_retrieve(self):
        url = reverse("courses:course-detail", args=(self.course.pk,))
        # dogs:dog-detail
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.course.title)

    def test_course_create(self):
        url = reverse("courses:course-list")
        data = {"title": "Курс 2"}
        response = self.client.post(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = reverse("courses:course-detail", args=(self.course.pk,))
        data = {"title": "Курс 1"}
        response = self.client.patch(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), "Курс 1")

    def test_course_delete(self):
        url = reverse("courses:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse("courses:course-list")
        response = self.client.get(url)

        data = response.json()
        print(data)

        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.course.pk,
                        'title': self.course.title,
                        'preview': None,
                        'description': self.course.description,
                        'owner': self.user.pk,
                        'count_lessons': 1,
                        'lessons':
                            [
                                {
                                    'id': self.lesson.pk,
                                    'title': self.lesson.title,
                                    'description': self.lesson.description,
                                    'preview': None,
                                    'video_url': self.lesson.video_url,
                                    'course': self.course.pk,
                                    'owner':  self.user.pk,
                                }
                            ],
                        'created_at': str(self.course.created_at),
                        'updated_at': str(self.course.updated_at),
                        'subscriptions': False
                    }
                ]
        }
        #2024-07-25T07:54:27.529849Z
        #Создает объект datetime из строки
        # "2019-08-26T10:50:58.294041"
        # datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S.%f')


        # 'created_at': '2024-07-25T07:43:42.219321Z', 'updated_at': '2024-07-25T07:43:42.219342Z'
        print(f"created_at:{self.course.created_at} updated_at:{self.course.updated_at}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
#
#
# class BreedTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(email="admin@sky.pro")
#         self.breed = Breed.objects.create(name='Лабрадор', breed="Большая мохнатая красивая белая собака", owner=self.user)
#         self.dog = Dog.objects.create(name="Гром", breed=self.breed, owner=self.user)
#         self.client.force_authenticate(user=self.user)
#
#     def test_breed_retrieve(self):
#         url = reverse("dogs:breeds-retrieve", args=(self.breed.pk,))
#         response = self.client.get(url)
#         data = response.json()
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get('name'), self.breed.name)
#
#     def test_breed_create(self):
#         url = reverse("dogs:breeds-create")
#         data = {
#             "name": "Овчарка"
#                 }
#         response = self.client.post(url, data)
#
#         data = response.json()
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Dog.objects.all().count(), 1)
#
#     def test_breed_update(self):
#         url = reverse("dogs:breeds-update", args=(self.breed.pk,))
#         data = {"name": "Лайка"}
#         response = self.client.patch(url, data)
#
#         data = response.json()
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get('name'), "Лайка")
#
#     def test_breed_delete(self):
#         url = reverse("dogs:breeds-delete", args=(self.breed.pk,))
#         response = self.client.delete(url)
#
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Breed.objects.all().count(), 0)
#
#     def test_breed_list(self):
#         url = reverse("dogs:breeds-list")
#         response = self.client.get(url)
#
#         data = response.json()
#         # print(data)
#
#         result = {
#             'count': 1,
#             'next': None,
#             'previous': None,
#             'results':
#                 [
#                     {'id': self.breed.pk,
#                      'dogs': [self.dog.name],
#                      'name': self.breed.name,
#                      'breed': self.breed.breed,
#                      'owner': self.user.pk
#                      }
#                 ]}
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data, result)
#
