FROM python:3.9-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt
RUN pip install pydantic==2.4.2

COPY . .

EXPOSE 8000

CMD ["python", "src/main.py"]