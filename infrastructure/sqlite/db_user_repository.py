from domain.repositories.user_repository import UserRepository
class DbUserRepository(UserRepository):
    """
    DbUserRepository is a concrete implementation of the UserRepository interface.

    Args:
        UserRepository (_type_): _description_
    """
    def get_user_by_id(self, user_id: int):
        pass
