# Library Management System API

A Django-based backend API for managing a library system, including user management, book checkouts and returns, fine management, and more.

---

## Features

- User authentication and management.
- Book management (add, update, and track books).
- Book checkout and return functionality.
- Fine management for overdue checkouts.
- Book reviews and tagging system.

---

## Setup Instructions

Follow these steps to set up and run the project on your local machine:

### Prerequisites
- Python 3.8 or higher
- Git

### Steps

1. **Clone the repository**  
   Clone the project repository from GitHub:
   ```bash
   git clone https://github.com/Anassnaj/Library-Management-System-API.git

# Authentication Setup for Social Media API

## Overview
This project uses Django Rest Framework for building the Social Media API. Authentication is handled via Token Authentication (or JWT) to secure the endpoints.

# Social Media API - Authentication Setup

## Overview
This repository contains the source code for a Social Media API built with Django and Django Rest Framework (DRF). The API includes authentication features to secure access to protected endpoints using token-based authentication.

## Authentication Method
The API uses **JWT (JSON Web Token)** for authentication. JWT provides a stateless and secure method for handling authentication, where users authenticate once and receive an access token that can be used for subsequent requests.

## Setting Up Authentication

### Step 1: Install Required Packages
Install Django Rest Framework and the SimpleJWT package for JWT-based authentication:

```bash
pip install djangorestframework djangorestframework-simplejwt
Step 2: Update settings.py
In your settings.py, add 'rest_framework' and configure the authentication settings for JWT.

Add 'rest_framework' to INSTALLED_APPS:

python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
Add the following configuration for JWT authentication:

python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
Step 3: Add Authentication URLs
In your urls.py, include the routes for obtaining and refreshing JWT tokens:

python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   ...
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint to obtain JWT token
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint to refresh JWT token
]
Step 4: Protect API Endpoints
To secure your API endpoints, use the IsAuthenticated permission class. This will require users to be authenticated before they can access the endpoints.

Example:

python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class PostList(APIView):
    permission_classes = [IsAuthenticated]  # Ensures the user is authenticated

    def get(self, request):
        # Your view logic here
        return Response({"message": "This is a protected post."})
Step 5: Testing Authentication
Get the JWT Token:
To authenticate a user and obtain a JWT token, send a POST request to the /api/token/ endpoint with your username and password:

bash
curl -X POST -d "username=<your-username>&password=<your-password>" http://127.0.0.1:8000/api/token/
The response will include both an access token and a refresh token:

json
{
    "access": "<your-access-token>",
    "refresh": "<your-refresh-token>"
}
Use the Access Token:
Once you have the access token, you can include it in the Authorization header for protected API requests:

bash
Authorization: Bearer <your-access-token>
Step 6: Refreshing the JWT Token
If the access token expires, you can refresh it by sending a POST request to the /api/token/refresh/ endpoint with your refresh token:

bash
curl -X POST -d "refresh=<your-refresh-token>" http://127.0.0.1:8000/api/token/refresh/
This will return a new access token.

Testing the API
You can test the authenticated routes using tools like Postman or curl. If a valid token is not provided in the Authorization header, the API will respond with a 403 Forbidden status code.

Example API Call:
To get a protected list of posts, use the following curl command with the token:

bash
curl -H "Authorization: Bearer <your-access-token>" http://127.0.0.1:8000/api/posts/
This will return the list of posts, provided the token is valid.

Conclusion
This setup ensures that only authenticated users can access the protected API endpoints. The JWT tokens are stateless and can be used to make multiple API requests without requiring users to log in repeatedly.

License
This project is licensed under the MIT License - see the LICENSE file for details.
