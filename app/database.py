from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

engine = create_engine(
    "mysql+pymysql://root:@localhost/mens_bag_database",
    pool_pre_ping=True  # 🔥 prevents dead connections
)

# ✅ FIX: use scoped_session instead of single global session
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()