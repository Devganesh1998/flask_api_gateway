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


#### To test file transfer
1. Make sure the port `5000` is free in your machine and run the command
    ```bash
    docker-compose up
    ```
2. Open a new terminal and run the following commands.
    ```bash
    cd frontEndTest/
    yarn dev
    ```
3. Open an another new terminal and run the following commands.
    ```bash
    cd frontEndTest/
    yarn serve
    ```
4. Now open browser with this following link - [http://localhost:5006/](http://localhost:5006/)
5. You can select a file by clicking on `choose file` button and then after selecting a file, you can upload the selected file to product service by clicking the `upload` button (this button hits this endpoint `/api/v1/products/file` and receives the sent file as response). To save/download the uploaded file to your system click on the `download` button.
