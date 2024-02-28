# Simple tutorial for the OOP.md file.

"""If you like and have time, feel free to improve the example below, 
create a menu for it, create new classes like Blue-Ray DVD and so on,
have a good job!
"""

# DVD Rental Store Example
from typing import Optional


class DVD:
    """Represents a DVD in a rental store.

    Attributes:
        dvd_counter (int): Class variable to count the total number of DVD instances.
        Genre: A nested class representing DVD genres.
        __title (str): The title of the DVD.
        __release_year (int): The release year of the DVD.
        __genre (list[Genre]): The genres of the DVD.
        __available (bool): The availability of the DVD for rent.
    """
    dvd_counter = 0 # Counts the total DVDs created
    class Genre:
        """Nested class to define DVD genres."""
        ACTION = 'Action'
        COMEDY = 'Comedy'
        DRAMA = 'Drama'
        SCIFI = 'Science Fiction'
        THRILLER = 'Thriller'

    def __init__(self, title: str, release_year: int, genre: list[Genre]) -> None:
        """Initializes a new DVD instance."""
        self.__title = title
        self.__release_year = release_year
        self.__genre = genre
        self.__available = True
        DVD.dvd_counter += 1 # Increment the counter for each new DVD

    def get_title(self) -> str:
        """Returns the title of the DVD."""
        return self.__title
    
    def rent(self) -> bool:
        """Attempts to rent the DVD.

        Returns:
            bool: True if the DVD was successfully rented, False otherwise.
        """
        if self.__available:
            self.__available = False
            return True
        else:
            return False
        
    def return_dvd(self) -> bool:
        """Marks the DVD as available for rent again."""
        self.__available = True

    def __str__(self) -> str:
        """Returns a string representation of the DVD."""
        return f'DVD: {self.__title} ({self.__release_year}) {self.__genre}'
    

class DVDStore:
    """Represents a store that rents DVDs.

    Attributes:
        __dvds (list): A list of all DVDs in the store.
        __rented_dvds (list): A list of all currently rented DVDs.
    """

    def __init__(self) -> None:
        """Initializes a new DVDStore instance."""
        self.__dvds = []
        self.__rented_dvds = []

    def add_dvd(self, dvd: DVD) -> None:
        """Adds a DVD to the store's inventory."""
        self.__dvds.append(dvd)
          
    def get_all_dvd(self) -> list:
        """Returns a list of all DVDs in the store."""
        return self.__dvds
    
    def get_dvd(self, title: str) -> Optional[DVD]:
        """Finds a DVD by title.

        Args:
            title (str): The title of the DVD to find.

        Returns:
            DVD: The DVD with the matching title, or None if not found.
        """
        for dvd in self.__dvds:
            if dvd.get_title() == title:
                return dvd
            
    def get_all_rented_dvd(self) -> list:
        """Returns a list of all currently rented DVDs."""
        return self.__rented_dvds
    
    def get_rented_dvd(self, title: str) -> Optional[DVD]:
        """Attempts to rent a DVD.

        Args:
            dvd (DVD): The DVD to rent.
        """
        for dvd in self.__rented_dvds:
            if dvd.get_title() == title:
                return dvd
            
    def rent_dvd(self, dvd) -> None:
        """Returns a rented DVD to the store.

        Args:
            dvd (DVD): The DVD to return.
        """
        if dvd.rent():
            self.__rented_dvds.append(dvd)
            print(f"{dvd.get_title()} has been successfully rented.")
        else:
            print(f"{dvd.get_title()} is not available for rent.")

    def return_dvd(self, dvd):
        """Returns a string representation of the store's DVD inventory."""
        if dvd in self.__rented_dvds:
            self.__rented_dvds.remove(dvd)
            dvd.return_dvd()
            print(f"{dvd.get_title()} has been successfully returned.")
        else:
            print("You did not rent this DVD.")

    def __str__(self) -> str:
        dvds_str = [str(dvd) for dvd in self.__dvds]  
        return "\n".join(dvds_str)


# Example usage
if __name__ == "__main__":
    print('-- 0 --')

    dvd1 = DVD('Inception', 2010, [DVD.Genre.SCIFI, DVD.Genre.ACTION])
    print(dvd1)
    print(dvd1.__dict__)

    print('-- 1 --')

    web_store = DVDStore()
    web_store.add_dvd(dvd1)
    web_store.add_dvd(DVD('Parasite', 2019, [DVD.Genre.THRILLER, DVD.Genre.DRAMA]))
    web_store.add_dvd(DVD('Interstellar', 2014, [DVD.Genre.SCIFI, DVD.Genre.ACTION]))
    web_store.add_dvd(DVD('The Matrix', 1999, [DVD.Genre.ACTION, DVD.Genre.SCIFI]))
    web_store.add_dvd(DVD('The Matrix', 1999, [DVD.Genre.ACTION, DVD.Genre.SCIFI]))
    web_store.add_dvd(DVD('The Matrix', 1999, [DVD.Genre.ACTION, DVD.Genre.SCIFI]))
    print(web_store)

    print('-- 2 --')

    r1_dvd = web_store.get_dvd('Parasite')
    r2_dvd = web_store.get_dvd('Interstellar')
    print(r1_dvd)

    print('-- 3 --')

    web_store.rent_dvd(r1_dvd) # Parasite has been successfully rented.

    print('-- 4 --')

    web_store.rent_dvd(r1_dvd) # Parasite is not available for rent.

    print('-- 5 --')

    web_store.rent_dvd(r2_dvd)

    print('-- 6 --')

    rented_dvds = web_store.get_all_rented_dvd()
    for dvd in rented_dvds:
        print(dvd)

    print('-- 7 --')

    web_store.return_dvd(r2_dvd)

    print('-- 8 --')
    rented_dvds = web_store.get_all_rented_dvd()
    for dvd in rented_dvds:
        print(dvd)

    print('-- 9 --')

    print(DVD.dvd_counter)

    print('-- 10 --')

