from domain.repositories.user_repository import UserRepository

class UserInfoService:
    """    
    「ViewModel」的なもの
    """
    def __init__(self, user_repository: UserRepository):
        """
        Initialize the Service class.

        Args:
            user_repository (UserRepository): _description_
        """
        self.user_repository = user_repository

    def display_user_info(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")

