from enum import Enum, auto


class Providers(Enum):
    TWITCH = auto()
    GITHUB = auto()


class Roles(Enum):
    ADMIN = auto()
    USER = auto()


class Categories(Enum):
    ARTS_AND_CULTURE = auto()
    BUSINESS = auto()
    COMEDY = auto()
    EDUCATION = auto()
    FICTION = auto()
    HEALTH_AND_FITNESS = auto()
    KIDS_AND_FAMILY = auto()
    LEISURE = auto()
    NEWS_AND_POLITICS = auto()
    RELIGION = auto()
    SCIENCE = auto()
    SOCIETY = auto()
    SPORTS = auto()
    CRIME = auto()
    TV_AND_FILM = auto()


class Shared(Enum):
    MODERATOR = auto()
    CONSUMERS = auto()


def role_check(role: str):
    if role == "ADMIN":
        return Roles.ADMIN
    elif role == "USER":
        return Roles.USER


def provider_check(provider: str):
    if provider == 'GITHUB':
        return Providers.GITHUB
    elif provider == 'TWITCH':
        return Providers.TWITCH


class FakeClient:
    def __init__(self, user_id):
        self.id = user_id
        self.username = 'Jerry George'
        self.is_authenticated = True
