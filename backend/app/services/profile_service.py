from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.profile import UserProfile
from app.schemas.profile import ProfileCreate, ProfileUpdate


class ProfileService:
    @staticmethod
    async def get_by_user_id(db: AsyncSession, user_id: int) -> Optional[UserProfile]:
        result = await db.execute(select(UserProfile).where(UserProfile.user_id == user_id))
        return result.scalars().first()

    @staticmethod
    async def create_or_update(db: AsyncSession, user_id: int, profile_in: ProfileCreate) -> UserProfile:
        profile = await ProfileService.get_by_user_id(db, user_id)
        if not profile:
            profile = UserProfile(user_id=user_id, **profile_in.dict())
            db.add(profile)
        else:
            for field, value in profile_in.dict(exclude_unset=True).items():
                setattr(profile, field, value)
        await db.commit()
        await db.refresh(profile)
        return profile


profile_service = ProfileService()
