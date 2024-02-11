#!/usr/bin/python3
"""
Review module for the HBNB project 
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews made by users about a place"""
    place_id = ""
    user_id = ""
    text = ""
