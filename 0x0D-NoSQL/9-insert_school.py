#!/usr/bin/env/python3
"""insert a document"""


def insert_school(mongo_collection, **kwargs):
    """insert new doc"""
    col = mongo_collection.insert_one(kwargs)
    return col.inserted_id
