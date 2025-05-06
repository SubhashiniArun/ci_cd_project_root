CI/CD Project using Flask

This project deploys the [main_app](https://github.com/SubhashiniArun/flask_ci_cd) and [service_app](https://github.com/SubhashiniArun/flask_service_ci_cd) to Kubernetes


Detailed flow of the Project
* One main app -> used by client to fetch the data -> sends the user request to RabbitMQ async queue
* One service app -> process the user requests in RabbitMQ queue asynchronously.