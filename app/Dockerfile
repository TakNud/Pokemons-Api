FROM python:3.9
WORKDIR /app
COPY /app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pwd
RUN ls
CMD ["python", "app/mainAPI.py"]
EXPOSE 5000

