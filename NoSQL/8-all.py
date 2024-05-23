#!/usr/bin/env python3
"""Lists all documents"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    all_documents = mongo_collection.find({})
    document_list = []
    for document in all_documents:
        document_list.append(document)
    return document_list
