provider = [
    'GalacticHost;FHD;TAB,TV,PC;99.99;False',
    'WizardTV;FHD;PHONE,PC;45.99;False',
    'QuantumCloud+;HD;PHONE,PC;52.99;True',
    'PixelUniverse;UHD;TV,PC;29.99;False',
    'DreamWeaver+;HD;PHONE;69.99;True'
]

movies = [
    ["Title: Inception; Genre(s): Action, Science Fiction; Date: 2010 7 16", 8.8],  
    ["Title: The Godfather; Genre(s): Crime, Drama; Date: 1972 3 24", 9.2],  
    ["Title: Forrest Gump; Genre(s): Drama, Romance; Date: 1994 7 6", 8.8],  
    ["Title: Interstellar; Genre(s): Adventure, Drama, Science Fiction; Date: 2014 11 7", 8.6],  
    ["Title: The Dark Knight; Genre(s): Action, Crime, Drama; Date: 2008 7 18", 9.0],  
    ["Title: Pulp Fiction; Genre(s): Crime, Drama; Date: 1994 10 14", 8.9],  
    ["Title: Fight Club; Genre(s): Drama; Date: 1999 10 15", 8.8],  
    ["Title: Spirited Away; Genre(s): Animation, Fantasy; Date: 2001 7 20", 8.6],  
    ["Title: La La Land; Genre(s): Drama, Music, Romance; Date: 2016 12 9", 8.0],  
    ["Title: Parasite; Genre(s): Comedy, Drama, Thriller; Date: 2019 5 30", 8.6],  
]


series = [
    ["Title: Breaking Bad; Genre(s): Crime, Drama, Thriller; Date: 2008 1 20", 9.5],  
    ["Title: Game of Thrones; Genre(s): Action, Adventure, Drama; Date: 2011 4 17", 9.3],  
    ["Title: Stranger Things; Genre(s): Drama, Fantasy, Horror; Date: 2016 7 15", 8.7],  
    ["Title: The Crown; Genre(s): Drama, History; Date: 2016 11 4", 8.7],  
    ["Title: Black Mirror; Genre(s): Drama, Science Fiction, Thriller; Date: 2011 12 4", 8.8],  
    ["Title: The Mandalorian; Genre(s): Action, Adventure, Fantasy; Date: 2019 11 12", 8.8],  
    ["Title: The Witcher; Genre(s): Action, Adventure, Fantasy; Date: 2019 12 20", 8.2],  
    ["Title: The Office; Genre(s): Comedy, Sitcom; Date: 2005 3 24", 8.9],  
    ["Title: Friends; Genre(s): Comedy, Romance; Date: 1994 9 22", 8.9],  
    ["Title: Sherlock; Genre(s): Crime, Drama, Mystery; Date: 2010 7 25", 9.1],  
]

musics = [
    ["Music: Rolling in the Deep; Genre: Pop; Date: 2010 3 10 - Adele"],
    ["Music: Shape of You; Genre: Pop; Date: 2017 6 4 - Ed Sheeran"],
    ["Music: Uptown Funk; Genre: Funk/Pop; Date: 2014 7 21 - Mark Ronson ft. Bruno Mars"],
    ["Music: Old Town Road; Genre: Country/Rap; Date: 2019 8 15 - Lil Nas X"],
    ["Music: Thrift Shop; Genre: Hip Hop; Date: 2012 3 14 - Macklemore & Ryan Lewis"],
    ["Music: Happy; Genre: Pop; Date: 2013 9 11 - Pharrell Williams"],
    ["Music: Someone Like You; Genre: Pop; Date: 2011 5 5 - Adele"],
    ["Music: Royals; Genre: Pop; Date: 2013 7 3 - Lorde"],
    ["Music: Blinding Lights; Genre: Synth-pop; Date: 2019 9 9 - The Weeknd"],
    ["Music: Get Lucky; Genre: Disco; Date: 2013 2 22 - Daft Punk ft. Pharrell Williams & Nile Rodgers"],
]


def data_processing() -> list[dict]:
    services = []
    for line in provider:
        services.append([
            {'name': line.split(';')[0].strip()},
            {'quality': line.split(';')[1].strip()},
            {'device_list': line.split(';')[2].strip().split(',')},
            {'fee': line.split(';')[3].strip()},
            {'offline_mode': line.split(';')[4].strip()},
        ])
    return services
