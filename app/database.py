import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
DATABASE_PATH = Path(os.environ.get("DATABASE_PATH", PROJECT_DIR / "database.db"))

engine = create_engine(
    "sqlite:///" + str(DATABASE_PATH),
    connect_args={"check_same_thread": False}
)

Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
