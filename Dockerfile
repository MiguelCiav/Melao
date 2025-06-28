FROM python:3.12.4

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh .
RUN chmod 755 entrypoint.sh

COPY . .

RUN echo "Verificando el contenido de /app..."
RUN ls -la /app

EXPOSE 8000

CMD ["/bin/bash", "./entrypoint.sh"]