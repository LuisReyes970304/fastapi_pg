from sqlmodel import select


class UserCrud:
    async def find_all(self, user, session):
            statement = select(user)
            results = session.exec(statement)
            for user in results:
                yield user
                
    async def create(self, user, session):
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user