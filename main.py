#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

# Landing Page with choice of cities to query
@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Toronto'}, {'name':'Montreal'}, {'name':'Calgary'},
        {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
        {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'}, 
        {'name':'Quebec'}])

# Displays the response object information
@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)
# Run the App
if __name__=='__main__':
    app.run(debug=True)
