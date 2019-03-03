#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:04:00 2019

@author: larry1285
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def gg():
    return "Hello World!"
@app.route("/home")
def home():
    return "home!"
@app.route("/about")

def about():
    return "about "