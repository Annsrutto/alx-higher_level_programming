#!/usr/bin/python3
"""A script that lists all State objects
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1],
    sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb: // {username}: {password}
                           @localhost/{database}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()
