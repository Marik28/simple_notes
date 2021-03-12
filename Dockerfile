FROM python:3.9

WORKDIR /usr/src/notes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN ["chmod", "a+x", "/usr/src/notes/entrypoint.sh"]
RUN ls -l .

EXPOSE 8000

ENTRYPOINT ["sh", "/usr/src/notes/entrypoint.sh"]
