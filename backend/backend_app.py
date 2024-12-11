from flask import Flask, request, jsonify
from functools import wraps
from datetime import datetime
import json
import os


app = Flask(__name__)


# Simple in-memmory user store and token store
USERS = {}
TOKENS = {}


# File for persistant post storage
FILE_PATH = 'redundant_things_to_know.json'


# Rate Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hoer"]
)


# Load and save posts from JSON file for persistance
def load_posts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    return []


def save_posts(posts):
    with open(FILE_PATH, 'w') as f:
        json.dump(posts, f)


POSTS = load_posts()


# User Authentication
