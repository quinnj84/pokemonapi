from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://root:KB1EQm5EVNwxwmbzamHsi86FnRGEQdVK@dpg-cfgkdq9a6gdma8h2olug-a.frankfurt-postgres.render.com/testdb1_de2z"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()