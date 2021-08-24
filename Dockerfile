FROM python:3.9-slim-buster as dev

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD /requirements/base.txt .
RUN ls
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python -m pip install -r base.txt

WORKDIR /app
ADD . /app

RUN useradd -u 5678 appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
