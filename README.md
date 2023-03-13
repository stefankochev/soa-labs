## Service Oriented Architecture - Tools & Tech Stack Course

SOA tech stack crash course. This project aims to help SOA course students get
familiar with the tools and the technology we'll be using during the lab exercises.

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

#### Local (no-container) development

For local API development, we can still run the database in a container:
```
docker-compose up -d postgres-db
```

The database is now available on localhost:5432. This is configured in the src/.env file.

We need a virtual environment. We can create one with the command:
```
python -m venv venv
```

Activate the env with:
```
source venv/bin/activate
```

for Windows:
```
venv\Scripts\activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Setup PYTHON PATH:
```
export PYTHONPATH=.
```

for Windows:
```
set PYTHONPATH=.
```

Run the API:
```
python src/devserver.py
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