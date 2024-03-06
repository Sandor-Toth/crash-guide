import OOP_data
import random
import re
from abc import ABC, abstractmethod
from datetime import datetime

"""
This is just a small example of the use of some elements of OOP.
If you feel like it, feel free to extend, improve or change the code!
"""

# Abstract base class for systems
class System(ABC):
    # Nested classes to define constants for system attributes
    class ResponseTime:
        HIGH = 'HIGH'
        MEDIUM = 'MEDIUM'
        LOW = 'LOW'

    class ServerStability:
        BAD = 'BAD'
        GOOD = 'GOOD'
        VERY_GOOD = 'VERY GOOD'

    class ServerSafety:
        TRUSTY = 'TRUSTY'
        UNTRUSTY = 'UNTRUSTY'

    # Constructor initializes the system metrics using private methods
    def __init__(self):
        self.__response_time = self.__response_time_calculator()
        self.__server_stability = self.__stability_calculator()
        self.__server_safety = self.__safety_calculator()

    # Private method to calculate response time
    def __response_time_calculator(self):
        random_number = random.randint(1, 250)
        if random_number <= 50:
            return self.ResponseTime.LOW
        elif random_number <= 150:
            return self.ResponseTime.MEDIUM
        else:
            return self.ResponseTime.HIGH
        
    # Private method to randomly select server stability
    def __stability_calculator(self):
        stability_options = [
            self.ServerStability.BAD,
            self.ServerStability.GOOD,
            self.ServerStability.VERY_GOOD
        ]
        return random.choice(stability_options)
    
    # Private method to randomly select server safety
    def __safety_calculator(self):
        safety_options = [self.ServerSafety.TRUSTY, self.ServerSafety.UNTRUSTY]
        return random.choice(safety_options)
    
    # Abstract method to be implemented by subclasses to display server status
    @abstractmethod
    def server_status(self):
        return (
            f'Server status:\n'
            f'- Server response time: {self.__response_time}\n'
            f'- Server stability: {self.__server_stability}\n'
            f'- Server safety: {self.__server_safety}\n'
        )

# ServiceProvider class inherits from System
class ServiceProvider(System):
    # Nested class to define constants for maximum quality
    class MaximumQuality:
        UHD = 'UHD'
        FHD = 'FHD'
        HD = 'HD'

    # Nested class to define constants for device compatibility
    class DeviceCompatibility:
        PHONE = 'Phone'
        TAB = 'Tablet'
        PC = 'PC'
        TV = 'TV'

    # Constructor initializes service provider attributes and calls the base class constructor
    def __init__(
            self, 
            name: str, 
            quality: MaximumQuality, 
            compatibility: list[DeviceCompatibility],
            fee:  int,
            offline_mode: bool):
        super().__init__()
        self._name = name
        self._quality = quality
        self._compatibility = compatibility
        self._subscription_fee = fee
        self._offline_mode = offline_mode

    # Method to display server status, utilizing the base class implementation
    def server_status(self):
        return super().server_status()
    
    # Static method to promote the service provider
    @staticmethod
    def promotion(provider):
        print(f'Look at us! Now free for a week! --- {provider} ---')
    
# Abstract base class for Media
class Media(ABC):
    def __init__(self, **kwargs) -> None:
        self._title: str = kwargs['title']
        self._genres: list[str] = kwargs['genres']
        self._release_date: datetime = kwargs['release_date']

    # Abstract method for advertising, to be implemented by subclasses
    @abstractmethod
    def advertising(self):
        pass

    # Static method to format a list of content for display
    @staticmethod
    def format_list(content_list):
        formatted_list = [str(elem) for elem in content_list]
        return formatted_list

# AudioWork class inherits from Media
class AudioWork(Media):
    # Constructor initializes audio work specific attributes and calls the base class constructor
    def __init__(self, performer, **kwargs) -> None:
        super().__init__(**kwargs)
        self._performer: str = performer

    # Class method to create an instance from a string representation
    @classmethod
    def from_string(cls, audio_str):
        # Regular expression parsing to extract data from string
        title_match = re.search(r"Music: (.*?);", audio_str)
        genres_match = re.search(r"Genre: (.*?);", audio_str)
        date_match = re.search(r"Date: (\d{4}) (\d{1,2}) (\d{1,2})", audio_str)
        performer_match = re.search(r"- (.*)$", audio_str)
        # Extracting data using the matches and creating an instance
        title = title_match.group(1) if title_match else None
        genres = genres_match.group(1).split(', ') if genres_match else None
        release_date = datetime.strptime(
            ' '.join(date_match.groups()), '%Y %m %d') if date_match else None
        performer = performer_match.group(1) if performer_match else None
        return cls(title=title, genres=genres, 
                   release_date=release_date, performer=performer)
    
    # Implementation of advertising method for audio works
    def advertising(self):
        print(f"If you love great music then you need to hear {self._title} "
              f"by {self._performer}!")
    
    # String representation of the audio work
    def __str__(self) -> str:
        return (f"Song's title: {self._title}; Genre: {self._genres}; " 
                f"{self._performer} ({self._release_date.strftime('%Y')})")

