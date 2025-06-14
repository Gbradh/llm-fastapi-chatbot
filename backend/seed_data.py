from sqlalchemy.orm import Session
from database import SessionLocal, create_tables
from models import Customer

def seed():
    create_tables()
    db: Session = SessionLocal()

    if db.query(Customer).count() == 0:
        customers = [
            Customer(name="Aisha Sharma", gender="female", location="Mumbai"),
            Customer(name="Ravi Kumar", gender="male", location="Delhi"),
            Customer(name="Neha Singh", gender="female", location="Mumbai"),
            Customer(name="Aman Gupta", gender="male", location="Pune"),
            Customer(name="Priya Mehra", gender="female", location="Chennai"),
        ]
        db.add_all(customers)
        db.commit()
    db.close()

if __name__ == "__main__":
    seed()
