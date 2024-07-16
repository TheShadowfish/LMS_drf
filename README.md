# Entry points:

**Courses**:
http://localhost:8000/courses/

**Lessons**:

list: http://localhost:8000/courses/lessons/

retrieve: http://localhost:8000/courses/lessons/<int:pk>/

update: http://localhost:8000/courses/lessons/<int:pk>/update/

create: http://localhost:8000/courses/lessons/create/

delete: http://localhost:8000/courses/lessons/<int:pk>/delete/

**users**

list: http://localhost:8000/users/

retrieve_update: http://localhost:8000/users/<int:pk>/retrieve_update/

**payments**

list: http://localhost:8000/payments/

retrieve: http://localhost:8000/payments/<int:pk>/

create: http://localhost:8000/payments/create/

update: http://localhost:8000/payments/<int:pk>/update/

delete: http://localhost:8000/payments/<int:pk>/delete/

# Загрузка данных

Фикстуры с данными в папке **data**, порядок загрузки

1) python3 manage.py loaddata data/courses.json
2) python3 manage.py loaddata data/users.json

=========================================================

# Задание 1 (+)
Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.

Эндпоинты для авторизации и регистрации должны остаться доступны для неавторизованных пользователей.

# Задание 2 (+)
Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.

# Задание 3
Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.

**Примечание**

Заводить группы лучше через админку и не реализовывать для этого дополнительных эндпоинтов.

# Дополнительное задание
Для профиля пользователя введите ограничения, чтобы авторизованный пользователь мог просматривать любой профиль, но редактировать только свой. При этом для просмотра чужого профиля должна быть доступна только общая информация, в которую не входят: пароль, фамилия, история платежей.