#!/usr/bin/env python3
""" python + mongodb"""

def list_all(mongo_collection):
    """list all"""
    return mongo_collection.find()
