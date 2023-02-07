# ecom-today---todo-list

## Зависимости.
- Python3
- Django
- Django Rest Framework

### Локальный запуск проекта.
- Откройте терминал и перейдите в ту директорию, в которой будет располагаться проект.
- Склонируйтуе проект к себе на машину:
```python
git clone https://github.com/RomanMelnikS/ecom-today---todo-list.git
```
- Cоздайте и активируйте виртуальное окружение:
```python
python -m venv 'venv'
source venv/Scripts/activate
pip install -r requirements.txt
```
- Выполните команды:
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Проект запустится локально на вашей машине и будет доступен по ссылке http://127.0.0.1:8000/.

Задача:
Необходимо создать Django приложение Todo List. У приложение должно быть 5 Api
методов:
1. Создание записи /api/record/create - POST
2. Чтение записи /api/record/get?uuid={string} - GET
3. Список записей /api/records/all - GET
4. Список записей на указанные даты
/api/records/list?start={DD.MM.YY}&end={DD.MM.YY} - GET
5. Удаление записи /api/record/delete?uuid={string} - DELETE
Все записи должны храниться в БД.
У модели должно быть 5 полей
id - служебное поле каждой модели, описывать в файле модели не надо.
uuid - Уникальная строка из 8 символов;
created - Дата и время создания;
body - Текстовое поле длинной до 2000 символов;
active - Логическое поле, по умолчанию True;
Для генерации UUID записи, необходимо прописать класс, который будет отвечать за
генерацию идентификатора, и проверять не существует ли записи со сгенерированным
идентификатором.
Технологии:
Python 3.10, Django, Django Rest Framework
Проект должен находиться на GitHub
В корне проекта должен быть файл requirement.txt со всеми библиотеками
проекта и их версиями.
Базы данных можно использовать любую, по своему усмотрению.