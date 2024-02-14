from abc import ABC, abstractmethod
from typing import Dict

class GetUserInterface(ABC):

    @abstractmethod
    def query_user(self, query_param: str) -> Dict:
        pass
