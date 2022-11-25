FROM python

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py" ]

#ENTRYPOINT [ "python", "manage.py" ]
#CMD [ "runserver", "0.0.0.0:8000", "--noreload" ]