import pdb 
from models.country import Country 
from models.city import City 
from models.attraction import Attraction
from models.review import Review 

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository
import repositories.review_repository as review_repository

country_repository.delete_all()
city_repository.delete_all()
attraction_repository.delete_all()
review_repository.delete_all()

country1 = Country("Japan", False, True)
country_repository.save(country1)
country2 = Country("United States of America", True, True)
country_repository.save(country2)
country3 = Country("Australia")
country_repository.save(country3)
country4 = Country("Spain", True, True)
country_repository.save(country4)
country5 = Country("United Kingdom", True)
country_repository.save(country5)
country6 = Country("Netherlands", True, True)
country_repository.save(country6)
country7 = Country("Greece", True, True)
country_repository.save(country7)
country8 = Country("Italy", True, True)
country_repository.save(country8)
country9 = Country("Switzerland", False, True)
country_repository.save(country9)
country10 = Country("New Zealand", False, True)
country_repository.save(country10)
country11 = Country("Thailand")
country_repository.save(country11)
country12 = Country("Egypt", False, True)
country_repository.save(country12)
country13= Country("Canada", False, True)
country_repository.save(country13)
country14 = Country("India", False, True)
country_repository.save(country14)

# res = country_repository.select_all()
# for country in res:
#     print(country.__dict__)

# country1.visited = False
# country_repository.update(country1)

city1 = City("Tokyo",country1, False, True)
city_repository.save(city1)
city2 = City("Kyoto", country1, False, True)
city_repository.save(city2)

city3 = City("San Francisco", country2)
city_repository.save(city3)
city4 = City("New Orleans", country2)
city_repository.save(city4)
city5 = City("Boston", country2)
city_repository.save(city5)

city6 = City("Sydney", country3)
city_repository.save(city6)

city7 = City("Madrid", country4, True, True)
city_repository.save(city7)
city8 = City("Barcelona", country4, True, True)
city_repository.save(city8)

city9 = City("London", country5)
city_repository.save(city9)
city10 = City("Glasgow", country5)
city_repository.save(city10)

city11 = City("Amsterdam", country6, True, True)
city_repository.save(city11)
city12 = City("Rotterdam", country6)
city_repository.save(city12)

city13 = City("Athens", country7, False, True)
city_repository.save(city13)
city14 = City("Chania, Crete", country7, True, True)
city_repository.save(city14)

city15 = City("Rome", country8, True, True)
city_repository.save(city15)
city16 = City("Venice", country8, True, True)
city_repository.save(city16)

city17 = City("Zurich", country9, False, True)
city_repository.save(city17)

city18 = City("Wellington", country10)
city_repository.save(city18)
city19 = City("Queenstown", country10)
city_repository.save(city19)

city20 = City("Honolulu", country2, False, True)
city_repository.save(city20)

city21 = City("Bangok", country11)
city_repository.save(city21)

city22 = City("Cairo", country12, False, True)
city_repository.save(city22)
city23 = City("Alexandria", country12)
city_repository.save(city23)

city24= City("Toronto", country13)
city_repository.save(city24)

city25 = City("Mumbai", country14)
city_repository.save(city25)

# res = city_repository.select_all()
# for city in res:
#     print(city.__dict__)

# city10.name = "Edinburgh"
# city_repository.update(city10)

attraction1 = Attraction("Sensoji Temple", "Place of Worship", city1)
attraction_repository.save(attraction1)
attraction2 = Attraction("Imperial Palace", "Historic Site", city1)
attraction_repository.save(attraction2)
attraction3 = Attraction("Ghibli Museum", "Museum", city1, True)
attraction_repository.save(attraction3)

attraction4 = Attraction("Nishiki Market", "Food Market", city2)
attraction_repository.save(attraction4)
attraction5 = Attraction("Nijo Castle", "Historic Site", city2, True)
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
attraction13 = Attraction("Royal Palace", "Historical Site", city7, True)
attraction_repository.save(attraction13)
attraction14 = Attraction("Gran Via", "Food & Shopping", city7)
attraction_repository.save(attraction14)

attraction15 = Attraction("Camp Nou", "Sports", city8)
attraction_repository.save(attraction15)

attraction16 = Attraction("Buckingham Palace", "Historic Site", city9, True)
attraction_repository.save(attraction16)
attraction17 = Attraction("Spitalfields Market", "Market", city9)
attraction_repository.save(attraction17)
attraction18 = Attraction("British Museum", "Museum", city9)
attraction_repository.save(attraction18)

attraction19 = Attraction("Kelvingrove Museum", "Museum", city10)
attraction_repository.save(attraction19)
attraction20 = Attraction("Glasgow Cathedral", "Place of Worship", city10)
attraction_repository.save(attraction20)

attraction21 = Attraction("Rijksmuseum", "Museum", city11, True)
attraction_repository.save(attraction21)
attraction22 = Attraction("River Cruise", "Boat Tour", city11, True)
attraction_repository.save(attraction22)
attraction23 = Attraction("Bloemenmarkt", "Flower Market",city11)
attraction_repository.save(attraction23)

attraction24 = Attraction("Rotterdam Zoo", "Zoo", city12, True)
attraction_repository.save(attraction24)

attraction25 = Attraction("Acropolis Museum", "Museum", city13, True)
attraction_repository.save(attraction25)
attraction26 = Attraction("Parthenon", "Historic Site", city13, True)
attraction_repository.save(attraction26)
attraction27 = Attraction("National Garden", "Parks & Nature", city13)
attraction_repository.save(attraction27)

attraction28 = Attraction("Botanic Park", "Parks & Nature", city14, True)
attraction_repository.save(attraction28)
attraction29 = Attraction("Old Port", "Historic Site", city14)
attraction_repository.save(attraction29)



# res = attraction_repository.select_all()
# for attraction in res:
#     print(attraction.__dict__)

# attraction18.name = "V&A"
# attraction_repository.update(attraction18)

review1 = Review("Turtles", "Had a lovely time at this park and the best part was seeing the terrapins that live in the pond. It was great weather for October!", attraction12)
review_repository.save(review1)
review2 = Review("Kelvingrove", "Great park in the grounds of the museum. Found a fantastic pizza place across from the museum!", attraction19)
review_repository.save(review2)


# res = review_repository.select_all()
# for review in res:
#     print(review.__dict__)

review1.title = "El Retiro"
review_repository.update(review1)

pdb.set_trace()

