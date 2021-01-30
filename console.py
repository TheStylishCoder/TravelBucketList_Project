import pdb 
from models.country import Country 
from models.city import City 
from models.attraction import Attraction
from models.review import Review 

import repositories.country_repository as country_repository

country_repository.delete_all()

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

country_repository.select_all()


pdb.set_trace()

