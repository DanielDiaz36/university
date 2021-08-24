# * University website *

````
Demo: https://firedevs-university.herokuapp.com/
User: admin
Pass: admin
````
#### Steps to deploy project:
1. Install python 3.9
2. Create virtual environment:
``python -m venv venv_university``
3. Active environment:
``venv_university\Scripts\activate.bat``
4. Install packages:
``pip install -r requirements.txt``
5. Convigure .env (use .env.sample)
6. Run migrations:
``python manage.py migrate``
7. Run command load:
``python manage.py load``
8. Run server
``python manage.py runserver``
9. Login:
````
User: admin
Pass: admin
````