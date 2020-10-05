import pdb

from models.destination import Destination
from models.country import Country

import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository


destination_repository.delete_all()
country_repository.delete_all()


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

country6 = Country("New Zealand", "Oceania")
country_repository.save(country6)

# testing update country
# country7 = Country("Spain", "Asia")
# country_repository.save(country7)
# print(country_repository.select(country7.id))
# country7.continent = "Europe"
# country_repository.update(country7)


# Japan
destination1 = Destination("Osaka", country1)
destination_repository.save(destination1)
destination2 = Destination("Tokyo", country1)
destination_repository.save(destination2)

# France
destination3 = Destination("Paris", country2)
destination_repository.save(destination3)

# Canada
destination4 = Destination("Vancover", country3)
destination_repository.save(destination4)
destination5 = Destination("Calgary", country3)
destination_repository.save(destination5)

# Mexico
destination6 = Destination("Guadalajara", country4)
destination_repository.save(destination6)

# Germany
destination7 = Destination("Berlin", country5)
destination_repository.save(destination7)
destination8 = Destination("Hamburg", country5)
destination_repository.save(destination8)

# New Zealand
destination9 = Destination("Christchurch", country6)
destination_repository.save(destination9)

# testing update city
# destination10 = Destination("Mexico Ctiy", country6)
# destination_repository.save(destination10)
# print(destination_repository.select(destination10.id))
# destination10.name = "Mexico City"
# destination_repository.update(destination10)


pdb.set_trace()