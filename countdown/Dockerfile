FROM python:alpine

ENV TZ="America/Chicago"
RUN pip install flask
WORKDIR /app
COPY app.py countdown_dates.txt /app/
COPY static/ /app/static/
COPY templates/ /app/templates/

EXPOSE 5000

CMD ["python3", "app.py"]
