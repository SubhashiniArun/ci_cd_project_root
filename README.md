## MicroServices Architecture - CI/CD Project using Flask

This project deploys the [main_app](https://github.com/SubhashiniArun/flask_ci_cd) and [service_app](https://github.com/SubhashiniArun/flask_service_ci_cd) to Kubernetes using Github Actions (CI/CD)

### Steps to run the app locally

##### Main app:
* navigate to the main app (flask_ci_cd)
* virtualenv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python run.py
* check the app's health http://localhost:8000/api/health


##### Service app:
* navigate to the service app (flask_service_ci_cd)
* virtualenv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python run.py
* check the app's health http://localhost:5001/serviceapi/health

##### RabbitMQ
* start the rabbitmq locally. It runs on the port 15672 

#### App Testing 
* Test the microservice functionality by sending GET request to http://localhost:8000/api/users, it will send the request to the service app (http://localhost:5001/serviceapi/users)

* Test the async processing of the app by sending GET request to http://localhost:8000/api/process_user with {ids: []} as JSON body
* Visualize the queue getting initialized in RabbitMQ (http://localhost:15672)
* In the Service app's terminal you could see the logs that message is consume from the queue and processed 

#### Architecture & flow of the Project
* One main app -> used by client to send the user requests to RabbitMQ queue
* One service app -> process the user requests in RabbitMQ queue asynchronously.

###### Docker
* 2 Apps (main app & service app) has its own Dockerfile

###### Github Actions (CI/CD)
* Build the docker images of the apps (main app and service app) and push the images to Docker Hub Respository.
* Automate the build and deployment to Kubernetes 

###### Kubernetes
* Each app with its own Pods/images runs on a cluster
* Define the replicas of the cluster to scale the app
* Resources: Deployment environment, Service enviornment

Kubernetes Overview:
* Control plane: Handles scheduling/scaling
* Worker Nodes: runs the application containers inside pods

* We can auto scale the pods using Horizontal Pod Autoscaler based on the CPU/memory usage
* We can manually scale the app by setting the repliacs using kubectl >> kubectl scale deployment my-app
--replicas=5

Service in Kubernetes:  * Provide network identity (DNS & IP) to set of pods
                        * Automatically updates when pods scale up and down
                        * Support load balancing across pods
                        * Expose pods internally (clusterIP) or externally (load balancer)


![alt text](https://github.com/SubhashiniArun/ci_cd_project_root/blob/main/flow.png)


#### Local testing Kubernetes using minikube

* install minikube
* mnikube start
* minikube start --driver=docker
* eval $(minikube docker-env)
* build the docker images (refer deploy.yml in .github/workflows for build syntax)
* apply all the kubernetes resources using "kubectl apply -f k8s/flask_ci_cd_deployment.yaml"
* get the external ip "minikube service flask_ci_cd --url --namespace=app-microservices-rabbitmq-ci-cd"
* use this url in the .env file and run the smoke tests





