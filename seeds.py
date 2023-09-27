# Import necessary classes and objects from models.py
from models import app, db, Pizza, Restaurant, RestaurantPizza

# Create a Flask application context
with app.app_context():
    # Create database tables if they don't exist
    db.create_all()

    # Insert data into the database
    def seed_database():
        # Create Pizza objects
        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
        pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

        # Create Restaurant objects
        restaurant1 = Restaurant(name="Pizza Hut", address="123 Main St")
        restaurant2 = Restaurant(name="Domino's", address="456 Elm St")

        # Add objects to the session
        db.session.add_all([pizza1, pizza2, restaurant1, restaurant2])
        db.session.commit()

        # Get Pizza and Restaurant objects from the database
        pizza1 = Pizza.query.filter_by(name="Margherita").first()
        pizza2 = Pizza.query.filter_by(name="Pepperoni").first()
        restaurant1 = Restaurant.query.filter_by(name="Pizza Hut").first()
        restaurant2 = Restaurant.query.filter_by(name="Domino's").first()

        # Create RestaurantPizza objects and set the relationship
        restaurant_pizza1 = RestaurantPizza(price=10.99, pizza=pizza1, restaurant=restaurant1)
        restaurant_pizza2 = RestaurantPizza(price=12.99, pizza=pizza2, restaurant=restaurant1)
        restaurant_pizza3 = RestaurantPizza(price=11.99, pizza=pizza1, restaurant=restaurant2)

        # Add RestaurantPizza objects to the session
        db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
        db.session.commit()

    if __name__ == '__main__':
        seed_database()
