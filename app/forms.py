# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, validators

##################################################################
# Form Name: ArtistForm
# Fields: artist(string)
# Explanation: Form used in the submit view and template, which
#              receives the name of an artist to be queried.
##################################################################

class ArtistForm(FlaskForm):
    artist = TextField(u'Metal artist', [validators.DataRequired(
        message='Please submit a metal artist'
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
    )], render_kw={"placeholder": "Email"})
    evaluation1 = BooleanField('Evaluation 1', default=False)
    evaluation2 = BooleanField('Evaluation 2', default=False)
    evaluation3 = BooleanField('Evaluation 3', default=False)
    evaluation4 = BooleanField('Evaluation 4', default=False)
    evaluation5 = BooleanField('Evaluation 5', default=False)
