#!/usr/bin/env Python
# -*- coding: <encoding utf-8> -*-  

"""
Form and data for the Limonium Solution.
"""

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo

from


#  The Form of the regist.

class RegistForm(Form):
    email = StringField('Email', validators = [Required(), Length(1,64), Email()])
    username = StringField('Username', validators = [Required(), Length(1,64), \
                            Regexp('^[A-Za-z0-9_.]*$', 0, \
                            'Username must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators =[Required(), EqualTo('password2', message =\
                              'Passwords must match.')])
    password2 = PasswordField('Confirm password', validators = [Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already in use.')

