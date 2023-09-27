# Restaurant and Pizza Management API

This is a Flask-based API for managing restaurants and their associated pizzas. The API allows you to perform various operations including creating new restaurant-pizza relationships, retrieving restaurant details, deleting restaurants, and more.
### AUTHOR
IAN NJAGAH NDUNG'U 
## Getting Started

### Prerequisites

Before running this application, ensure you have the following installed:

- Python (3.x)
- Flask
- Flask-Migrate
- SQLAlchemy

### Installing Dependencies

Install the required dependencies using pip:

pip install Flask Flask-Migrate SQLAlchemy


### Running the Application
Ensure you are in the project directory.
Create the database and apply migrations:
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

### Start the application:
 /home/njagah/Phase-4-week1-challenge/myenv/bin/python /home/njagah/Phase-4-week1-challenge/main.py
 The API will be running at http://localhost:5555

 ### Endpoints
GET /restaurants
Description: Retrieve a list of all restaurants.

Response:

Status Code: 200 OK


GET /restaurants/<restaurant_id>
Description: Retrieve details of a specific restaurant.

Parameters:

restaurant_id: ID of the restaurant.
Response:

Status Code: 200 OK


DELETE /restaurants/<restaurant_id>
Description: Delete a restaurant and its associated pizzas.

Parameters:

restaurant_id: ID of the restaurant.
Response:

Status Code: 204 No Content
POST /restaurants_pizzas/create
Description: Create a new restaurant-pizza relationship.

Request:


Response:

Status Code: 201 Created

## Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Make your changes and commit them (git commit -m 'Add new feature')
Push to the branch (git push origin feature/your-feature)
Create a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.


