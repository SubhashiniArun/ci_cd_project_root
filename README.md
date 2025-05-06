CI/CD Project using Flask

This project deploys the [main_app](https://github.com/SubhashiniArun/flask_ci_cd) and [service_app](https://github.com/SubhashiniArun/flask_service_ci_cd) to Kubernetes


Detailed flow of the Project
* One main app -> used by client to send the user request to RabbitMQ async queue
* One service app -> process the user requests in RabbitMQ queue asynchronously.

Architecture

Docker
-> 2 Apps (main app and service app) has its own Dockerfile

Github Actions
-> Automate the build and deployment to Kubernetes
-> Build the docker images of the apps (main app and service app) and push the images to Docker Hub Respository. 

Kubernetes
-> Each app with its own Pods/images runs on a cluster
-> Define the replicas of the cluster to scale the app
-> Resources: Deployment environment, Service enviornment


Kubernetes Overview:

Control plane: Handles scheduling/scaling
Worker Nodes: runs the application containers inside pods

We can auto scale the pods using Horizontal Pod Autoscaler based on the CPU/memory usage
We can manually scale the app by setting the repliacs using kubectl kubectl scale deployment my-app
--replicas=5

Service in Kubernetes:  Provide network identity (DNS & IP) to set of pods
                        Automatically updates when pods scale up and down
                        Support load balancing across pods
                        Expose pods internally (clusterIP) or externally (load balancer)


[Client/Browser]
      |
(curl http://main-app.my-cluster.com/user-request-job)
      |
      v
+---------------+
|   Main App    |  <--- Has Service (LoadBalancer / ClusterIP)
+---------------+
      |
     RabbitMQ (Producer) (amqp://rabbitmq:5672)
      |
      v
+---------------+    <--- Has Service (ClusterIP)
|   RabbitMQ    |    <--- Shared queue (job1, job2, ...)
+---------------+
      ^
      |
  RabbitMQ (Consumer) (amqp://rabbitmq)
      |
+---------------+
|  Service App  |    <--- No Service needed
+---------------+





