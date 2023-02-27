import uuid
from datetime import datetime, time

from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Integer, Float, Boolean, text, Date, Time, Sequence, Identity
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, ARRAY

from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Marque(Base):
    __tablename__  = 'marques'
    id             = Column(Integer, primary_key=True, index=True, autoincrement=True)    
    marque   = Column(String(60), unique=True, nullable=False, index=True)
    description    = Column(String(255))


class Moteur(Base):
    __tablename__  = 'moteurs'
    id             = Column(Integer, primary_key=True, index=True, autoincrement=True)    
    moteur   = Column(String(60), unique=True, nullable=False, index=True)
    description    = Column(String(255))


class Category(Base):
    __tablename__  = 'categories'
    id             = Column(Integer, primary_key=True, index=True, autoincrement=True)    
    categorie   = Column(String(60), unique=True, nullable=False, index=True)
    description    = Column(String(255))

class Modele(Base):
    __tablename__  = 'modeles'
    id             = Column(Integer, primary_key=True, index=True, autoincrement=True)    
    modele   = Column(String(60), unique=True, nullable=False, index=True)
    description    = Column(String(255))
    marque_id   = Column(Integer, ForeignKey("marques.id"), index=True)
    categorie_id   = Column(Integer, ForeignKey("categories.id"), index=True)

class Vehicule(Base):
    __tablename__   = 'vehicules'
    id              = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                         default=uuid.uuid4)
    immatriculation   = Column(String(60), index=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    modele_id   = Column(Integer, ForeignKey("modeles.id"), index=True)
                        
class Kilometrage(Base):
    __tablename__   = 'kilometrages'
    id              = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                         default=uuid.uuid4)
    kilometrage   = Column(Integer)
    date_mesure   = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    vehicule_id   = Column(UUID(as_uuid=True), ForeignKey("vehicules.id"), index=True)