# Tables of Contents

- [Quick Start](#quick-start)
- [Add Data](#add-data)

## Quick Start

1. Install requirements

```python
pip install -r requirements.txt
```

2. Create grader_web/local_settings.py. The example is available at [grader_web/local_settings.sample.py](grader_web/local_settings.sample.py) (basically just copy & paste)

3. Migrate

```python
python manage.py migrate
```

4. Run server

```python
python manage.py runserver
```

5. Your server will be running at [http://localhost:8000/](http://localhost:8000/). Hooray!

## Add Data

1. Create admin user

```python
python manage.py createsuperuser
```

2. Go to admin page at [http://localhost:8000/admin](http://localhost:8000/admin)

3. Enjoy!

# Django web app

- installation
  - clone and install programming.in.th/grader
  - config programming.in.th/grader and this
  - runserver
  - adjust docker compose file for proxy accordingly

# TODO :

- WS
- FrontEnd
- DEPLOY Test
