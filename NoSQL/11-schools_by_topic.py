#!/usr/bin/env python3
"""School by Topic"""

def schools_by_topic(mongo_collection, topic):
    """Returns a list of dictionaries that contain a topic"""
    return mongo_collection.find({"topics": topic})