# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11.3

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install -r requirements.txt
# Mounts the application code to the image
COPY . code
WORKDIR /code
RUN chmod 777 /code/*

EXPOSE 8000

WORKDIR /code/src/pyfloraposuda
# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]