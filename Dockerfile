FROM python:3.12.7
WORKDIR /app

COPY ./main.py /app/
COPY ./requirements.txt /app/
COPY ./com /app/com

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

FROM postgres:15
RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen ko_KR.UTF-8
ENV LANG=ko_KR.UTF-8
ENV LANGUAGE=ko_KR:ko
ENV LC_ALL=ko_KR.UTF-8