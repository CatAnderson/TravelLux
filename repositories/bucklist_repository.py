from db.run_sql import run_sql

from models.destination import Destination
from models.country import Country
from models.bucketlist import Bucketlist

import repositories.destination_repository as destination_repository


def save(bucketlist):
    sql = "INSERT INTO bucketlists (destination_id) VALUES (%s) RETURNING *"
    values = [bucketlist.destination.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    bucketlist.id = id
    return bucketlist


def select_all():
    bucketlists = []

    sql = "SELECT * FROM bucketlists"
    results = run_sql(sql)

    for row in results:
        destination_id = destination_repository.id
        bucketlist_id = row["id"]
        bucketlist = Bucketlist(destination_id, bucketlist_id)
        bucketlists.append(bucketlist)
    return bucketlists


def select(id):
    bucketlist = None
    sql = "SELECT * FROM buckelist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        destination_id = destination_repository.select(result['destination_id'])
        bucketlist_id = result["id"]
        bucketlist = Bucketlist(destination_id, bucketlist_id)
    return bucketlist


def delete_all():
    sql = "DELETE FROM bucketlists"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bucketlists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

