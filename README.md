# store_with_stripe

https://store-with-stripe.herokuapp.com/

1 method:

1) Download all the libraries and packages with the required versions required for the project using the command:
```
pip install -r requirements.txt
```


2) We start docker, thereby creating a local database using the command:
```
docker-compose up -d db
```


3) Synchronizing migrations using the command:
```
python manage.py migrate
```


4) Create a superuser for administration using the command:
```
python manage.py createsuperuser 
```

5) Run the application locally using the command:
```
python manage.py runserver
```


2 method:

1) we start docker, thereby creating a local database and launching the application using the command:
```
docker-compose up -d
```


2) Synchronizing migrations using the command:
```
python manage.py migrate
```


3) Create a superuser for administration using the command:
```
python manage.py createsuperuser
```