# AudioVisualWork class inherits from Media
class AudioVisualWork(Media):
    def __init__(self, type, imdb_rating, **kwargs) -> None:
        super().__init__(**kwargs)
        self._type: str= type
        self._imdb_rating: float = imdb_rating

    # Class method to create an instance from a string representation
    @classmethod
    def from_string(cls, movie_str, type, imdb_rating):
        # Regular expression parsing to extract data from string
        title_match = re.search(r"Title: (.*?);", movie_str)
        genres_match = re.search(r"Genre\(s\): (.*?);", movie_str)
        date_match = re.search(r"Date: (\d{4} \d{1,2} \d{1,2})", movie_str)

        title = title_match.group(1) if title_match else None
        genres = genres_match.group(1).split(', ') if genres_match else None
        release_date = datetime.strptime(
            ' '.join(date_match.groups()), '%Y %m %d') if date_match else None
        return cls(title=title, genres=genres, release_date=release_date,
                   type=type, imdb_rating=imdb_rating)

    # Implementation of advertising method for audiovisual works
    def advertising(self):
        print(f"Are you ready for a great movie or series? Look at the {self._title}!")

    # String representation of the audiovisual work
    def __str__(self) -> str:
        return (f"Title: {self._title}; Genre(s){self._genres}; " 
                f"Release date: ({self._release_date.strftime('%B %d %Y')})")

# StreamingService class inherits from ServiceProvider
class StreamingService(ServiceProvider):
    # Constructor initializes streaming service specific attributes and calls the base class constructor
    def __init__(self, name, quality, compatibility, fee, 
            offline_mode, contents: dict):
        super().__init__(name, quality, compatibility, fee, offline_mode)
        self._contents = contents

    # Property to get the provider name
    @property
    def provider_name(self):
        return self._name
    
    # Property to get the provider contents
    @property
    def provider_contents(self):
        return self._contents
    

# Utility function to process data and create media content instances
def process_data(data, work_type=None):
    content_list = []
    for elem in data:
        if work_type == 'AudioWork':
            content_list.append(AudioWork.from_string(elem[0]))
        else:
            content_list.append(
                AudioVisualWork.from_string(elem[0], work_type, elem[1]))
    return content_list


content = {}
content['Musics'] = process_data(OOP_data.musics, 'AudioWork')
content['Movies'] = process_data(OOP_data.movies, 'Movie')
content['Series'] = process_data(OOP_data.series, 'Series')

# Main function to create streaming service instances based on external data
def create_streaming_service():
    streaming_services = []
    services = OOP_data.data_processing()
    for elem in services:
        device_list = [
            getattr(ServiceProvider.DeviceCompatibility, item) 
            for item in elem[2]['device_list']
        ]
        streaming_services.append(
            StreamingService(
                elem[0]['name'], 
                elem[1]['quality'],
                device_list,
                elem[3]['fee'],
                elem[4]['offline_mode'],
                content
            )
        )
    return streaming_services

# Create streaming service instances and demonstrate their functionality
streaming_services = create_streaming_service()
for elem in streaming_services:
    print(f"{elem.provider_name} - {elem.server_status()}")
    print('--- Musics ---')
    print(Media.format_list(elem.provider_contents['Musics']))
    print('--- Movies ---')
    print(Media.format_list(elem.provider_contents['Movies']))
    break

# Demonstrating the selection and advertisement of random provider and media content
print('--- Select random provider ---')
random_provider_num = random.randint(0, 4)
randim_item_num = random.randint(0, 9)
print(f"{streaming_services[random_provider_num].provider_name}")
print(streaming_services[random_provider_num].provider_contents['Musics'][randim_item_num])
streaming_services[random_provider_num].provider_contents['Musics'][randim_item_num].advertising()
print(streaming_services[random_provider_num].provider_contents['Movies'][randim_item_num])
streaming_services[random_provider_num].provider_contents['Movies'][randim_item_num].advertising()
print(streaming_services[random_provider_num].provider_contents['Series'][randim_item_num])
streaming_services[random_provider_num].provider_contents['Series'][randim_item_num].advertising()
ServiceProvider.promotion(streaming_services[random_provider_num].provider_name)

