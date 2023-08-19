#!/usr/bin/python3

'''
Write a Python file similar to model_state.py
named model_city.py that contains the class definition of a City.

You must use the module SQLAlchemy

Next, write a script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa:

Your script should take 3 arguments:
mysql username, mysql password and database name

You must use the module SQLAlchemy

You must import State and Base from model_state
- from model_state import Base, State

Your script should connect to a MySQL server
running on localhost at port 3306

Results must be sorted in ascending order by cities.id

Results must be display as they are in the example below
(<state name>: (<city id>) <city name>)

Your code should not be executed when imported
'''

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
