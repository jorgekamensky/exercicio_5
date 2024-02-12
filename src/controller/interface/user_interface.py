from abc import ABC, abstractmethod
from typing import Dict

class UserInterface(ABC):

    @abstractmethod
    def user_input(self, user_input: Dict) -> Dict:
        pass
