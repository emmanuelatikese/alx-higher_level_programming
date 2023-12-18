#!/usr/bin/python3
''' This is the begining of orm'''

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(City).order_by(City.id).all()
    for ct in st:
        name = session.query(State).filter_by(id=ct.state_id).one_or_none()
        print("{}: ({}) {}".format(name.name, ct.id, ct.name))
    session.close()
