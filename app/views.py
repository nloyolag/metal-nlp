# -*- coding: utf-8 -*-

import os
from flask import request, render_template, redirect, url_for, send_from_directory, flash, session
from forms import LyricsForm, EvaluationForm
from methods import predict_cluster, save_results
from app import app

##################################################################
# View Name: submit_view
# Methods: GET, POST
# Explanation: View that allows to upload lyrics from a metal
#              song to the site.
# GET: Renders the template with the lyrics form
# POST: Sends the lyrics to the server, and predicts the cluster
#       to which the song belongs to.
##################################################################

@app.route('/', methods=['GET', 'POST'])
def submit_view():
    form = LyricsForm()
    if request.method == 'POST' and form.validate():
        result = predict_cluster(form.lyrics.data)
        session['cluster_info'] = result
        return redirect(url_for('evaluation_view'))
    else:
        return render_template("index.html", form=form)

##################################################################
# View Name: evaluation_view
# Methods: GET, POST
# Explanation: View that shows the clustering results and shows
#              a form to evaluate the recommendations.
# GET: Renders the template with the evaluation form
#      and the previously uploaded lyrics.
# POST: Gathers the recommendations and saves them to a file.
#       The view then redirects to a thank you page.
##################################################################

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation_view():
    form = CoordinateForm()
    if request.method == 'POST' and form.validate():
        results = {
            'email': form.email.data,
            'evaluation1': form.evaluation1.data,
            'evaluation2': form.evaluation2.data,
            'evaluation3': form.evaluation3.data,
            'evaluation4': form.evaluation4.data,
            'evaluation5': form.evaluation5.data
        }
        save_results(results)
        return redirect(url_for('thanks_view'))
    else:
        cluster_info = session['cluster_info']
        return render_template("evaluate.html", cluster_info=cluster_info, form=form)

##################################################################
# View Name: thanks_view
# Methods: GET
# Explanation: View that thanks the user for submitting his
#              answer.
# GET: Renders the thanks view.
##################################################################

@app.route('/thanks', methods=['GET'])
def thanks_view():
    return render_template("thanks.html")