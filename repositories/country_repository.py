from db.run_sql import run_sql

from models.city import City
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        name = row['name']
        continent = row['continent']
        country_id = row['id']
        country = (name, continent, country_id)
        countries.append(country)
    return countries
    

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        name = result['name']
        continent = result['continent']
        country_id = result['id']
        country = (name, continent, country_id)
    return country



