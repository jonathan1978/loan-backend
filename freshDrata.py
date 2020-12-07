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

customer1 = Customer(name="Tom", contact="2332770334", loan_amount=2500, loan_repaid=300, prepayment=0, arrears=100, city="Accra", region="Greater Accra", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer2 = Customer(name="Roxanne", contact="233548705628", loan_amount=2500, loan_repaid=300, prepayment=500, arrears=0, city="Tema", region="Greater Accra", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer3 = Customer(name="Joe", contact="233242770336", loan_amount=3000, loan_repaid=3000, prepayment=0, arrears=0, city="Sekondi-Takoradi", region="Western Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer4 = Customer(name="Fred", contact="233242770331", loan_amount=3000, loan_repaid=3000, prepayment=0, arrears=0, city="Sekondi-Takoradi", region="Western Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer5 = Customer(name="Cecilia", contact="233242770332", loan_amount=5000, loan_repaid=3000, prepayment=700, arrears=0, city="Sekondi-Takoradi", region="Western Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer6 = Customer(name="Joseph", contact="2332427703212", loan_amount=6000, loan_repaid=3000, prepayment=0, arrears=100, city="Tamale", region="Northern Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer7 = Customer(name="Romanus", contact="233241270332", loan_amount=7000, loan_repaid=3000, prepayment=583.33, arrears=0, city="Ho", region="Volta Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer8 = Customer(name="Richard", contact="233242550332", loan_amount=4000, loan_repaid=3000, prepayment=333.33, arrears=0, city="Cape Coast", region="Central Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer9 = Customer(name="Francis", contact="233242770332", loan_amount=9000, loan_repaid=3000, prepayment=0, arrears=750, city="Kumasi", region="Ashanti Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer10 = Customer(name="Peter", contact="233242000332", loan_amount=3500, loan_repaid=3000, prepayment=500, arrears=0, city="Kumasi", region="Ashanti Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer11 = Customer(name="Jonathan", contact="233242110332", loan_amount=7500, loan_repaid=3000, prepayment=0, arrears=0, city="Koforidua", region="Eastern Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer12 = Customer(name="Paul", contact="233242770332", loan_amount=6000, loan_repaid=3000, prepayment=500, arrears=0, city="Koforidua", region="Eastern Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer13 = Customer(name="Francisca", contact="233242770122", loan_amount=8500, loan_repaid=3000, prepayment=1416.67, arrears=0, city="Accra", region="Greater Accra", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer14 = Customer(name="Emelia", contact="233242771132", loan_amount=9500, loan_repaid=3000, prepayment=0, arrears=1583.33, city="Tema", region="Greater Accra", location="Ghana", coordinates="5.6037° N, 0.1870° W")
customer15 = Customer(name="Amanda", contact="233242222332", loan_amount=5500, loan_repaid=3000, prepayment=0, arrears=458.33, city="Bolgatanga", region="Upper West Region", location="Ghana", coordinates="5.6037° N, 0.1870° W")

agent1 = Agent(email="something@example.com", password="123456789")
session.add(customer1)
session.add(customer2)
session.add(customer3)
session.add(customer4)
session.add(customer5)
session.add(customer6)
session.add(customer7)
session.add(customer8)
session.add(customer9)
session.add(customer10)
session.add(customer11)
session.add(customer12)
session.add(customer13)
session.add(customer14)
session.add(customer15)
session.add(agent1)


session.commit()