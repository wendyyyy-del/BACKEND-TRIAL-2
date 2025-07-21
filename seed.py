from app import create_app, db
from models import User, Bus

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username="admin", role="admin")
    admin.set_password("admin123")

    driver = User(username="driver", role="driver")
    driver.set_password("driver123")

    customer = User(username="customer", role="customer")
    customer.set_password("customer123")

    db.session.add_all([admin, driver, customer])
    db.session.commit()

    bus = Bus(number_plate="KDA 123X", capacity=45, driver_id=driver.id)
    db.session.add(bus)
    db.session.commit()

    print("Database seeded!")
