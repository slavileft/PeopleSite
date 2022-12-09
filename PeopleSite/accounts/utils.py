from enum import Enum


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_value(cls):
        return max(len(name) for name, value in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    do_not_show = 'Do not show'


class EyesColor(ChoicesEnumMixin, Enum):
    black = 'Black'
    brown = 'Brown'
    blue = 'Blue'
    green = 'Green'
    hazel = 'Hazel'
    amber = 'Amber'
    grey = 'Grey'


class HairColor(ChoicesEnumMixin, Enum):
    black = 'Black'
    brown = 'Brown'
    red = 'Red'
    blond = 'Blond'
    grey = 'Grey'
    white = 'White'