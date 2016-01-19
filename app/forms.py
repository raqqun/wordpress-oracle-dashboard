from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class NewContextForm(Form):
    context_name = StringField('Context Name', description='Context Name', validators=[DataRequired()])
    context_default = BooleanField('Default')


class NewInstallationForm(Form):
    name = StringField('installation-name', description='Installation Name', validators=[DataRequired()])
    base_url = StringField('installation-url', description='Base URL', validators=[DataRequired()])
    api_token = StringField('installation-token', description='API Token', validators=[DataRequired()])
    context_id = IntegerField('installation-context', description='Context', validators=[DataRequired()])

