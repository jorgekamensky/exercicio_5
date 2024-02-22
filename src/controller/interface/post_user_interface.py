from abc import ABC, abstractmethod
from typing import Dict

class PostUserInterface(ABC):

    @abstractmethod
    def insert_user(self, user_input: Dict) -> Dict:
        pass
