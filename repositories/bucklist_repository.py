from db.run_sql import run_sql

from models.destination import Destination
from models.country import Country
from models.bucketlist import Bucketlist


def save(bucketlist):
    sql = "INSERT INTO bucketlists (destination_id) VALUES (%s) RETURNING *"
    values = [bucketlist.destination.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    bucketlist.id = id
    return bucketlist


