from abc import ABC, abstractmethod
from typing import Dict

class UserInterface(ABC):

    @abstractmethod
    def save_user(self, user_input: Dict) -> Dict:
        pass
