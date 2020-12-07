from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import Customer, Agent

DATABASE_USER = "Jonathan"
DATABASE_PASSWORD = "Jonathan"
DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:5432/loancompany"
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

customer1 = Customer(name="tom", contact="235652154", loan_amount=2500, loan_repaid=300, prepayment=500, arrears=0, city="accra", region="ghana", location="ghana", coordinates="5.6037° N, 0.1870° W")
customer2 = Customer(name="tomas", contact="235652154", loan_amount=2500, loan_repaid=300, prepayment=500, arrears=0, city="accra", region="ghana", location="ghana", coordinates="5.6037° N, 0.1870° W")


agent1 = Agent(email="something@example.com", password="123456789")
session.add(customer1)
session.add(customer2)
session.add(agent1)


session.commit()