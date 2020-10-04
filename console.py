import pdb

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


country1 = Country("Japan", "Asia")
country_repository.save(country1)

country2 = Country("France", "Europe")
country_repository.save(country2)

country3 = Country("Canada", "North America")
country_repository.save(country3)

country4 = Country("Mexico", "North America")
country_repository.save(country4)

country5 = Country("Germany", "Europe")
country_repository.save(country5)

# Japan
city1 = City("Osaka", country1)
city_repository.save(city1)
city2 = City("Tokyo", country1)
city_repository.save(city2)

# France
city3 = City("Paris", country2)
city_repository.save(city3)


# Canada
city4 = City("Vancover", country3)
city_repository.save(city4)
city5 = City("Calgary", country3)
city_repository.save(city5)

# Mexico
city6 = City("Mexico City", country4)
city_repository.save(city6)

# Germany
city7 = City("Berlin", country5)
city_repository.save(city7)
city8 = City("Hamburg", country5)
city_repository.save(city8)