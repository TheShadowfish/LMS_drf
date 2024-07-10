# Entry points:

**Courses**:
http://localhost:8000/courses/

**Lessons**:

list: http://localhost:8000/courses/lessons/

retrieve: http://localhost:8000/courses/lessons/<int:pk>/

update: http://localhost:8000/courses/lessons/<int:pk>/update/

create: http://localhost:8000/courses/lessons/create/

delete: http://localhost:8000/courses/lessons/create/<int:pk>/delete/

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
Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью 
SerializerMethodField()

# Задание 2 (+)
Добавьте новую модель в приложение users:

**Платежи**

- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

Поля 
**пользователь**
, 
**оплаченный курс
 и 
отдельно оплаченный урок**
 должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.

Если вы забыли как работать с фикстурами или кастомной командой - можете вернуться к уроку 20.1 Работа с ORM в Django чтобы вспомнить материал.

# Задание 3
Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод реализуйте с помощью сериализатора для связанной модели.

Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

# Задание 4
Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:

- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

# Дополнительное задание
Для профиля пользователя сделайте вывод истории платежей, расширив сериализатор для вывода списка платежей