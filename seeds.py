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
        restaurant1 = Restaurant(id=1 ,name="Pizza Hut", address="123 Main St")
        
        restaurant2 = Restaurant(id=2 ,name="Domino's", address="456 Elm St")

        # Add objects to the session
        db.session.add_all([restaurant1, restaurant2])
        db.session.commit()

        
        # Create RestaurantPizza objects and set the relationship
        print('error')
        restaurant_pizza1 = RestaurantPizza(id=1 ,price=10.99, pizza_id=1, restaurant_id=1)
        print('error1')
        restaurant_pizza2 = RestaurantPizza(id=2 ,price=12.99, pizza_id=1, restaurant_id=1)
        restaurant_pizza3 = RestaurantPizza(id=3, price=11.99, pizza_id=2, restaurant_id=2)

        # Add RestaurantPizza objects to the session
        db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
        db.session.commit()

    if __name__ == '__main__':
        seed_database()
