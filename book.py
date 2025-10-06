from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    @abstractmethod
    def calculateLateFee(self, days_late):
        pass


class EBook(Book):
    def calculateLateFee(self, days_late):
        return days_late * 0.5


class PrintedBook(Book):
    def calculateLateFee(self, days_late):
        return days_late * 1.5
