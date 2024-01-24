from sqlalchemy import Column, DateTime, Text
# from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base
from datetime import datetime


class BudgetTracking(Base):
    __tablename__ = "budget_tracking"

    BudgetID = Column(Integer, primary_key=True, index=True)
    BudgetName = Column(String, index=True, nullable=False)
    BudgetAmount = Column(Integer, nullable=False)
    Expenditure = Column(Integer, nullable=False)
    TransactionDate = Column(DateTime, default=datetime.utcnow)
    Note = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'),
                        index=True
                        )
    created_by = Column(String,
                        nullable=False,
                        default=text("'admin'"),
                        index=True
                        )
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True,
                        index=True
                        )
    updated_by = Column(String, nullable=True, index=True)


class RevenueCollection(Base):
    __tablename__ = "revenue_collection"

    RevenueID = Column(Integer, primary_key=True, index=True)
    SourceName = Column(String, index=True, nullable=False)
    CollectionAmount = Column(Integer, nullable=False)
    CollectionDate = Column(DateTime, default=datetime.utcnow)
    Note = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'),
                        index=True
                        )
    created_by = Column(String,
                        nullable=False,
                        default=text("'admin'"),
                        index=True
                        )
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True,
                        index=True
                        )
    updated_by = Column(String, nullable=True, index=True)
