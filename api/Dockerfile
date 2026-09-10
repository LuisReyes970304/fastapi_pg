
FROM python:3.12-slim

#Define the app dir
WORKDIR /app

#Copy the package before the code.
COPY . ./api

#Install the requirements
RUN pip install --no-cache-dir -r ./api/requirements.txt

ENV PYTHONPATH=/app
WORKDIR /app/api

#These are the comand
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
