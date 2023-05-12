from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite items included for local testing if desired, SQLALCHEMY_DATABASE_URL is for link to more robust database.

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
#'sqlite:///./<db_name>.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

## Below for SQLite only
## engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
