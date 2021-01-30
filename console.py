import pdb 
from models.country import Country 
from models.city import City 
from models.attraction import Attraction
from models.review import Review 

import repositories.country_repository as country_repository

country1 = Country("Japan", True, True)
country_repository.save(country1)


pdb.set_trace()

