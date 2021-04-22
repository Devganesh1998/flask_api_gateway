## Introduction
A Flask API gateway featuring three microservices: users, shows, and products.

#### Requirements
Tools:
- python3
- docker-compose
- docker

Python modules:
- See requirements.txt

#### Usage
1. Make sure the port `5000` is free in your machine and run the command
    ```bash
    docker-compose up
    ```
2. Visit [http://localhost:5000/api/v1/products/lists](http://localhost:5000/api/v1/products/lists) to make the gateway hit the product service and get back the result.
3. List of services and their routes
    - User service
        - Home - [http://localhost:5000/api/v1/users](http://localhost:5000/api/v1/users)
        - Lists - [http://localhost:5000/api/v1/users/lists](http://localhost:5000/api/v1/users/lists)
    - Product service
        - Home - [http://localhost:5000/api/v1/products](http://localhost:5000/api/v1/products)
        - Lists - [http://localhost:5000/api/v1/products/lists](http://localhost:5000/api/v1/products/lists)
    - Show service
        - Home - [http://localhost:5000/api/v1/shows](http://localhost:5000/api/v1/shows)
        - Lists - [http://localhost:5000/api/v1/shows/lists](http://localhost:5000/api/v1/shows/lists)
5. Begin making HTTP Requests to the API.
6. Checkout api_pkg/services to add or alter services.

