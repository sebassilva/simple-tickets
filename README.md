# Configuración inicial

1) Descarga este repositorio
 `git clone https://github.com/sebassilva/simple-tickets`

2) Descarga e instala python3
2) Instala [django 2.1.2](https://www.djangoproject.com/)
3) Descarga e istala [Django Rest Framework](https://www.django-rest-framework.org/tutorial/1-serialization/)

4) Corre las migraciones
`python3 manage.py makemigrations`
`python3 manage.py migrate`

5) Corre el servidor
`python3 manage.py runserver`

6) El servidor correrá en el puerto 8000 de localhost, por lo que puedes acceder a la siguiente[url](http://localhost:8000/ticket/)

7) Puedes crear tickets manualmente en la página anterior o puedes correr el script que genera 100 tickets
`python3 autogenerate.py`
