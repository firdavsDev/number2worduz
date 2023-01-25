from abc import ABC, abstractmethod
from functools import lru_cache

class BaseData(ABC):
    """data class for number2word_uz

    Args:
        ABC (_type_): abstract base class
    """    
    ones_uz = ('', 'bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz')
    twos_uz = ('o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson')
    tens_uz = ('yuz', 'ming', 'million', 'milyard', 'trilyon', 'kvadrilyon')

    @abstractmethod
    def number2word_uz(self, number) -> str:
        """abstract method for number2word_uz

        Returns:
            str: number2word_uz
        """        
        pass


class Number2WordUz(BaseData):
    """number2word_uz class 

    Args:
        BaseData (BaseData): BaseData class

    Returns:
        Number2WordUz: Number2WordUz class

    Usage:
        >>> number = int(input('Enter number: '))
        >>> print(Number2WordUz(number)()) # call method 

    """    
    def __init__(self, number: int) -> None:
        self.number = number

    # call method
    def __call__(self) -> str:
        return self.number2word_uz(self.number)

    @lru_cache(maxsize=128)
    def number2word_uz(self, number) -> str:
        """transform number to word

        Args:
            number (int): number

        Raises:
            e: Exception

        Returns:
            str: number2word_uz
        """        
        try:
            if number == 0:
                return self.ones_uz[0]
            if number < 10:
                return self.ones_uz[number]
            if number < 20:
                return self.twos_uz[number - 10]
            if number < 100:
                return f'{self.twos_uz[number // 10 - 1]} {self.number2word_uz(number % 10)}'
            if number < 1000:
                return f'{self.number2word_uz(number // 100)} {self.tens_uz[0]} {self.number2word_uz(number % 100)}'
            return next(
                (
                    f'{self.number2word_uz(number // 1000**i)} {self.tens_uz[i]} {self.number2word_uz(number % 1000**i)}'
                    for i in range(1, len(self.tens_uz))
                    if number < 1000 ** (i + 1)
                ),
                'Too big number',
            )
        except Exception as e:
            raise e

# Using example:
#   
# if __name__ == '__main__':
#     number = int(input('Enter number: '))
#     print(Number2WordUz(number)())

