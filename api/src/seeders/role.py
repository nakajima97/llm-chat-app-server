from sqlalchemy.ext.asyncio import AsyncSession
from src.models.role import Role
from src.db import db_session
from src.constants import ChatRoleId


async def seed_roles(db: AsyncSession):
    roles = [
        {"id": ChatRoleId.ASSISTANT, "name": "assistant"},
        {"id": ChatRoleId.USER, "name": "user"},
    ]

    for role in roles:
        new_role = Role(id=role["id"], name=role["name"])
        db.add(new_role)

    await db.commit()


if __name__ == "__main__":
    import asyncio

    async def main():
        async with db_session() as session:
            await seed_roles(session)

    asyncio.run(main())
