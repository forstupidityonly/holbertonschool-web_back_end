#!/usr/bin/env python3
"""learn pyhton"""

def schools_by_topic(mongo_collection, topic):
    """rtn list of list"""
    return mongo_collection.find({"topics": topic})
