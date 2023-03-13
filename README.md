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

#### Tips and Tricks

Windows users may encounter some problems because of the following difference:

- Windows ends lines in a carriage return and a linefeed \r\n,
- While Linux and macOS only use a linefeed \n.

To fix the problem, before git clone or git pull, run the following cmd:
```
git config --global core.autocrlf input
```

[ref.](https://github.com/docker/compose/issues/2301)