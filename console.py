import pdb 
from models.country import Country 
from models.city import City 
from models.attraction import Attraction
from models.review import Review 

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()

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

city10.name = "Edinburgh"
city_repository.update(city10)

pdb.set_trace()

