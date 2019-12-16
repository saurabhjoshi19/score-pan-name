from flask import render_template, url_for, redirect, jsonify
from flask import request

from app import app
from app.forms import StringScoreForm
from .utils import levenshtein_ratio


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    string_score_form = StringScoreForm()
    if string_score_form.validate_on_submit():
        score = levenshtein_ratio(string_score_form.applicant_name.data, string_score_form.pan_name.data)
        return render_template('score.html', score=score)
    return render_template('index.html', form=string_score_form)


@app.route('/getScore', methods=['POST'])
def get_score():
    json = request.get_json()
    applicant_name = json['applicant_name']
    pan_name = json['pan_name']
    return jsonify("Your score is {} %".format(levenshtein_ratio(applicant_name, pan_name)))
