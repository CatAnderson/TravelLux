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


