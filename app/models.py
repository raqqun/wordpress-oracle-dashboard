from app import db



class Contextes(db.Model):
    context_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    default = db.Column(db.Boolean(), default=0)
    installation = db.relationship('Installations', backref='context', lazy='dynamic')


class Installations(db.Model):
    installation_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    version = db.Column(db.String(255))
    base_url = db.Column(db.String(255))
    api_token = db.Column(db.String(255))
    context_id = db.Column(db.Integer, db.ForeignKey('contextes.context_id'))
    plugin = db.relationship('Plugins', backref='installation', lazy='dynamic')
    theme = db.relationship('Themes', backref='installation', lazy='dynamic')


class Plugins(db.Model):
    plugin_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    version = db.Column(db.String(255))
    file_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    installation_id = db.Column(db.Integer, db.ForeignKey('installations.installation_id'))


class Themes(db.Model):
    theme_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    version = db.Column(db.String(255))
    file_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    installation_id = db.Column(db.Integer, db.ForeignKey('installations.installation_id'))
