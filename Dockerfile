FROM python:3.11-slim

SHELL ["/bin/bash", "-c"]

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron \
    openssh-client flake8 locales vim

RUN useradd -rms /bin/bash app && chmod 777 /opt /run

WORKDIR /app

COPY . /app/

RUN chmod +x manage.py

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt gunicorn

USER app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
