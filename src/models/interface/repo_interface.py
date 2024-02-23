from abc import ABC, abstractmethod

class RepoInterface(ABC):

    @abstractmethod
    def post_user(self, user: any):
        pass

    @abstractmethod
    def get_user(self, query_param: str):
        pass

    @abstractmethod
    def delete_user(self):
        pass