from db.run_sql import run_sql

from models.destination import Destination
from models.country import Country

import repositories.country_repository as country_repository


def save(destination):
    sql = "INSERT INTO destinations (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [destination.name, destination.country.id, destination.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    destination.id = id
    return destination


def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        name = row['name']
        country_id = country_repository.select(row["country_id"])
        visited = row['visited']
        destination_id = row['id']
        destination = Destination(name, country_id, visited, destination_id)
        destinations.append(destination)
    return destinations


def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        name = result['name']
        country_id = country_repository.select(result["country_id"])
        visited = result['visited']
        destination_id = result['id']
        destination = Destination(name, country_id, visited, destination_id)
    return destination


def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(destination):
    sql = "UPDATE destinations SET (name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [destination.name, destination.country.id, destination.visited, destination.id]
    run_sql(sql, values)
    