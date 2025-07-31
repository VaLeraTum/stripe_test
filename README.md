### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ValeraTum/yatube.git
```

```
cd stripe_test
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```
* Если у вас Linux/macOS

```
source venv/bin/activate
```
* Если у вас windows

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
cd stripes
```

```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
