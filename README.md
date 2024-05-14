# Blog API
This FastAPI-based API provides basic CRUD functionality for managing blog posts.

# Features
Create: Add new blog posts.
Read: View existing blog posts.
Update: Modify existing blog posts.
Delete: Remove blog posts.

# Setup and Installation
Clone the repository:

git clone https://github.com/deadaj1707/Blog-App.git

Navigate to the project directory:

cd Blog-App

Start the FastAPI server:

uvicorn main:app --reload
Open your web browser and go to http://localhost:8000 to access the API documentation and interact with the endpoints.

# API Endpoints
GET /: Retrieve all blog posts.
POST /: Create a new blog post.
PUT /update/{id}: Update an existing blog post.
POST /delete/{id}: Delete a blog post.
POST /like/{id}: Increment the like count of a blog post.

# Data Models
The API uses the following data model for blog posts:

{
  "id": "string",
  "title": "string",
  "desc": "string",
  "important": "boolean",
  "likes": "integer"
}

# Usage
Creating a Blog Post: Send a POST request to / with the title, desc, and optional important fields in the request body.

Updating a Blog Post: Send a PUT request to /update/{id} with the title, desc, and important fields in the request body.

Deleting a Blog Post: Send a POST request to /delete/{id} to delete a blog post by its ID.

Liking a Blog Post: Send a POST request to /like/{id} to increment the like count of a blog post by its ID.

# Additional Notes
Ensure that MongoDB is running locally or update the database connection settings in config/db.py.
The API utilizes Jinja2 templates for server-side rendering of HTML pages. HTML templates are located in the templates directory.
