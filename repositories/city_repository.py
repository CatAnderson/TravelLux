from db.run_sql import run_sql

from models.city import City
from models.country import Country


def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

