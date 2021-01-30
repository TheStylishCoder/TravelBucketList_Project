import pdb 
from models.country import Country 
from models.city import City 
from models.attraction import Attraction
from models.review import Review 

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository

country_repository.delete_all()
city_repository.delete_all()
attraction_repository.delete_all()

country1 = Country("Japan", True, True)
country_repository.save(country1)
country2 = Country("United States of America")
country_repository.save(country2)
country3 = Country("Australia")
country_repository.save(country3)
country4 = Country("Spain")
country_repository.save(country4)
country5 = Country("United Kingdom")
country_repository.save(country5)

# res = country_repository.select_all()
# for country in res:
#     print(country.__dict__)

# country1.visited = False
# country_repository.update(country1)

city1 = City("Tokyo",country1)
city_repository.save(city1)
city2 = City("Kyoto", country1)
city_repository.save(city2)

city3 = City("San Francisco", country2)
city_repository.save(city3)
city4 = City("New Orleans", country2)
city_repository.save(city4)
city5 = City("Boston", country2)
city_repository.save(city5)

city6 = City("Sydney", country3)
city_repository.save(city6)

city7 = City("Madrid", country4)
city_repository.save(city7)
city8 = City("Barcelona", country4)
city_repository.save(city8)

city9 = City("London", country5)
city_repository.save(city9)
city10 = City("Glasgow", country5)
city_repository.save(city10)

# res = city_repository.select_all()
# for city in res:
#     print(city.__dict__)

# city10.name = "Edinburgh"
# city_repository.update(city10)

attraction1 = Attraction("Sensoji Temple", "Place of Worship", city1)
attraction_repository.save(attraction1)
attraction2 = Attraction("Imperial Palace", "Historic Sight", city1)
attraction_repository.save(attraction2)
attraction3 = Attraction("Ghibli Museum", "Museum", city1, True)
attraction_repository.save(attraction3)

attraction4 = Attraction("Nishiki Market", "Food Market", city2)
attraction_repository.save(attraction4)
attraction5 = Attraction("Nijo Castle", "Historic Sight", city2, True)
attraction_repository.save(attraction5)

attraction6 = Attraction("Museum of Modern Art", "Museum", city3)
attraction_repository.save(attraction6)

attraction7 = Attraction("Botanical Gardens", "Parks & Nature", city4, True)
attraction_repository.save(attraction7)
attraction8 = Attraction("St.Louis Cathedral", "Place of Worship", city4)
attraction_repository.save(attraction8)

attraction9 = Attraction("Fenway Park", "Sports", city5, True)
attraction_repository.save(attraction9)

attraction10 = Attraction("Bondi Beach", "Beach", city6)
attraction_repository.save(attraction10)
attraction11 = Attraction("Taronga Zoo", "Zoo", city6)
attraction_repository.save(attraction11)

attraction12 = Attraction("El Retiro Park", "Parks & Nature", city7)
attraction_repository.save(attraction12)
attraction13 = Attraction("Royal Palace", "Historical Sight", city7, True)
attraction_repository.save(attraction13)
attraction14 = Attraction("Gran Via", "Food & Shopping", city7)
attraction_repository.save(attraction14)

attraction15 = Attraction("Camp Nou", "Sports", city8)
attraction_repository.save(attraction15)

attraction16 = Attraction("Buckingham Palace", "Historical Sight", city9, True)
attraction_repository.save(attraction16)
attraction17 = Attraction("Spitalfields Market", "Market", city9)
attraction_repository.save(attraction17)
attraction18 = Attraction("British Museum", "Museum", city9)
attraction_repository.save(attraction18)

attraction19 = Attraction("Kelvingrove Museum", "Museum", city10)
attraction_repository.save(attraction19)
attraction20 = Attraction("Glasgow Cathedral", "Place of Worship", city10)
attraction_repository.save(attraction20)




pdb.set_trace()

