from factories import create_UserRepository
from application.services.service import UserInfoService

def main():
    user_repository = create_UserRepository("sqlite")
    service = UserInfoService(user_repository)
    service.display_user_info(1)

if __name__ == "__main__":
    main()
