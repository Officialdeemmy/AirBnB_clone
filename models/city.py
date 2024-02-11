#!/usr/bin/python3
"""
City Module for HBNB project
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines city to look for"""
    state_id = ""
    name = ""
