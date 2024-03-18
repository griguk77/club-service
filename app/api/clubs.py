from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import ClubOut, ClubIn, ClubUpdate
from app.api import db_manager

clubs = APIRouter()

@clubs.post('/', response_model=ClubOut, status_code=201) #localhost:8002/api/v1/clubs
async def create_club(payload: ClubIn):
    club_id = await db_manager.add_club(payload)

    response = {
        'id': club_id,
        **payload.dict()
    }

    return response


@clubs.get('/', response_model=List[ClubOut]) #localhost:8001/api/v1/footballers
async def get_clubs():
    return await db_manager.get_all_club()