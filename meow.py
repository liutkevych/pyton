def meow(n: int) -> str:
    """ 
    Moew n times. 

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of meows, one per line
    :rtype: str
    """
    return "meow\n" * 3

number: int = input("Number: ")
meows: str = meow(number)
print(meows)