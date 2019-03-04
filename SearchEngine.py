#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:04:00 2019

@author: larry1285
"""
from flask import Flask, render_template,  redirect, request
from forms import SearchForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/",  methods=['GET', 'POST'])
def search():
    #create form and display search page
    form = SearchForm()
    return render_template('search.html',form=form)

@app.route("/searchResult",  methods=['GET', 'POST'])
def searchResult():
    #processing POST form
    if request.method == 'POST' :
        form = SearchForm()
        data=request.form
        query=data.get('query')
        #call our program and store the urls in a variable
        urls=["https://www.google.com.tw/","test.uci.com","123.com"]
        #display searchResult page
        return render_template('searchResult.html',query=query,form=form,urls=urls,urlsLen=len(urls))
    #else:
    return "error"


