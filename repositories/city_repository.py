from db.run_sql import run_sql

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        name = row['name']
        country_id = country_repository.select(row["country_id"])
        visited = row['visited']
        city_id = row['id']
        city = City(name, country_id, visited)
        cities.append(city)
    return cities
