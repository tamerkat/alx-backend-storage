#!/usr/bin/env python3
""" Lists all documents in a collection """


def schools_by_topic(mongo_collection, topic):
    """mongo"""
    return mongo_collection.find({ "topic": topic })
