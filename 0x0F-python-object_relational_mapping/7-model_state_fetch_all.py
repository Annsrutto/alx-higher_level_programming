#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine(f'mysql+mysqldb: // {username}: {password}
                           @localhost/{database}', pool_pre_ping=True)

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    states = session.query(State).order_by(State.id.asc()).all()
    
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
