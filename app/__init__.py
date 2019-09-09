from flask import Flask, jsonify, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes
