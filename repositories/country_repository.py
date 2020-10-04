from db.run_sql import run_sql

from models.city import City
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return country

