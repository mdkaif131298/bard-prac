# Monolithic and Microservices Example

This project demonstrates a simple Flask-based e-commerce application implemented with both a monolithic and microservices architecture.

## Monolithic Architecture

In the monolithic architecture, the application is implemented as a single, self-contained unit. All functionality, including product management and order processing, is handled within a single Python application.

### Running the Monolithic Application

To run the monolithic application, follow these steps:

1. Open a terminal and navigate to the root directory of the project.
2. Run the following command to start the monolithic application on port 5003:

```
python app.py
```

Access the monolithic application in your web browser at http://localhost:5003.

## Microservices Architecture

In the microservices architecture, the application is split into two separate microservices: `products_service` for managing products and `orders_service` for processing orders. These services communicate over HTTP.

### Separated Services

- **Products Service (`products_service`):** This microservice is responsible for managing product information. It provides endpoints for listing products.

- **Orders Service (`orders_service`):** This microservice handles order processing. You can place orders by sending a POST request to the `/place_order` endpoint.

### Running the Microservices

To run the microservices, follow these steps:

1. Open a terminal and navigate to the `products_service` directory.
2. Run the following command to start the products service on port 5001:

```bash
cd products_service
python app.py
```
Open another terminal and navigate to the `orders_service` directory. 
Run the following command to start the orders service on port 5002:

```bash
cd orders_service
python app.py
```

Access the products service in your web browser at http://localhost:5001.
Access the orders service in your web browser at http://localhost:5002.

## Usage

- In both the monolithic and microservices architectures, you can access product information.
- In the monolithic architecture, you can place orders through the same application.
- In the microservices architecture, you can place orders by sending a POST request to the `orders_service` endpoint: http://localhost:5002/place_order.