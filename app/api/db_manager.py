from app.api.models import ClubIn, ClubOut, ClubUpdate
from app.api.db import clubs, database


async def add_club(payload: ClubIn):
    query = clubs.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_club():
    query = clubs.select()
    return await database.fetch_all(query=query)
