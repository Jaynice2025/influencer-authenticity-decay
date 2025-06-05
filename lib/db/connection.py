# lib/db/connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///dev.db"  # L'URL de la base de données, ajuste si nécessaire

# Crée un moteur pour la base de données
engine = create_engine(DATABASE_URL, echo=True)

# Crée une session pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()

# Fonction pour obtenir une session locale
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
