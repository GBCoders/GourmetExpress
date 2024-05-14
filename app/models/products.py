from ..app import db
from sqlalchemy import ForeignKey
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = "category_products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(30), unique=True, nullable=False)

class Products(db.Model):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    description: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category_products.id"))

    user: Mapped["Category"] = relationship(back_populates="products")