from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.types import String, Integer, BigInteger
from .base import Base

class Registration(Base):
    __tablename__ = 'registrations'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str] = mapped_column(BigInteger, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    drink: Mapped[str] = mapped_column(String(50), nullable=False)
    eat: Mapped[str] = mapped_column(String(50), nullable=False)