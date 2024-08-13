#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """retuen doc in collection"""
    return [result for result in mongo_collection.find()]
