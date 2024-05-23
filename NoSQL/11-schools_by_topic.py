#!/usr/bin/env python3
"""Finds data"""


def schools_by_topic(mongo_collection, topic):
    """Finds data that contain the specified topic"""
    return mongo_collection.find({"topics": topic})
