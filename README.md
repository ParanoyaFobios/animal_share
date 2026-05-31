# AnimalShare

AnimalShare is a Django-based educational project that combines a community forum for finding lost or adopted animals with a simple online store. It is designed as a full-stack learning application with user accounts, media uploads, messaging, commenting, and shopping cart features.

## Key Features

### Forum and Community
- User registration and login
- Profile editing with avatar upload
- Password reset via email configuration
- Create, edit, and delete animal-related posts
- View posts by other users
- Comment on posts
- Real-time unread message count in the interface
- Private messaging between users

### Shop and Marketplace
- Product catalog with categories
- Category filtering and sorting support
- Product pages with pricing and discount calculations
- Shopping cart for logged-in users
- Order creation with delivery and payment options
- Admin management for products, categories, and orders

### Admin and Data Management
- Django admin site to add or update products, categories, posts, and users
- Custom admin displays and utilities for cart and order management
- Database-backed models for users, posts, comments, products, carts, orders, and messages

## Technology Stack

- Python >= 3.12
- Django 4.2.4 (project generated with this version)
- SQLite for local development (db.sqlite3)
- psycopg2-binary>=2.9.11 declared in pyproject.toml for optional PostgreSQL support
- python-dotenv for environment variable loading
- whitenoise for static file handling in production
- django-storages with AWS S3 settings for media file storage

## Project Structure

- animalshare/ – project configuration and settings
- blog/ – forum posts, comments, and blog views
- users/ – user profiles, authentication, and account management
- goods/ – product catalog and categories
- carts/ – shopping cart and cart utilities
- orders/ – order processing and order item management
- usertouser/ – private message model and inbox logic
- media/ – uploaded images for avatars, product catalog, and posts

## Setup and Installation

1. Clone the repository and change directory:
    `bash
    git clone https://github.com/ParanoyaFobios/animal_share
    cd firstsite
    `
2. Install dependencies and create environment:
    `bash
    uv sync
    `
3. Create or update the environment file from .env:
   - SECRET_KEY
   - EMAIL_HOST_USER
   - EMAIL_HOST_PASSWORD
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_STORAGE_BUCKET_NAME
   The project already loads environment variables from .env. For working .env file print me at 237629134pah@gmail.com

4. Apply database migrations
   `bash
   python manage.py migrate
   `

5. Create a superuser for admin access:
   `bash
   python manage.py createsuperuser
   `

6. Start the development server:
   `bash
   python manage.py runserver
   `

7. Open the site in a browser:
   `	ext
   http://127.0.0.1:8000/
   `

## Running with Docker

This project includes Docker configuration files. See README.Docker.md for Docker-specific build and deployment instructions.

## Notes

- Local development uses SQLite, while pyproject.toml includes psycopg2-binary for PostgreSQL compatibility on production or Heroku.
- The project supports image uploads for user avatars, product images, and animal post photos.
- Email password reset requires valid SMTP credentials in .env.
- Static files are configured with whitenoise, and media file storage is configured for AWS S3 if environment variables are provided.

## How to Use This Project

1. Register a new account and log in.
2. Edit your profile and upload an avatar.
3. Create an animal post with a title, description, and image.
4. Browse other users' posts and leave comments.
5. Send and receive private messages through the inbox.
6. Browse the online store, add products to your cart, and place an order.
7. Use the admin interface to manage products, categories, posts, and user accounts.
