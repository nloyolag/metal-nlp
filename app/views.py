# -*- coding: utf-8 -*-

import os
import pickle
from flask import request, render_template, redirect, url_for, session
from forms import ArtistForm, EvaluationForm
from methods import predict_cluster, save_results
from app import app
from app import APP_STATIC, APP_ROOT

# mode = "NORMAL"
mode = "RANDOM"

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
    form = ArtistForm()
    if request.method == 'POST' and form.validate():
        result = predict_cluster(form.artist.data, mode)
        if result == None:
            form.artist.errors.append('The submitted artist is not available.')
            return render_template("index.html", form=form)
        with open(os.path.join(APP_STATIC, 'data/prediction_data.pkl'), 'wb') as f:
            pickle.dump(result, f, pickle.HIGHEST_PROTOCOL)
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
    form = EvaluationForm()
    if request.method == 'POST' and form.validate():
        results = {
            'email': form.email.data,
            'evaluation1': form.evaluation1.data,
            'evaluation2': form.evaluation2.data,
            'evaluation3': form.evaluation3.data,
            'evaluation4': form.evaluation4.data,
            'evaluation5': form.evaluation5.data
        }
        save_results(results, mode)
        return redirect(url_for('thanks_view'))
    else:
        cluster_info = {}
        with open(os.path.join(APP_STATIC, 'data/prediction_data.pkl'), 'rb') as f:
            cluster_info = pickle.load(f)
        eval_fields = [
            form.evaluation1,
            form.evaluation2,
            form.evaluation3,
            form.evaluation4,
            form.evaluation5
        ]
        return render_template(
            "evaluate.html",
            cluster_info=cluster_info,
            eval_fields=eval_fields,
            form=form
        )

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
