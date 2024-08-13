#!/usr/bin/env python3
""" Lists all documents in a collection """


def insert_school(mongo_collection, **kwargs):
    """insert"""
    return mongo_collection.insert_one(kwargs).inserted_id
