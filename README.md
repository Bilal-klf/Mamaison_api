# Mamaison_api

This Django-based API project provides functionalities for managing user records and house data. It includes endpoints for user registration, authentication, and retrieving house data.

## Features

- **User Registration:** Allows the creation of new users with fields for name, email, password, and phone number.

- **User Authentication:** Provides a mechanism for user authentication via email and password.

- **House Data Management:** Allows retrieval of house data including temperature, humidity, and windows status.

## Technologies Used

- Django: A high-level Python web framework for rapid development and clean, pragmatic design.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs in Django.
- MySQL: An open-source relational database management system used for storing data.


## Endpoints

- **Admin Interface:** Access the Django admin interface for managing users and house data.

- **User Registration Endpoint:** `/saveUser/`
- Method: `POST`
- Create a new user by providing `name`, `email`, `password`, and `phone_number`.

- **User Authentication Endpoint:** `/getUser/`
- Method: `POST`
- Authenticate a user by providing `email` and `password`.

- **House Data Retrieval Endpoint:** `/getHouseData/`
- Method: `GET`
- Retrieve all house data including temperature, humidity, and windows status.

- **Obtain Authentication Token Endpoint:** `/api-token-auth/`
- Method: `POST`
- Obtain an authentication token for accessing authenticated endpoints.
