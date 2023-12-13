import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


alex = User(
    full_name='Alex Davydov',
    email='AlexDavydov92@gmail.com',
    current_address='South Street',
    permanent_address='South Street',
)
