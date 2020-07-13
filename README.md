# django-employee-register-system

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mdcg/django-employee-register-system/blob/master/LICENSE)

A simple employee registration system written in Django. 

## First Steps

First of all, you will need to have Docker and Docker Compose installed on your machine. To do this, simply access the following links with the installation guides:

* [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)

Once both Docker and Docker Compose are installed, we will now need to create our environment variables.

To do this, initially go to the `config` folder and run the following command:

``` 
> cp .env-example .env
```

The above command will create a `.env` file where our environment variables will be stored. Now just open it and add the corresponding values ​​for each of the variables.

## Running

To run the system, simply run the following command:

``` 
> docker-compose up
```

The above command may take a while, so be patient.

## Creating a superuser

Make sure, first of all, that the system is running, as the following commands will have no effect otherwise.

You will initially need the hash of the container that Django is running. To do this, run the following command:

```
> docker container ps | grep django-employee-register-system_dev
```

You will see an output like this:

```
7eec065c2c7a        django-employee-register-system_dev   "sh -c 'python --ver…"   2 minutes ago       Up 2 minutes        0.0.0.0:8000->8000/tcp   django-employee-register-system_dev_1
```

Now you need to copy the hash of the container that Django is running (in my case the hash is `7eec065c2c7a`) and execute the following command together with it:

```
> docker exec -it <container_hash> sh
```

Right now you are inside the Django container. Run the following command:

```
> python manage.py createsuperuser
```

Now just enter the data for the superuser registration. Once you have registered, just type `exit` to return to your computer's shell.


## Contributing

Feel free to do whatever you want with this project. :-)