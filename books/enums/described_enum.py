import abc
from enum import Enum
from functools import cached_property


class DescribedEnum(Enum):

    @abc.abstractmethod
    @cached_property
    def descriptions(self) -> dict:
        raise NotImplementedError

    @property
    def description(self) -> str:
        return self.descriptions.get(self)
