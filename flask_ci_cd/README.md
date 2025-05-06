# APP

Setting up the App 
-> set up flask app
-> define app configurations in config.py file for better separation to load the env variables using load_dotenv()
-> load the configurations into app using *app.config.from_object()*
-> set up error handler globally for the app by defining logger(logging for application, logging into logfile)  
-> initialize extensions - DB (SQLAlchemy)
-> set up blueprint to register the routes

1. create User models in models file
2. use SQLAlchemy ORM to interact with MySQL Database
3. create RESFTful APIS to add, get, update and delete the resources. used blueprint to register the APIs
4. add unit tests to test the APIs
5. implement microservice architecture to call API from other [service app link](https://github.com/SubhashiniArun/flask_service_ci_cd)
6. set up logger functionality
------------------------------------------------------------------------------------------------------
7. deep dive into database connectivity (separating DB from APIs) and MySQL queries (complex queries - join multiples table) 
8. set up RabbitMQ queue for aysnc/background processing
9. deploy using CI/CD (Github Actions) to kubernetes 
10. including AWS EC2, Serverless lambda, S3,
11. Data analysis

Developed and containerized a microservice using Docker, and deployed it on Kubernetes with CI/CD pipelines (GitHub Actions), automating build, test, and deployment processes to accelerate release cycles and enhance system reliability.

