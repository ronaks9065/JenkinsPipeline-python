FROM python:3.6
COPY .  /flask_project
WORKDIR /flask_project
RUN pip install -r requirements.txt
EXPOSE  8081
CMD ["python", "app.py"]
