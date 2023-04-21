from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_name = "site"
SQLALCHEMY_DATABASE_URL = "sqlite:///" + db_name + ".db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


