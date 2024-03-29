## Service Oriented Architecture - Microservices - Fundamentals, Tools & Tech Stack Course

SOA tech stack crash course. This project aims to help SOA course students get
familiar with the tools and the technology we'll be using during the lab exercises.
It is a showcase project for the fundamentals of microservices architecture.

#### What you'll need

* Windows or Linux or macOS machine
* Python 3.9 or later [Python Downloads](https://www.python.org/downloads/)
* Docker [Install Docker](https://docs.docker.com/engine/install/)
* Docker Compose [Install Docker Compose](https://docs.docker.com/compose/install/)

*Note - Docker Compose is installed as part of the standard Docker Desktop installation

#### Setup

To start the services as docker containers, simply run:
```
docker-compose up
```

If code updates are applied, a new docker image build is needed:

```
docker-compose build
docker-compose up
```

Or build and run with a single command:
```
docker-compose up --build
```

You can now access the two services:
- Items Service http://localhost:5002/items/docs
- Notifications Service http://localhost:5002/notifications/docs

or

- Items Service http://0.0.0.0:5002/items/docs
- Notifications Service http://0.0.0.0:5002/notifications/docs


#### Local (no-container) development

For local API development, we can still run the database in a container:
```
docker-compose up -d postgres-db-items
```

for the items service, or:
```
docker-compose up -d postgres-db-notifications
```
for the notifications service.

The database is now available on localhost:5432. This is configured in each .env file.

We need a Kafka broker running in a container:
```
docker-compose up -d broker
```

Let's run the items-service locally:
```
cd items-service
```

We need a virtual environment. We can create one with the command:
```
python -m venv venv
```

You can now access the service:
- Items Service http://localhost:5002/docs
- Notifications Service http://localhost:5004/docs

or

- Items Service http://0.0.0.0:5002/docs
- Notifications Service http://0.0.0.0:5004/docs


Activate the virtual environment with the following commands:

For Linux:
```
source venv/bin/activate
```

For Windows:
```
venv\Scripts\activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Run the service:
```
python devserver.py
```


#### Tips and Tricks

Windows users may encounter some problems because of the following difference:

- Windows ends lines in a carriage return and a linefeed \r\n,
- While Linux and macOS only use a linefeed \n.

To fix the problem, before git clone or git pull, run the following cmd:
```
git config --global core.autocrlf input
```

[ref.](https://github.com/docker/compose/issues/2301)
