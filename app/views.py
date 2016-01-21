from flask import render_template, request, g, jsonify, url_for, flash, redirect
from app import app, db
from models import Contextes, Installations, Plugins, Themes
from forms import NewContextForm, NewInstallationForm

from config import WP_ORACLE_API

import requests

@app.route("/")
@app.route("/index")
def index():
    ContextForm = NewContextForm()
    InstallationForm = NewInstallationForm()
    contexts = Contextes.query.all()
    installations = Installations.query.all()
    return render_template('index.html',
        context_form=ContextForm,
        installation_form=InstallationForm,
        contexts=contexts,
        installations=installations)


# Get or Update Specific Context
@app.route("/contexts/<int:id>", methods=['GET', 'PUT'])
def get_contexts(id):
    if request.method == 'PUT':
        return 'Context Updated'
    else:
        return "Context id : %d" % id


# Get Plugins Of Specific Installation
@app.route('/installations/<int:id>/plugins', methods=['GET'])
def get_plugins(id):
    plugins = []
    return jsonify(plugins=plugins)


# Get Themes Of Specific Installations
@app.route('/installations/<int:id>/themes', methods=['GET'])
def get_themes(id):
    themes = []
    return jsonify(themes=themes)


# Get Installations Of Speficic Context
@app.route("/contexts/<int:id>/installations", methods=['GET'])
def get_context_installations(id):
    installations = []
    return jsonify(installations=installations)


# Get or Update Specific Installation
@app.route("/installations/<int:id>", methods=['GET', 'PUT'])
def installations(id):
    if request.method == 'PUT':
        return 'update'
    else:
        return "Installation id : %d" % id


# Create New Context
@app.route("/contexts", methods=['POST'])
def new_context():
    ContextForm = NewContextForm()

    if ContextForm.validate_on_submit():
        context = Contextes()
        context.name = ContextForm.context_name.data
        context.default = ContextForm.context_default.data
        db.session.add(context)
        db.session.commit()
        return jsonify(context=context.name + ' Created')


    errors = {}
    for field_name, field_errors in ContextForm.errors.iteritems():
        errors[ContextForm[field_name].description] = field_errors

    return jsonify(errors=errors)


# Create New Installation
@app.route("/installations", methods=['POST'])
def new_installation():
    InstallationForm = NewInstallationForm()

    if InstallationForm.validate_on_submit():
        installation = Installations()
        installation.name = InstallationForm.name.data
        installation.base_url = InstallationForm.base_url.data
        installation.context_id = InstallationForm.context_id.data
        installation.api_token = InstallationForm.api_token.data

        r = requests.get(
            installation.base_url + WP_ORACLE_API['status'],
            headers={'API-TOKEN': installation.api_token}
        )

        r_json = r.json()
        if (r.status_code == 200) and (r_json['blog']['status'] == 'ok'):
            pass
        else:
            pass
            # db.session.add(installation)
            # db.session.commit()

        return 'ok'

        # return jsonify(installation=installation.name + ' Installation Created')

    errors = {}
    for field_name, field_errors in InstallationForm.errors.iteritems():
        errors[InstallationForm[field_name].description] = field_errors

    return jsonify(errors=errors)

