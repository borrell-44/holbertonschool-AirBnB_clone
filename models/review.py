#!/usr/bin/python3

""" class Review file """

from models.base_model import BaseModel


class Review(BaseModel):

    """ Reviews of AirBnB """

    place_id = ""
    user_id = ""
    text = ""
