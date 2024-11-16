from functools import cached_property

from books.enums.described_enum import DescribedEnum


class BookGenre(DescribedEnum):

    SCI_FI = 'Sci-fi'
    FANTASY = 'fantasy'
    DETECTIVE = 'detective'
    COMEDY = 'comedy'
    DRAMA = 'drama'

    @cached_property
    def descriptions(self) -> dict:
        return {
            self.SCI_FI: 'Научная фантастика',
            self.FANTASY: 'Фэнтези',
            self.DETECTIVE: 'Детектив',
            self.COMEDY: 'Комедия',
            self.DRAMA: 'Драма'
        }
