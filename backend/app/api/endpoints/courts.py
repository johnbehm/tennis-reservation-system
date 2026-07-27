from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.court import CourtResponse
from app.services.court_service import get_all_courts

router = APIRouter(prefix="/courts", tags=["Courts"])


@router.get("", response_model=List[CourtResponse])
def list_courts(db: Session = Depends(get_db)):
    return get_all_courts(db)