#!\Python34\env Python
# -*- coding: <encoding utf-8> -*-  

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Limonium import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='首页',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='联系',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='关于',
        year=datetime.now().year,
        message='《电子发票综合服务平台》简介'
    )

@app.route('/regist')
def regist():
    """Renders the regist page."""
    return render_template(
        'regist.html',
        title='注册',
        year=datetime.now().year,
        message='注册您的账户'
    )