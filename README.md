
My first Django project: managing a to-do list, stored in a browser cookie

Install & Run (... but note that your environment may have different file locations, etc)
- export WORKON_HOME=~/.python-envs
- source /usr/local/bin/virtualenvwrapper.sh
- mkvirtualenv django-test
- pip install -r pip-requirements.txt
- python manage.py runserver
... then just browse to this location: http://127.0.0.1:8000/todolist/


Notes
- For production project, I would have started with test scripts.
  (Selenium in this case... it's not to the level of unit tests yet.)
- no server-side persistence (no item IDs, etc)
- no cookie format checking
- When dependencies change: pip freeze > pip-requirements.txt


To Do
- testing
- edit items
- true RESTful architecture
- AJAX (no page reloads)
- drag to new position

