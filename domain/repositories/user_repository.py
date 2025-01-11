from abc import ABCMeta, abstractmethod

class UserRepository(metaclass=ABCMeta):
    """
    UserRepository is an abstract class that defines the interface for the user repository.

    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

