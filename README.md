# DifferentItFlights

---
An implementation of an API using Django Rest Framework in Serverless Architecture

## Description

API with base model 

```
type Flight {
  numberFlightID: ID!
  departureTimestamp: String
  arrivalTimestamp: String
  departureIata: String
  arrivalIata: String
  status: String
}
```

The API responds and receives information in JSON format.
The implementation consists of demonstration of the most common http protocols (GET, POST, PUT, DELETE), and the API is running on AWS using a Lambda function.
(No persistant data, only transactional data)

## Getting Started


### Local

For local operation, you must do git clone and then start a virtual environment.
```
python -m venv venv

```
Next, you must install the dependencies required for the API to work.

```
Python -m pip install -r requirements.txt

```
Finally, you must do the process of mounting and running the Django application.

```
cd DifferentItTest

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

### Remote (recommended)

Because the API is running on an AWS Lambda it can be accessed via the following link

https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/

#### URL URIs

The urls that the API has are :

*{'url': 'https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/'  , 
            'method': 'GET' ,
             'description': 'Get all Basic API urls'}
* { 'url' : 'https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/'   ,
            'method': 'GET',
            "description": "List all flights" }
* { 'url' : 'https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/',
            "method": "POST",
            "description": "Create a new flight"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/<int:pk>/",
            "method": "GET",
            "description": "Get a flight by ID"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/<int:pk>/",
            "method": "PUT",
            "description": "Update a flight"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/<int:pk>/",
            "method": "DELETE",
            "description": "Delete a flight"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/departure/<str:departureIata>/",
            "method": "GET",
            "description": "Get a flight by departure IATA"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/arrival/<str:arrivalIata>/",
            "method": "GET",
            "description": "Get a flight by arrival IATA"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/departure/<str:departureIata>/arrival/<str:arrivalIata>/",
            "method": "GET",
            }, "description": "Get a flight by departure IATA and arrival IATA"}
* { "url": "https://ptg1qdsg00.execute-api.us-east-2.amazonaws.com/dev/flights/status/<str:status>/",
            "method": "GET",
            "description": "Get a flight by status"}

## Development process

1. Design of the API, using Django Rest, in this way we make use of Routers, Serializers, Views, Models, SQLite DB
2. For Serverless implementation in AWS we used a python module that facilitates the deploy to AWS called ZAPPA, creating a lambda function [Here](https://www.youtube.com/watch?v=WaiL4sba).
2.1. Because ZAPPA makes a connection to AWS services, we must create 1 user in IAM with the permissions to create S3 instances, Lambda, ApiGateway plus extra permissions, in case services such as EFS are used.
2.2. Then we start ZAPPA with the command ``` zappa init``` where we will be asked for the access key and secret access key of the user we created in IAM, in addition to asking for the name we want to give to the lambda function and the address of our django project settings file.
2.3. Once ZAPPA is configured, we must make the first deploy to AWS using ```zappa deploy dev``` being dev, the name of the environment that we defined in the previous step.
2.4. As a result and if everything went correctly zappa init will return the URL of our gateaway with which we can make the http requests to our API.
2.5. If we have made changes in the Django code, we can update our lambda using the command ```zappa update dev ```.

### Resources consulted for development

* [https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design)
* [https://github.com/efi-mk/serverless-django-demo](https://github.com/efi-mk/serverless-django-demo)
* [https://github.com/zappa/Zappa](https://github.com/zappa/Zappa)
* [https://github.com/veryacademy/YT-Django-Serverless-Deploy-Zappa-v1](https://github.com/veryacademy/YT-Django-Serverless-Deploy-Zappa-v1)
* [https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html)
* [Zappa + GateWay deploy](https://www.youtube.com/watch?v=WaiL4sba)


## Authors

Contributors names and contact info

 Carlos Gutierrez  
 [@LinkedIn](https://www.linkedin.com/in/carlos-javier-gutierrez-torres-389708214/)

