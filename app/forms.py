# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, BooleanField, validators

##################################################################
# Form Name: LyricForm
# Fields: lyrics(string)
# Explanation: Form used in the submit view and template, which
#              receives the lyrics of a song to be categorized.
##################################################################

class LyricForm(FlaskForm):
    lyrics = TextAreaField(u'Metal song lyrics', [validators.DataRequired(
        message='Please submit lyrics from a metal song'
    )])

##################################################################
# Form Name: EvaluationForm
# Fields: email(Text)
#         evaluation1(Boolean)
#         evaluation2(Boolean)
#         evaluation3(Boolean)
#         evaluation4(Boolean)
#         evaluation5(Boolean)
# Explanation: Form used in the evaluation view and template,
#              which receives the user's email, and
#              the evaluations of the recommendations provided
#              by the system.
##################################################################

class EvaluationForm(FlaskForm):
    email = TextField('Email', [validators.DataRequired(
        message='Please provide your email'
    )])
    evaluation1 = BooleanField('Evaluation 1', [validators.DataRequired(
        message='Please evaluate the recommendation'
    )])
    evaluation2 = BooleanField('Evaluation 2', [validators.DataRequired(
        message='Please evaluate the recommendation'
    )])
    evaluation3 = BooleanField('Evaluation 3', [validators.DataRequired(
        message='Please evaluate the recommendation'
    )])
    evaluation4 = BooleanField('Evaluation 4', [validators.DataRequired(
        message='Please evaluate the recommendation'
    )])
    evaluation5 = BooleanField('Evaluation 5', [validators.DataRequired(
        message='Please evaluate the recommendation'
    )])
