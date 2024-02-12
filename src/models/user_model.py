import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    second_name: str
    full_name: str = dataclasses.field(init=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.second_name}"