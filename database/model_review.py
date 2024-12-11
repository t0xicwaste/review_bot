from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.types import String, Integer
from .base import Base

class Review(Base):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    grade: Mapped[str] = mapped_column(String, nullable=False)
    guest: Mapped[str] = mapped_column(String, nullable=False)
    theme: Mapped[str] = mapped_column(String, nullable=False)
    next_theme: Mapped[str] = mapped_column(String, nullable=False)
    next_review: Mapped[str] = mapped_column(String, nullable=False)