from infrastructure.sqlite.db_user_repository import DbUserRepository
from infrastructure.api.api_user_repository import ApiUserRepository
from domain.repositories.user_repository import UserRepository
def create_UserRepository(user_repository: UserRepository):
    """
    create_UserRepository is a function that creates a UserRepository instance.
    
    Args:
        user_repository (UserRepository): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if user_repository == "sqlite":
        return DbUserRepository()
    elif user_repository == "api":
        return ApiUserRepository()
    else:
        raise ValueError(f"Invalid user repository: {user_repository}")
