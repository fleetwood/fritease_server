from flask import Flask, jsonify, render_template

app = Flask(__name__)

from app import routes
