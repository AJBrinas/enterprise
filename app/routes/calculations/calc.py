from fastapi import HTTPException, status
from sqlalchemy import func
from ...config.database import db_dependency
from ...models.s_health import HealthInformation as hi


def persons_gender(db: db_dependency):
    gender = db.query(hi.gender,
                                 func.count(hi.gender).label('total')
                                 ).group_by(hi.gender).all()
    label = gender.gender
    total = gender.total
    return label, total
    # return HTTPException(status_code=status.HTTP_200_OK)
