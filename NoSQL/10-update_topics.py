#!/usr/bin/env python3
"""Updates a document"""


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a document"""
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return result.modified_count
