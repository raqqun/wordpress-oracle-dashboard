import os

basedir = os.path.abspath(os.path.dirname(__file__))

# This is the path of our database file.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# This is the folder where we will store database migration data files.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Enable CSRF
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# Wordpress Oracle Plugin Endpoints
WP_ORACLE_API = {
    'status': 'wp-oracle/status',
    'version': 'wp-oracle/version',
    'plugins': 'wp-oracle/plugins',
    'themes': 'wp-oracle/themes',
    'core_update': 'wp-oracle/core_updates',
    'plugin_update': 'wp-oracle/plugin_updates',
    'theme_update': 'wp-oracle/theme_updates',
    'translation_update': 'wp-oracle/translation_update',
    'core_upgrade': 'wp-oracle/core_upgrade',
    'plugin_upgrade': 'wp-oracle/plugin_upgrade?plugin=',
    'theme_upgrade': 'wp-oracle/theme_upgrade?theme=',
    'translation_upgrade': 'wp-oracle/translation_upgrade'
}