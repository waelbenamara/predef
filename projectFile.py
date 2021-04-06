from flask_website import app
app.run(debug=True)

#!/usr/bin/env python
from flask_website import app
from flask_website.search import update_documentation_index
with app.test_request_context():
    update_documentation_index()

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'testkey'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'flask-website.db')
DATABASE_CONNECT_OPTIONS = {}
ADMINS = frozenset(['http://lucumr.pocoo.org/'])

WHOOSH_INDEX = os.path.join(_basedir, 'flask-website.whoosh')
DOCUMENTATION_PATH = os.path.join(_basedir, '../flask/docs/_build/dirhtml')

del os

# flasky extensions.  flasky pygments style based on tango style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class FlaskyStyle(Style):
    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        # No corresponding class for the following:
        #Text:                     "", # class:  ''
        Whitespace:                "underline #f8f8f8",      # class: 'w'
        Error:                     "#a40000 border:#ef2929", # class: 'err'
        Other:                     "#000000",                # class 'x'

        Comment:                   "italic #8f5902", # class: 'c'
        Comment.Preproc:           "noitalic",       # class: 'cp'

        Keyword:                   "bold #004461",   # class: 'k'
        Keyword.Constant:          "bold #004461",   # class: 'kc'
        Keyword.Declaration:       "bold #004461",   # class: 'kd'
        Keyword.Namespace:         "bold #004461",   # class: 'kn'
        Keyword.Pseudo:            "bold #004461",   # class: 'kp'
        Keyword.Reserved:          "bold #004461",   # class: 'kr'
        Keyword.Type:              "bold #004461",   # class: 'kt'

        Operator:                  "#582800",   # class: 'o'
        Operator.Word:             "bold #004461",   # class: 'ow' - like keywords

        Punctuation:               "bold #000000",   # class: 'p'

        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name:                      "#000000",        # class: 'n'
        Name.Attribute:            "#c4a000",        # class: 'na' - to be revised
        Name.Builtin:              "#004461",        # class: 'nb'
        Name.Builtin.Pseudo:       "#3465a4",        # class: 'bp'
        Name.Class:                "#000000",        # class: 'nc' - to be revised
        Name.Constant:             "#000000",        # class: 'no' - to be revised
        Name.Decorator:            "#888",           # class: 'nd' - to be revised
        Name.Entity:               "#ce5c00",        # class: 'ni'
        Name.Exception:            "bold #cc0000",   # class: 'ne'
        Name.Function:             "#000000",        # class: 'nf'
        Name.Property:             "#000000",        # class: 'py'
        Name.Label:                "#f57900",        # class: 'nl'
        Name.Namespace:            "#000000",        # class: 'nn' - to be revised
        Name.Other:                "#000000",        # class: 'nx'
        Name.Tag:                  "bold #004461",   # class: 'nt' - like a keyword
        Name.Variable:             "#000000",        # class: 'nv' - to be revised
        Name.Variable.Class:       "#000000",        # class: 'vc' - to be revised
        Name.Variable.Global:      "#000000",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "#000000",        # class: 'vi' - to be revised

        Number:                    "#990000",        # class: 'm'

        Literal:                   "#000000",        # class: 'l'
        Literal.Date:              "#000000",        # class: 'ld'

        String:                    "#4e9a06",        # class: 's'
        String.Backtick:           "#4e9a06",        # class: 'sb'
        String.Char:               "#4e9a06",        # class: 'sc'
        String.Doc:                "italic #8f5902", # class: 'sd' - like a comment
        String.Double:             "#4e9a06",        # class: 's2'
        String.Escape:             "#4e9a06",        # class: 'se'
        String.Heredoc:            "#4e9a06",        # class: 'sh'
        String.Interpol:           "#4e9a06",        # class: 'si'
        String.Other:              "#4e9a06",        # class: 'sx'
        String.Regex:              "#4e9a06",        # class: 'sr'
        String.Single:             "#4e9a06",        # class: 's1'
        String.Symbol:             "#4e9a06",        # class: 'ss'

        Generic:                   "#000000",        # class: 'g'
        Generic.Deleted:           "#a40000",        # class: 'gd'
        Generic.Emph:              "italic #000000", # class: 'ge'
        Generic.Error:             "#ef2929",        # class: 'gr'
        Generic.Heading:           "bold #000080",   # class: 'gh'
        Generic.Inserted:          "#00A000",        # class: 'gi'
        Generic.Output:            "#888",           # class: 'go'
        Generic.Prompt:            "#745334",        # class: 'gp'
        Generic.Strong:            "bold #000000",   # class: 'gs'
        Generic.Subheading:        "bold #800080",   # class: 'gu'
        Generic.Traceback:         "bold #a40000",   # class: 'gt'
    }


# -*- coding: utf-8 -*-
from urlparse import urlparse
from werkzeug import url_quote
from flask import Markup


class Extension(object):

    def __init__(self, name, author, description,
                 github=None, gitlab=None, bitbucket=None, docs=None, website=None,
                 approved=False, notes=None):
        self.name = name
        self.author = author
        self.description = Markup(description)
        self.github = github
        self.gitlab = gitlab
        self.bitbucket = bitbucket
        self.docs = docs
        self.website = website
        self.approved = approved
        self.notes = notes

    def to_json(self):
        rv = vars(self).copy()
        rv['description'] = unicode(rv['description'])
        return rv

    @property
    def pypi(self):
        return 'http://pypi.python.org/pypi/%s' % url_quote(self.name)

    @property
    def docserver(self):
        if self.docs:
            return urlparse(self.docs)[1]


# This list contains all extensions that were approved as well as those which
# passed listing.
extensions = [
    Extension('Flask-OpenID', 'Armin Ronacher',
        description='''
            <p>Adds <a href="http://openid.net/">OpenID</a> support to Flask.
        ''',
        github='mitsuhiko/flask-openid',
        docs='http://pythonhosted.org/Flask-OpenID/',
        notes='''
            Short long description, missing tests.
        '''
    ),
    Extension('Flask-Babel', 'Armin Ronacher',
        description='''
            <p>Adds i18n/l10n support to Flask, based on
            <a href=http://babel.edgewall.org/>babel</a> and
            <a href=http://pytz.sourceforge.net/>pytz</a>.
        ''',
        github='mitsuhiko/flask-babel',
        docs='http://pythonhosted.org/Flask-Babel/',
        approved=True,
        notes='''
            How to improve: add a better long description to the next release.
        '''
    ),
    Extension('Flask-SQLAlchemy', 'Armin Ronacher',
        description='''
            <p>Add <a href="http://www.sqlalchemy.org/">SQLAlchemy</a> support to Flask
            with automatic configuration and helpers to simplify common web use cases.
            Major features include:</p>
            <ul>
            <li>Handle configuring one or more database connections.</li>
            <li>Set up sessions scoped to the request/response cycle.</li>
            <li>Time queries and track model changes for debugging.</li>
            </ul>
        ''',
        github='mitsuhiko/flask-sqlalchemy',
        docs='http://flask-sqlalchemy.pocoo.org/',
        approved=True
    ),
    Extension('Flask-Migrate', 'Miguel Grinberg',
        description='''
            <p><a href="http://www.sqlalchemy.org/">SQLAlchemy</a> database
            migrations for Flask applications using
            <a href="https://alembic.readthedocs.org/">Alembic</a>. The
            database operations are provided as command line arguments for
            <a href="https://flask-script.readthedocs.org/">Flask-Script</a>.
        ''',
        github='miguelgrinberg/flask-migrate',
        docs='http://pythonhosted.org/Flask-Migrate/',
    ),
    Extension('Flask-XML-RPC', 'Matthew Frazier',
        description='''
            <p>Adds <a href="http://www.xmlrpc.com/">XML-RPC</a> support to Flask.
        ''',
        bitbucket='leafstorm/flask-xml-rpc',
        docs='http://pythonhosted.org/Flask-XML-RPC/',
        approved=True
    ),
    Extension('Flask-CouchDB', 'Matthew Frazier',
        description='''
            <p>Adds <a href="http://couchdb.apache.org/">CouchDB</a> support to Flask.
        ''',
        bitbucket='leafstorm/flask-couchdb',
        docs='http://pythonhosted.org/Flask-CouchDB/',
        approved=True,
        notes='''
            There is also Flask-CouchDBKit.  Both are fine because they are
            doing different things, but the latter is not yet approved.
        '''
    ),
    Extension('Flask-Uploads', 'Max Countryman',
        description='''
            <p>Flask-Uploads allows your application to flexibly and
            efficiently handle file uploading and serving the uploaded files.
            You can create different sets of uploads - one for document
            attachments, one for photos, etc.
        ''',
        github='maxcountryman/flask-uploads',
        docs='https://flask-uploads.readthedocs.org/en/latest/',
        approved=True
    ),
    Extension('Flask-Themes', 'Matthew Frazier',
        description='''
            <p>Flask-Themes makes it easy for your application to support
            a wide range of appearances.
        ''',
        bitbucket='leafstorm/flask-themes',
        docs='http://pythonhosted.org/Flask-Themes/',
        approved=True
    ),
    Extension('Flask-CouchDBKit', 'Kridsada Thanabulpong',
        description='''
            <p>Adds <a href="http://www.couchdbkit.org/">CouchDBKit</a> support to Flask.
        ''',
        github='sirn/flask-couchdbkit',
        docs='http://pythonhosted.org/Flask-CouchDBKit/'
    ),
    Extension('Flask-Genshi', 'Dag Odenhall',
        description='''
            <p>Adds support for the <a href="http://genshi.edgewall.org/">Genshi</a>
            templating language to Flask applications.
        ''',
        github='dag/flask-genshi',
        docs='http://pythonhosted.org/Flask-Genshi/',
        approved=True,
        notes='''
            This is the first template engine extension.  When others come
            around it would be a good idea to decide on a common interface.
        '''
    ),
    Extension('Flask-Mail', 'Matt Wright (created by Dan Jacob)',
        description='''
            <p>Makes sending mails from Flask applications very easy and
            has also support for unittesting.
        ''',
        github='mattupstate/flask-mail',
        docs='http://pythonhosted.org/Flask-Mail/',
        approved=True
    ),
    Extension('Flask-WTF', 'Anthony Ford (created by Dan Jacob)',
        description='''
            <p>Flask-WTF offers simple integration with WTForms. This
            integration includes optional CSRF handling for greater security.
        ''',
        github='ajford/flask-wtf',
        docs='http://pythonhosted.org/Flask-WTF/',
        approved=True
    ),
    Extension('Flask-Testing', u'Christoph Heer (created by Dan Jacob)',
        description='''
            <p>The Flask-Testing extension provides unit testing utilities for Flask.
        ''',
        github='jarus/flask-testing',
        docs='http://pythonhosted.org/Flask-Testing/',
        approved=True
    ),
    Extension('Flask-Script', 'Sean Lynch (created by Dan Jacob)',
        description='''
            <p>The Flask-Script extension provides support for writing external
            scripts in Flask. It uses argparse to parse command line arguments.
        ''',
        github='techniq/flask-script',
        docs='http://pythonhosted.org/Flask-Script/',
        approved=True,
        notes='''
            Flask-Actions has some overlap.  Consider that when approving
            Flask-Actions or similar packages.
        '''
    ),
    Extension('flask-lesscss', 'Steve Losh',
        description='''
            <p>
              A small Flask extension that makes it easy to use
              <a href=http://lesscss.org/>LessCSS</a> with your
              Flask application.
        ''',
        docs='http://sjl.bitbucket.org/flask-lesscss/',
        bitbucket='sjl/flask-lesscss',
        notes='''
            Broken package description, nonconforming package name, does not
            follow standard API rules (init_lesscss instead of lesscss).

            Considered for unlisting, improved version should release as
            "Flask-LessCSS" with a conforming API and fixed packages indices,
            as well as a testsuite.
        '''
    ),
    Extension('Flask-Creole', 'Ali Afshar',
        description='''
            <p>Creole parser filters for Flask.
        ''',
        docs='http://pythonhosted.org/Flask-Creole',
        bitbucket='aafshar/flask-creole-main',
        approved=True,
        notes='''
            Flask-Markdown and this should share API, consider that when
            approving Flask-Markdown
        '''
    ),
    Extension('Flask-Cache', 'Thadeus Burgess',
        description='''
            <p>Adds cache support to your Flask application.
        ''',
        docs='http://pythonhosted.org/Flask-Cache',
        github='thadeusb/flask-cache',
    ),
    Extension('Flask-Principal', 'Ali Afshar',
        description='''
            <p>Identity management for Flask.
        ''',
        docs='http://pythonhosted.org/Flask-Principal',
        github='mattupstate/flask-principal',
        approved=False
    ),
    Extension('Flask-Zen', 'Noah Kantrowitz',
        description='''
            <p>Flask-Zen allows you to use PyZen via Flask-Script commands.
        ''',
        docs='http://pythonhosted.org/Flask-Zen/',
        github='coderanger/flask-zen',
        approved=False
    ),
    Extension('Flask-Static-Compress', 'Alan Hamlett',
        description='''
            <p>Automatically minifies, combines, and versions your static CSS
              and JavaScript assets. Like Django-Compressor for Flask.
        ''',
        github='alanhamlett/flask-static-compress',
        docs='https://github.com/alanhamlett/flask-static-compress',
        approved=False
    ),
    Extension('Flask-Assets', u'Michael Elsdörfer',
        description='''
            <p>
              Integrates the webassets library with Flask, adding support for
              merging, minifying and compiling CSS and Javascript files.
        ''',
        docs='http://elsdoerfer.name/docs/flask-assets/',
        github='miracle2k/flask-assets',
        approved=False
    ),
    Extension('Flask-AutoIndex', 'Heungsub Lee',
        description='''
            <p>
              An extension that generates an index page for your Flask
              application automatically
        ''',
        docs='http://pythonhosted.org/Flask-AutoIndex/',
        github='sublee/flask-autoindex',
        approved=False
    ),
    Extension('Flask-Celery', 'Ask Solem',
        description='''
            <p>
              Celery integration for Flask
        ''',
        docs='http://ask.github.com/celery/',
        github='ask/flask-celery',
        approved=False
    ),
    Extension('Flask-Cors', 'Cory Dolphin',
        description='''
            <p>
              Cross Origin Resource Sharing (CORS)  for flask
        ''',
        docs='http://flask-cors.readthedocs.org/en/latest/',
        github='wcdolphin/flask-cors',
        approved=False
    ),
    Extension('Frozen-Flask', 'Simon Sapin',
        description='''
            <p>
              Freezes a Flask application into a set of static files.
              The result can be hosted without any server-side software
              other than a traditional web server.
        ''',
        docs='http://pythonhosted.org/Frozen-Flask/',
        github='SimonSapin/Frozen-Flask',
        approved=True
    ),
    Extension('Flask-FlatPages', 'Simon Sapin',
        description='''
            <p>
              Provides flat static pages to a Flask application, based on text
              files as opposed to a relational database.
        ''',
        docs='http://pythonhosted.org/Flask-FlatPages/',
        github='SimonSapin/Flask-FlatPages',
        approved=True
    ),
    Extension('Flask-FluidDB', 'Ali Afshar',
        description='''
            <p>
              FluidDB access for Flask.
        ''',
        docs='http://pythonhosted.org/Flask-FluidDB/',
        bitbucket='aafshar/flask-fluiddb-main',
        approved=False
    ),
    Extension('Flask-fillin', 'Christoph Heer',
        description='''
            <p>The Flask-fillin extension provides simple utilities for testing your forms in Flask application..
        ''',
        github='jarus/flask-fillin',
        docs='http://pythonhosted.org/Flask-fillin/',
    ),
    Extension('Flask-Gravatar', 'Zelenyak Aleksandr',
        description='''
            <p>
              Small extension for Flask to make using Gravatar easy.
        ''',
        docs='http://pythonhosted.org/Flask-Gravatar/',
        github='zzzsochi/Flask-Gravatar',
        approved=False
    ),
    Extension('Flask-HTMLBuilder', 'Zahari Petkov',
        description='''
            <p>
              Flask-HTMLBuilder is an extension that allows flexible and easy
              Python-only generation of HTML snippets and full HTML documents
              using a robust syntax.
        ''',
        docs='http://majorz.github.com/flask-htmlbuilder/',
        github='majorz/flask-htmlbuilder',
        approved=False
    ),
    Extension('Flask-MongoAlchemy', 'Francisco Souza',
        description='''
            <p>
              Add Flask support for MongoDB using MongoAlchemy.
        ''',
        docs='http://pythonhosted.org/Flask-MongoAlchemy/',
        github='cobrateam/flask-mongoalchemy',
        approved=False
    ),
    Extension('Flask-DebugToolbar', 'Matt Good',
        description='''
            <p>
              A port of the Django debug toolbar to Flask
        ''',
        docs='https://github.com/mgood/flask-debugtoolbar',
        github='mgood/flask-debugtoolbar',
        approved=False
    ),
    Extension('Flask-Login', 'Matthew Frazier',
        description='''
            <p>
              Flask-Login provides user session management for Flask. It
              handles the common tasks of logging in, logging out, and
              remembering your users' sessions over extended periods of time.
        ''',
        github='maxcountryman/flask-login',
        docs='http://pythonhosted.org/Flask-Login/',
        approved=True
    ),
    Extension('Flask-Security', 'Matt Wright',
        description='''
            <p>
              Flask-Security is an opinionated Flask extension which adds
              basic security and authentication features to your Flask apps
              quickly and easily.
        ''',
        docs='https://pythonhosted.org/Flask-Security/',
        github='mattupstate/flask-security'
    ),
    Extension('Flask-Exceptional', 'Jonathan Zempel',
        description='''
            <p>
              Adds Exceptional support to Flask applications
        ''',
        docs='http://pythonhosted.org/Flask-Exceptional/',
        github='jzempel/flask-exceptional',
        approved=True,
    ),
    Extension('Flask-Bcrypt', 'Max Countryman',
        description='''
            <p>
              Bcrypt support for hashing passwords
        ''',
        docs='http://pythonhosted.org/Flask-Bcrypt/',
        github='maxcountryman/flask-bcrypt',
        approved=True,
    ),
    Extension('Flask-MongoKit', 'Christoph Heer',
        description='''
            <p>
              Flask extension to better integrate MongoKit into Flask
        ''',
        docs='http://pythonhosted.org/Flask-MongoKit/',
        github='jarus/flask-mongokit'
    ),
    Extension('Flask-GAE-Mini-Profiler', 'Pascal Hartig',
        description='''
            <p>
              Flask integration of gae_mini_profiler for Google App Engine.
        ''',
        docs='http://pythonhosted.org/Flask-GAE-Mini-Profiler',
        github='passy/flask-gae-mini-profiler'
    ),
    Extension('Flask-Admin', 'Flask-Admin team',
        description='''
            <p>Simple and extensible administrative interface framework for Flask
        ''',
        docs='http://flask-admin.readthedocs.org/en/latest/index.html',
        github='flask-admin/flask-admin'
    ),
    Extension('Flask-ZODB', 'Dag Odenhall',
        description='''
            <p>
              Use the ZODB with Flask
        ''',
        docs='http://pythonhosted.org/Flask-ZODB/',
        github='dag/flask-zodb',
        approved=True
    ),
    Extension('Flask-Peewee', 'Charles Leifer',
        description='''
            <p>
              Integrates Flask and the peewee orm
        ''',
        docs='http://charlesleifer.com/docs/flask-peewee/index.html',
        github='coleifer/flask-peewee',
        approved=False
    ),
    Extension('Flask-Lettuce', 'Daniel, Dao Quang Minh',
        description='''
            <p>
              Add Lettuce support for Flask
        ''',
        # docs='http://pythonhosted.org/Flask-Lettuce/',
        github='dqminh/flask-lettuce',
        approved=False
    ),
    Extension('Flask-Sijax', 'Slavi Pantaleev',
        description='''
            <p>
              Flask integration for Sijax,
              a Python/jQuery library that makes AJAX easy to use
        ''',
        docs='http://pythonhosted.org/Flask-Sijax/',
        github='spantaleev/flask-sijax',
        approved=False
    ),
    Extension('Flask-Dashed', 'Jean-Philippe Serafin',
        description='''
            <p>
              Flask-Dashed provides tools for building
              simple and extensible admin interfaces.
        ''',
        docs='http://jeanphix.github.com/Flask-Dashed/',
        github='jeanphix/Flask-Dashed',
        approved=False
    ),
    Extension('Flask-SeaSurf', 'Max Countryman',
        description='''
            <p>
              SeaSurf is a Flask extension for preventing
              cross-site request forgery (CSRF).
        ''',
        docs='http://pythonhosted.org/Flask-SeaSurf/',
        github='maxcountryman/flask-seasurf',
        approved=True,
    ),
    Extension('Flask-PonyWhoosh', 'Jonathan Prieto-Cubides & Felipe Rodriguez',
        description='''
            <p>
              A full-text search engine using Pony ORM and Whoosh.
        ''',
        docs='https://pythonhosted.org/Flask-PonyWhoosh/',
        github='compiteing/flask-ponywhoosh',
    ),
    Extension('Flask-PyMongo', 'Dan Crosta',
        description='''
            <p>
              Flask-PyMongo bridges Flask and PyMongo.
        ''',
        docs='http://readthedocs.org/docs/flask-pymongo/',
        github='dcrosta/flask-pymongo',
    ),
    Extension('Flask-Raptor', 'Dan Lepage',
        description='''
            <p>
              Flask-Raptor provides support for adding raptors
              to Flask instances.
        ''',
        docs='http://pythonhosted.org/Flask-Raptor/',
        github='dplepage/flask-raptor',
    ),
    Extension('Flask-Shelve', 'James Saryerwinnie',
        description='''
            <p>
              Flask-Shelve bridges Flask and the Python standard library
              `shelve` module, for very simple (slow) no-dependency key-value
              storage.
        ''',
        docs='http://pythonhosted.org/Flask-Shelve/',
        github='jamesls/flask-shelve',
    ),
    Extension('Flask-RESTful', 'Twilio API Team',
        description='''
            <p>Flask-RESTful provides the building blocks for creating a great REST API.
        ''',
        docs='https://flask-restful.readthedocs.org/',
        github='flask-restful/flask-restful',
        approved=True
    ),
    Extension('Flask-Restless', 'Jeffrey Finkelstein',
        description='''
            <p>Flask-Restless provides simple generation of ReSTful APIs for
              database models defined using Flask-SQLAlchemy. The generated
              APIs send and receive messages in JSON format.
        ''',
        docs='http://readthedocs.org/docs/flask-restless/en/latest/',
        github='jfinkels/flask-restless',
        approved=True
    ),
    Extension('Flask-Heroku', 'Kenneth Reitz',
        description='''
            <p>Sets Flask configuration defaults for Heroku-esque environment variables
        ''',
        github='kennethreitz/flask-heroku',
        approved=False
    ),
    Extension('Flask-Mako', 'Beranger Enselme, Frank Murphy',
        description='''
            <p>Allows for <a href="http://www.makotemplates.org/">Mako templates</a>
            to be used instead of Jinja2
        ''',
        github='benselme/flask-mako',
        docs='http://pythonhosted.org/Flask-Mako/',
        approved=False
    ),
    Extension('Flask-WeasyPrint', 'Simon Sapin',
        description='''
            <p>Make PDF with <a href="http://weasyprint.org/">WeasyPrint</a>
               in your Flask app.
        ''',
        docs='http://pythonhosted.org/Flask-WeasyPrint/',
        github='SimonSapin/Flask-WeasyPrint',
    ),
    Extension('Flask-Classy', 'Freedom Dumlao',
        description='''
            <p>Class based views for Flask.
        ''',
        github='apiguy/flask-classy',
        docs='http://pythonhosted.org/Flask-Classy/',
        approved=False
    ),
    Extension('Flask-WebTest', 'Anton Romanovich',
        description='''
            <p>Utilities for testing Flask applications with
               <a href="http://webtest.readthedocs.org/en/latest/">WebTest</a>.
        ''',
        github='aromanovich/flask-webtest',
        docs='http://flask-webtest.readthedocs.org/',
        approved=False
    ),
    Extension('Flask-Misaka', 'David Baumgold',
        description='''
            A simple extension to integrate the
            <a href="http://misaka.61924.nl/">Misaka</a> module for efficiently
            parsing Markdown.
        ''',
        docs='https://flask-misaka.readthedocs.org/en/latest/',
        github='singingwolfboy/flask-misaka',
        approved=True,
    ),
    Extension('Flask-Dance', 'David Baumgold',
        description='''
            Doing the OAuth dance with style using Flask, requests, and oauthlib.
        ''',
        docs='https://flask-dance.readthedocs.org/en/latest/',
        github='singingwolfboy/flask-dance',
        approved=True,
    ),
    Extension('Flask-SSE', 'David Baumgold',
        description='''
            <a href="http://www.html5rocks.com/en/tutorials/eventsource/basics/">
            Server Sent Events</a> for Flask.
        ''',
        docs='https://flask-sse.readthedocs.org/en/latest/',
        github='singingwolfboy/flask-sse',
        approved=True,
    ),
    Extension('Flask-Limiter', 'Ali-Akber Saifee',
              description='''
            <p>Adds Ratelimiting support to Flask.
            Supports a configurable storage backend with implementations for
            in-memory, redis and memcache.
        ''',
        github='alisaifee/flask-limiter',
        docs='http://flask-limiter.readthedocs.org/en/latest/',
        approved=False,
    ),
    Extension('Flask-User', 'Ling Thio',
        description='''
            Customizable User Account Management for Flask:
            Register, Confirm email, Login, Change username, Change password, Forgot password,
            Role-based Authorization and Internationalization.
        ''',
        github='lingthio/flask-user',
        docs='http://flask-user.readthedocs.io/',
        approved=True,
    ),
    Extension('Flask-Via', 'SOON_, Chris Reeves',
        description='''
            <p>
                Provides a clean, simple URL routing framework for growing Flask
                Applications.
        ''',
        docs='http://flask-via.soon.build',
        github='thisissoon/Flask-Via',
    ),
    Extension('Flask-QueryInspect', 'Bret Barker',
        description='''
            <p>Provides metrics on SQL queries (using SQLAlchemy) executed
             for each request.</p>
        ''',
        docs='https://github.com/noise/flask-queryinspect',
        github='noise/flask-queryinspect',
    ),
    Extension('Flask-Stormpath', 'Randall Degges',
        description='''
            <p>Add Stormpath user management, authentication,
            and authorization to Flask.
        ''',
        docs='http://flask-stormpath.readthedocs.org/en/latest/',
        github='stormpath/stormpath-flask'
    ),
    Extension('Flask-Ask', 'John Wheeler',
        description='''
            <p>
              Flask-Ask makes it easy to write Amazon Echo apps with Flask and
              the Alexa Skills Kit.
        ''',
        docs='http://flask-ask.readthedocs.io/en/latest/',
        github='johnwheeler/flask-ask'
    ),
    Extension('Flask-Rest-JSONAPI', 'Pierre Chaisy',
        description='''
            <p>
              Build REST APIs following the
              <a href="http://jsonapi.org/format/">JSONAPI</a>
              specification with a powerful data layer system.
        ''',
        docs='http://flask-rest-jsonapi.readthedocs.io/en/latest/',
        github='miLibris/flask-rest-jsonapi'
    ),
    Extension('Flask-SAML', 'Florian Ruechel',
        description='''
            <p>
              Enable SAML authentication for your webapp.
        ''',
        docs='https://flask-saml.readthedocs.io/en/latest/',
        bitbucket='asecurityteam/flask_saml'
    ),
    Extension('Flask-Snow', 'Robert Wikman',
        description='''
            <p>
              Flask-snow enables easy access to the REST API in the ServiceNow ITSM platform
              with the help of the <a href="http://github.com/rbw0/pysnow">pysnow library</a>.
              Additionally, it supports OAuth for a seamless authentication / authorization experience.
        ''',
        docs='http://flask-snow.readthedocs.io/en/latest/',
        github='rbw0/flask-snow'
    ),
    Extension('flask-keycloak', 'Akhil Lawrence',
        description='''
            <p>Flask extension for
            <a href=https://www.keycloak.org>Keycloak</a> integration.
        ''',
        docs='https://github.com/akhilputhiry/flask-keycloak/blob/master/README.md',
        github='akhilputhiry/flask-keycloak',
    ),   
    Extension('Flask-MailboxValidator', 'MailboxValidator,
        description='''
            <p>
              Flask-MailboxValidator provides an easy way to call the MailboxValidator API which validates if an email address is a valid one.
        ''',
        docs='https://flask-mailboxvalidator.readthedocs.io/en/latest/',
        github='MailboxValidator/Flask_MailboxValidator'
    ),
    Extension('Flask-Dropzone', 'Grey Li',
        description='''
            <p>
              Upload file in Flask application with <a href="http://dropzonejs.com">Dropzone.js</a>.
        ''',
        docs='https://flask-dropzone.readthedocs.io/en/latest/',
        github='greyli/flask-dropzone',
    ),
    Extension('Flask-CKEditor', 'Grey Li',
        description='''
            <p>
              <a href="https://ckeditor.com">CKEditor</a> integration for Flask, including image 
              upload, code syntax highlight and more.
        ''',
        docs='https://flask-ckeditor.readthedocs.io/en/latest/',
        github='greyli/flask-ckeditor',
    ),
    Extension('Bootstrap-Flask', 'Grey Li',
        description='''
            <p>
              <a href="https://getbootstrap.com/">Bootstrap 4</a> helper for Flask/Jinja2. 
              Based on Flask-Bootstrap, but lighter and better.
        ''',
        docs='https://bootstrap-flask.readthedocs.io/en/latest/',
        github='greyli/bootstrap-flask',
    ),
    Extension('Flask-Avatars', 'Grey Li',
        description='''
            <p>
              All avatar generators in one place. Including:
              <ul>
                <li>Default avatar</li>
                <li>Gravatar</li>
                <li>Robohash</li>
                <li>Social media avatar</li>
                <li>Identicon generation</li>
                <li>Avatar crop</li>
              </ul>
        ''',
        docs='https://flask-avatars.readthedocs.io/en/latest/',
        github='greyli/flask-avatars',
    ),
    Extension('Flask-Share', 'Grey Li',
        description='''
            <p>
              Create social share component in Jinja2 template based on 
              <a href="https://github.com/overtrue/share.js/">share.js</a>.
        ''',
        docs='https://flask-share.readthedocs.io/en/latest/',
        github='greyli/flask-share',
    ),
    Extension('Flask-Praetorian', 'Tucker Beck',
        description='''
            <p>
              API security should be strong, simple, and precise like a Roman
              Legionary. This package aims to provide that. Using JWT tokens as
              implemented by PyJWT, flask-praetorian uses a very simple
              interface to make sure that the users accessing your API’s
              endpoints are provisioned with the correct roles for access.
        ''',
        docs='http://flask-praetorian.readthedocs.io/en/latest/',
        github='dusktreader/flask-praetorian',
    ),
    Extension('Flask-MonitoringDashboard', 'Patrick Vogel',
        description='''
            <p>
              Flask-MonitoringDashboard is an extension that offers 3 main functionalities with little effort from the 
              Flask developer:
              <ol>
                <li>Monitor and visualize the performance of a Flask application.</li>
                <li>Monitor and visualize the test coverage.</li>
                <li>Collect extra information about request outliers (requests which are slower than normal).</li>
              </ol>
            </p>
            ''',
        docs='http://flask-monitoringdashboard.readthedocs.io/',
        github='flask-dashboard/Flask-MonitoringDashboard'
    ),
    Extension('Flask-Dramatiq', 'Étienne Bersac',
        description='''
            <p>Plugs <a href="https://dramatiq.io/">Dramatiq</a> task queue in your
            Flask web app.
        ''',
        docs='https://flask-dramatiq.readthedocs.io/',
        gitlab='https://gitlab.com/bersace/flask-dramatiq',
    ),
    Extension('Flask-Assistant', 'Cam Sweeney',
        description='''
            <p>
             Framework for building conversational apps using
             Flask and API.AI with integration for Google Assistant.
        ''',
        docs='http://flask-assistant.readthedocs.io/en/latest/',
        github='treethought/flask-assistant'
    ),
]


# This is a list of extensions that is currently rejected from listing and with
# that also not approved.  If an extension ends up here it should improved to
# be listed.
unlisted = [
    Extension('Flask-Actions', 'Young King',
        description='''
            <p>
              Flask-actions provide some management comands for flask based
              project.
        ''',
        docs='http://pythonhosted.org/Flask-Actions/',
        bitbucket='youngking/flask-actions',
        approved=False,
        notes='''
            Rejected because of missing description in PyPI, formatting issues
            with the documentation (missing headlines, scrollbars etc.) and a
            general clash of functionality with the Flask-Script package.
            Latter should not be a problem, but the documentation should
            improve.  For listing, the extension developer should probably
            discuss the extension on the mailinglist with others.

            Futhermore it also has an egg registered with an invalid filename.
        '''
    ),
    Extension('Flask-Jinja2Extender', 'Dan Colish',
        description='''
            <p>
        ''',
        docs=None,
        github='dcolish/flask-jinja2extender',
        approved=False,
        notes='''
            Appears to be discontinued.

            Usecase not obvious, hacky implementation, does not solve a problem
            that could not be solved with Flask itself.  I suppose it is to aid
            other extensions, but that should be discussed on the mailinglist.
        '''
    ),
    Extension('Flask-Markdown', 'Dan Colish',
        description='''
            <p>
              This is a small module to a markdown processing filter into your
              flask.
        ''',
        docs='http://pythonhosted.org/Flask-Markdown/',
        github='dcolish/flask-markdown',
        approved=False,
        notes='''
            Would be great for enlisting but it should follow the API of
            Flask-Creole.  Besides that, the docstrings are not valid rst (run
            through rst2html to see the issue) and it is missing tests.
            Otherwise fine :)
        '''
    ),
    Extension('flask-urls', 'Steve Losh',
        description='''
            <p>
              A collection of URL-related functions for Flask applications.
        ''',
        docs='http://sjl.bitbucket.org/flask-urls/',
        bitbucket='sjl/flask-urls',
        approved=False,
        notes='''
            Broken PyPI index and non-conforming extension name.  Due to the
            small featureset this was also delisted from the list.  It was
            there previously before the approval process was introduced.
        '''
    ),
    Extension('Flask-Coffee', 'Col Wilson',
        description='''
            <p>
              Automatically compile CoffeeScript files while developing with
              the Flask framework.
        ''',
        docs=None,
        approved=False,
        notes='''
            On the mailing list, author claims it's flask-lesscss with a
            different label.  No sphinx-based docs, just a blog post.  No
            publicly accessible repository -- requires login on
            bettercodes.org.
        '''
    ),
    Extension('Flask-Solr', 'Ron DuPlain',
        description='''
            <p>
              Add Solr support to Flask using pysolr.
        ''',
        docs=None,
        github='willowtreeapps/flask-solr',
        notes='''
            Fully exposes pysolr API in Flask extension pattern, and code is
            production-ready.  It lacks documentation and tests.
        '''
    ),
    Extension('flask-csrf', 'Steve Losh',
        description='''
            <p>A small Flask extension for adding
            <a href=http://en.wikipedia.org/wiki/CSRF>CSRF</a> protection.
        ''',
        docs='http://sjl.bitbucket.org/flask-csrf/',
        bitbucket='sjl/flask-csrf',
        notes='''
            Unlisted because duplicates the Flask-SeaSurf extension.
        '''
    ),
]


extensions.sort(key=lambda x: x.name.lower())
unlisted.sort(key=lambda x: x.name.lower())

from urlparse import urljoin


server = 'https://pypi.org/'
detail_path = '/project/Flask/%s/'


class Release(object):

    def __init__(self, version):
        self.version = version

    def to_json(self):
        return dict(version=self.version,
                    detail_url=self.detail_url)

    @property
    def detail_url(self):
        return urljoin(server, detail_path % self.version)


releases = map(Release, [
    '0.1',
    '0.2',
    '0.3',
    '0.3.1',
    '0.4',
    '0.5',
    '0.5.1',
    '0.5.2',
    '0.6',
    '0.6.1',
    '0.7',
    '0.7.1',
    '0.7.2',
    '0.8',
    '0.8.1',
    '0.9',
    '0.10',
    '0.10.1',
    '0.11',
    '0.11.1',
    '0.12',
    '0.12.1',
    '0.12.2',
    '0.12.3',
    '0.12.4',
    '1.0',
    '1.0.1',
    '1.0.2',
])

# -*- coding: utf-8 -*-
from urlparse import urlparse
from flask import Markup


class Project(object):
    def __init__(self, name, url, description, source=None):
        self.name = name
        self.url = url
        self.description = Markup(description)
        self.source = source

    @property
    def host(self):
        if self.url is not None:
            return urlparse(self.url)[1]

    @property
    def sourcehost(self):
        if self.source is not None:
            return urlparse(self.source)[1]

    def to_json(self):
        rv = vars(self).copy()
        rv['description'] = unicode(rv['description'])
        return rv


projects = {
    'websites': [
        Project('Flask Website', 'http://flask.pocoo.org/', '''
            <p>
              The website of the Flask microframework itself including the
              mailinglist interface, snippet archive and extension registry.
        '''),
        Project('Brightonpy', 'http://brightonpy.org/', '''
            <p>
              The website of the Brighton Python User Group
        ''', source='http://github.com/j4mie/brightonpy.org/'),
        Project(u's h o r e … software development', 'http://shore.be/', '''
            <p>Corporate website of Shore Software Development.
        '''),
        Project(u'ROCKYOU.fm', 'https://www.rockyou.fm/', '''
            <p>
              ROCKYOU.fm is a german internet radio station and webzine
              featuring mostly metal and hard rock. Since 2012 the DJs and
              reporters provide their listeners with news, reviews, feature
              shows and interviews.
        '''),
        Project(u'MetalSpy', 'https://www.metalspy.de/', '''
            <p>
              MetalSpy.de is the portfolio website of a german hobby
              photographer featuring mainly photos of metal bands,
              festivals, fantasy conventions and cosplay.
        '''),
        Project('ThadeusB\'s Website', 'http://thadeusb.com/', u'''
            <p>
              Personal website of ThadeusB.
        '''),
        Project('Blueslug', 'http://blueslug.com/', u'''
            <p>
              A flask-powered anti-social delicious clone
        '''),
        Project('DotShare', 'http://dotshare.it/', u'''
            <p>
              Socially driven website for sharing Linux/Unix dot files.
        '''),
        Project(
            'sopython', 'http://sopython.com/',
            '<p>Site of the Python chat room on Stack Overflow. '
            'Includes OAuth authentication, a wiki, and a growing, '
            'searchable list of "canonical" answers to Python '
            'questions on SO.</p>',
            source='https://github.com/sopython/sopython-site'
        )
    ],
    'apps': [
        Project('hg-review', None, '''
            <p>
              hg-review is a code review system for Mercurial.  It is available
              GPL2 license.
        ''', source='http://bitbucket.org/sjl/hg-review/'),
        Project('Ryshcate', None, '''
            <p>
              Ryshcate is a Flask powered pastebin with sourcecode
              available.
        ''', source='http://bitbucket.org/leafstorm/ryshcate/'),
        Project(u'Übersuggest Keyword Suggestion Tool', None, u'''
            <p>
              Übersuggest is a free tool that exploit the Google
              suggest JSON API to get keyword ideas for your search marketing
              campaign (PPC or SEO).
        ''', source='http://bitbucket.org/esaurito/ubersuggest'),
        Project('Have they emailed me?', None, '''
            <p>
              A mini-site for checking Google's GMail feed with Oauth.
        ''', source='http://github.com/lincolnloop/emailed-me'),
        Project('Remar.kZ', None, '''
            <p>
               Sometimes you use someone else's computer and find something
               neat and interesting.  Store it on Remar.kZ without having
               to enter your credentials.
        ''', source='http://bitbucket.org/little_arhat/remarkz'),
        Project('Domination', None, u'''
            <p>
              Domination is a clone of a well-known card game.
        ''', source='https://bitbucket.org/xoraxax/domination/'),
        Project('jitviewer', None, '''
            <p>
              web-based tool to inspect the output of PyPy JIT log
        ''', source='https://bitbucket.org/pypy/jitviewer'),
        Project('blohg', 'http://blohg.org/', '''
            <p>
              A mercurial based blog engine.
        ''', source='https://github.com/rafaelmartins/blohg'),
        Project('pidsim-web', None, '''
            <p>
              PID Controller simulator.
        ''', source='https://github.com/rafaelmartins/pidsim-web'),
        Project('HTTPBin', 'http://httpbin.org/', u'''
            <p>
              An HTTP request & response service.
        ''', source='https://github.com/kennethreitz/httpbin'),
        Project('Flask-Pastebin', None, u'''
            <p>
              Pastebin app with Flask and a few extensions that does Facebook
              connect as well as realtime push notifications with socket.io
              and juggernaut.
        ''', source='https://github.com/mitsuhiko/flask-pastebin'),
        Project('newsmeme', None, u'''
            <p>
              A hackernews/reddit clone written with Flask and
              various Flask extensions.
        ''', source='https://bitbucket.org/danjac/newsmeme'),
        Project('Indico', 'https://getindico.io/', u'''
            <p>
              Indico is a full-fledged meeting and conference management
              system developed at CERN. It includes advanced features such
              as integration with collaborative systems, a plugin system
              and support for SSO-based authentication.
        ''', source='https://github.com/indico/indico/'),
        Project('SayHello', 'http://sayhello.helloflask.com', u'''
            <p>
              A simple message board.
        ''', source='https://github.com/greyli/sayhello'),
        Project('Bluelog', 'http://bluelog.helloflask.com', u'''
            <p>
              A blog engine that supports category and resource management.
        ''', source='https://github.com/greyli/bluelog'),
        Project('Albumy', 'http://albumy.helloflask.com', u'''
            <p>
              A full-featured photo-sharing social networking.
        ''', source='https://github.com/greyli/albumy'),
        Project('Todoism', 'http://todoism.helloflask.com', u'''
            <p>
              A to-do application implements as SPA, it supports 
              i18n (Flask-Babel) and provides web APIs.
        ''', source='https://github.com/greyli/todoism'),
        Project('CatChat', 'http://catchat.helloflask.com', u'''
            <p>
              A chat room based on WebSocket (Flask-Socket-IO), fetured 
              with Markdown support and code syntax highlighting.
        ''', source='https://github.com/greyli/catchat'),
    ]

}

# order projects by name
for _category in projects.itervalues():
    _category.sort(key=lambda x: x.name.lower())
del _category

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
     ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

from werkzeug import cached_property, http_date

from flask import url_for, Markup
from flask_website import app, search

engine = create_engine(app.config['DATABASE_URI'],
                       convert_unicode=True,
                       **app.config['DATABASE_CONNECT_OPTIONS'])
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()


class User(Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    openid = Column('openid', String(200))
    name = Column(String(200))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid

    def to_json(self):
        return dict(name=self.name, is_admin=self.is_admin)

    @property
    def is_admin(self):
        return self.openid in app.config['ADMINS']

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Category(Model):
    __tablename__ = 'categories'
    id = Column('category_id', Integer, primary_key=True)
    name = Column(String(50))
    slug = Column(String(50))

    def __init__(self, name):
        self.name = name
        self.slug = '-'.join(name.split()).lower()

    def to_json(self):
        return dict(name=self.name, slug=self.slug, count=self.count)

    @cached_property
    def count(self):
        return self.snippets.count()

    @property
    def url(self):
        return url_for('snippets.category', slug=self.slug)


class Snippet(Model, search.Indexable):
    __tablename__ = 'snippets'
    id = Column('snippet_id', Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.user_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    title = Column(String(200))
    body = Column(String)
    pub_date = Column(DateTime)

    author = relation(User, backref=backref('snippets', lazy='dynamic'))
    category = relation(Category, backref=backref('snippets', lazy='dynamic'))

    search_document_kind = 'snippet'

    def __init__(self, author, title, body, category):
        self.author = author
        self.title = title
        self.body = body
        self.category = category
        self.pub_date = datetime.utcnow()

    def to_json(self):
        return dict(id=self.id, title=self.title,
                    body=unicode(self.rendered_body),
                    pub_date=http_date(self.pub_date),
                    comments=[c.to_json() for c in self.comments],
                    author=self.author.to_json(),
                    category=self.category.slug)

    def get_search_document(self):
        return dict(
            id=unicode(self.id),
            title=self.title,
            keywords=[self.category.name],
            content=self.body
        )

    @classmethod
    def describe_search_result(cls, result):
        obj = cls.query.get(int(result['id']))
        if obj is not None:
            text = obj.rendered_body.striptags()
            return Markup(result.highlights('content', text=text)) or None

    @property
    def url(self):
        return url_for('snippets.show', id=self.id)

    @property
    def rendered_body(self):
        from flask_website.utils import format_creole
        return format_creole(self.body)


class Comment(Model):
    __tablename__ = 'comments'
    id = Column('comment_id', Integer, primary_key=True)
    snippet_id = Column(Integer, ForeignKey('snippets.snippet_id'))
    author_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String(200))
    text = Column(String)
    pub_date = Column(DateTime)

    snippet = relation(Snippet, backref=backref('comments', lazy=True))
    author = relation(User, backref=backref('comments', lazy='dynamic'))

    def __init__(self, snippet, author, title, text):
        self.snippet = snippet
        self.author = author
        self.title = title
        self.text = text
        self.pub_date = datetime.utcnow()

    def to_json(self):
        return dict(author=self.author.to_json(),
                    title=self.title,
                    pub_date=http_date(self.pub_date),
                    text=unicode(self.rendered_text))

    @property
    def rendered_text(self):
        from flask_website.utils import format_creole
        return format_creole(self.text)


class OpenIDAssociation(Model):
    __tablename__ = 'openid_associations'
    id = Column('association_id', Integer, primary_key=True)
    server_url = Column(String(1024))
    handle = Column(String(255))
    secret = Column(String(255))
    issued = Column(Integer)
    lifetime = Column(Integer)
    assoc_type = Column(String(64))


class OpenIDUserNonce(Model):
    __tablename__ = 'openid_user_nonces'
    id = Column('user_nonce_id', Integer, primary_key=True)
    server_url = Column(String(1024))
    timestamp = Column(Integer)
    salt = Column(String(40))


event.listen(db_session, 'after_flush', search.update_model_based_indexes)

from datetime import datetime
from flask import Flask, session, g, render_template
from flask_openid import OpenID

app = Flask(__name__)
app.config.from_object('websiteconfig')

from flask_website.openid_auth import DatabaseOpenIDStore
oid = OpenID(app, store_factory=DatabaseOpenIDStore)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.before_request
def load_current_user():
    g.user = User.query.filter_by(openid=session['openid']).first() \
        if 'openid' in session else None


@app.teardown_request
def remove_db_session(exception):
    db_session.remove()


@app.context_processor
def current_year():
    return {'current_year': datetime.utcnow().year}


app.add_url_rule('/docs/', endpoint='docs.index', build_only=True)
app.add_url_rule('/docs/<path:page>/', endpoint='docs.show',
                 build_only=True)
app.add_url_rule('/docs/<version>/.latex/Flask.pdf', endpoint='docs.pdf',
                 build_only=True)

from flask_website.views import general
from flask_website.views import community
from flask_website.views import mailinglist
from flask_website.views import snippets
from flask_website.views import extensions
app.register_blueprint(general.mod)
app.register_blueprint(community.mod)
app.register_blueprint(mailinglist.mod)
app.register_blueprint(snippets.mod)
app.register_blueprint(extensions.mod)

from flask_website.database import User, db_session
from flask_website import utils

app.jinja_env.filters['datetimeformat'] = utils.format_datetime
app.jinja_env.filters['dateformat'] = utils.format_date
app.jinja_env.filters['timedeltaformat'] = utils.format_timedelta
app.jinja_env.filters['displayopenid'] = utils.display_openid

# -*- coding: utf-8 -*-
import os
import re
from flask import url_for, Markup
from flask_website import app
from flask_website.search import Indexable

_doc_body_re = re.compile(r'''(?smx)
    <title>(.*?)</title>.*?
    <div.*?class=".*?body.*?>(.*)
    <div.*?class=".*?sphinxsidebar
''')


class DocumentationPage(Indexable):
    search_document_kind = 'documentation'

    def __init__(self, slug):
        self.slug = slug
        fn = os.path.join(app.config['DOCUMENTATION_PATH'],
                          slug, 'index.html')
        with open(fn) as f:
            contents = f.read().decode('utf-8')
            title, text = _doc_body_re.search(contents).groups()
        self.title = Markup(title).striptags().split(u'—')[0].strip()
        self.text = Markup(text).striptags().strip().replace(u'¶', u'')

    def get_search_document(self):
        return dict(
            id=unicode(self.slug),
            title=self.title,
            keywords=[],
            content=self.text
        )

    @property
    def url(self):
        return url_for('docs.show', page=self.slug)

    @classmethod
    def describe_search_result(cls, result):
        rv = cls(result['id'])
        return Markup(result.highlights('content', text=rv.text)) or None

    @classmethod
    def iter_pages(cls):
        base_folder = os.path.abspath(app.config['DOCUMENTATION_PATH'])
        for dirpath, dirnames, filenames in os.walk(base_folder):
            if 'index.html' in filenames:
                slug = dirpath[len(base_folder) + 1:]
                # skip the index page.  useless
                if slug:
                    yield DocumentationPage(slug)

import re
import creoleparser
from datetime import datetime, timedelta
from genshi import builder
from functools import wraps
from creoleparser.elements import PreBlock
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound
from flask import g, url_for, flash, abort, request, redirect, Markup
from flask_website.flaskystyle import FlaskyStyle # same as docs


pygments_formatter = HtmlFormatter(style=FlaskyStyle)

_ws_split_re = re.compile(r'(\s+)')


TIMEDELTA_UNITS = (
    ('year',   3600 * 24 * 365),
    ('month',  3600 * 24 * 30),
    ('week',   3600 * 24 * 7),
    ('day',    3600 * 24),
    ('hour',   3600),
    ('minute', 60),
    ('second', 1)
)


class CodeBlock(PreBlock):

    def __init__(self):
        super(CodeBlock, self).__init__('pre', ['{{{', '}}}'])

    def _build(self, mo, element_store, environ):
        lines = self.regexp2.sub(r'\1', mo.group(1)).splitlines()
        if lines and lines[0].startswith('#!'):
            try:
                lexer = get_lexer_by_name(lines.pop(0)[2:].strip())
            except ClassNotFound:
                pass
            else:
                return Markup(highlight(u'\n'.join(lines), lexer,
                                        pygments_formatter))
        return builder.tag.pre(u'\n'.join(lines))


custom_dialect = creoleparser.create_dialect(creoleparser.creole10_base)
# hacky way to get rid of image support
custom_dialect.img = custom_dialect.no_wiki
custom_dialect.pre = CodeBlock()


_parser = creoleparser.Parser(
    dialect=custom_dialect,
    method='html'
)


def format_creole(text):
    return Markup(_parser.render(text, encoding=None))


def split_lines_wrapping(text, width=74, threshold=82):
    lines = text.splitlines()
    if all(len(line) <= threshold for line in lines):
        return lines
    result = []
    for line in lines:
        if len(line) <= threshold:
            result.append(line)
            continue
        line_width = 0
        line_buffer = []
        for piece in _ws_split_re.split(line):
            line_width += len(piece)
            if line_width > width:
                result.append(u''.join(line_buffer))
                line_buffer = []
                if not piece.isspace():
                    line_buffer.append(piece)
                    line_width = len(piece)
                else:
                    line_width = 0
            else:
                line_buffer.append(piece)
        if line_buffer:
            result.append(u''.join(line_buffer))
    return result


def request_wants_json():
    # we only accept json if the quality of json is greater than the
    # quality of text/html because text/html is preferred to support
    # browsers that accept on */*
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
       request.accept_mimetypes[best] > request.accept_mimetypes['text/html']


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('general.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.is_admin:
            abort(401)
        return f(*args, **kwargs)
    return requires_login(decorated_function)


def format_datetime(dt):
    return dt.strftime('%Y-%m-%d @ %H:%M')


def format_date(dt):
    return dt.strftime('%Y-%m-%d')


def format_timedelta(delta, granularity='second', threshold=.85):
    if isinstance(delta, datetime):
        delta = datetime.utcnow() - delta
    if isinstance(delta, timedelta):
        seconds = int((delta.days * 86400) + delta.seconds)
    else:
        seconds = delta

    for unit, secs_per_unit in TIMEDELTA_UNITS:
        value = abs(seconds) / secs_per_unit
        if value >= threshold or unit == granularity:
            if unit == granularity and value > 0:
                value = max(1, value)
            value = int(round(value))
            rv = u'%s %s' % (value, unit)
            if value != 1:
                rv += u's'
            return rv
    return u''


def display_openid(openid):
    if not openid:
        return ''
    rv = openid
    if rv.startswith(('http://', 'https://')):
        rv = rv.split('/', 2)[-1]
    return rv.rstrip('/')

from time import time

from openid.association import Association
from openid.store.interface import OpenIDStore
from openid.store import nonce

from flask_website.database import db_session, OpenIDAssociation, \
     OpenIDUserNonce


class DatabaseOpenIDStore(OpenIDStore):
    """Implements the open store for the website using the database."""

    def storeAssociation(self, server_url, association):
        assoc = OpenIDAssociation(
            server_url=server_url,
            handle=association.handle,
            secret=association.secret.encode('base64'),
            issued=association.issued,
            lifetime=association.lifetime,
            assoc_type=association.assoc_type
        )
        db_session.add(assoc)
        db_session.commit()

    def getAssociation(self, server_url, handle=None):
        q = OpenIDAssociation.query.filter_by(server_url=server_url)
        if handle is not None:
            q = q.filter_by(handle=handle)
        result_assoc = None
        for item in q.all():
            assoc = Association(item.handle, item.secret.decode('base64'),
                                item.issued, item.lifetime, item.assoc_type)
            if assoc.getExpiresIn() <= 0:
                self.removeAssociation(server_url, assoc.handle)
            else:
                result_assoc = assoc
        return result_assoc

    def removeAssociation(self, server_url, handle):
        try:
            return OpenIDAssociation.query.filter(
                (OpenIDAssociation.server_url == server_url) &
                (OpenIDAssociation.handle == handle)
            ).delete()
        finally:
            db_session.commit()

    def useNonce(self, server_url, timestamp, salt):
        if abs(timestamp - time()) > nonce.SKEW:
            return False
        rv = OpenIDUserNonce.query.filter(
            (OpenIDUserNonce.server_url == server_url) &
            (OpenIDUserNonce.timestamp == timestamp) &
            (OpenIDUserNonce.salt == salt)
        ).first()
        if rv is not None:
            return False
        rv = OpenIDUserNonce(server_url=server_url, timestamp=timestamp,
                             salt=salt)
        db_session.add(rv)
        db_session.commit()
        return True

    def cleanupNonces(self):
        try:
            return OpenIDUserNonce.query.filter(
                OpenIDUserNonce.timestamp <= int(time() - nonce.SKEW)
            ).delete()
        finally:
            db_session.commit()

    def cleanupAssociations(self):
        try:
            return OpenIDAssociation.query.filter(
                OpenIDAssociation.lifetime < int(time())
            ).delete()
        finally:
            db_session.commit()

# -*- coding: utf-8 -*-
import os
from whoosh import highlight, analysis, qparser
from whoosh.support.charset import accent_map
from flask import Markup
from flask_website import app
from werkzeug import import_string


def open_index():
    from whoosh import index, fields as f
    if os.path.isdir(app.config['WHOOSH_INDEX']):
        return index.open_dir(app.config['WHOOSH_INDEX'])
    os.mkdir(app.config['WHOOSH_INDEX'])
    analyzer = analysis.StemmingAnalyzer() | analysis.CharsetFilter(accent_map)
    schema = f.Schema(
        url=f.ID(stored=True, unique=True),
        id=f.ID(stored=True),
        title=f.TEXT(stored=True, field_boost=2.0, analyzer=analyzer),
        type=f.ID(stored=True),
        keywords=f.KEYWORD(commas=True),
        content=f.TEXT(analyzer=analyzer)
    )
    return index.create_in(app.config['WHOOSH_INDEX'], schema)


index = open_index()


class Indexable(object):
    search_document_kind = None

    def add_to_search_index(self, writer):
        writer.add_document(url=unicode(self.url),
                            type=self.search_document_type,
                            **self.get_search_document())

    @classmethod
    def describe_search_result(cls, result):
        return None

    @property
    def search_document_type(self):
        cls = type(self)
        return cls.__module__ + u'.' + cls.__name__

    def get_search_document(self):
        raise NotImplementedError()

    def remove_from_search_index(self, writer):
        writer.delete_by_term('url', unicode(self.url))


def highlight_all(result, field):
    text = result[field]
    return Markup(highlight.Highlighter(
        fragmenter=highlight.WholeFragmenter(),
        formatter=result.results.highlighter.formatter)
            .highlight_hit(result, field, text=text)) or text


class SearchResult(object):

    def __init__(self, result):
        self.url = result['url']
        self.title_text = result['title']
        self.title = highlight_all(result, 'title')
        cls = import_string(result['type'])
        self.kind = cls.search_document_kind
        self.description = cls.describe_search_result(result)


class SearchResultPage(object):

    def __init__(self, results, page):
        self.page = page
        if results is None:
            self.results = []
            self.pages = 1
            self.total = 0
        else:
            self.results = [SearchResult(r) for r in results]
            self.pages = results.pagecount
            self.total = results.total

    def __iter__(self):
        return iter(self.results)


def search(query, page=1, per_page=20):
    with index.searcher() as s:
        qp = qparser.MultifieldParser(['title', 'content'], index.schema)
        q = qp.parse(unicode(query))
        try:
            result_page = s.search_page(q, page, pagelen=per_page)
        except ValueError:
            if page == 1:
                return SearchResultPage(None, page)
            return None
        results = result_page.results
        results.highlighter.fragmenter.maxchars = 512
        results.highlighter.fragmenter.surround = 40
        results.highlighter.formatter = highlight.HtmlFormatter('em',
            classname='search-match', termclass='search-term',
            between=u'<span class=ellipsis> … </span>')
        return SearchResultPage(result_page, page)


def update_model_based_indexes(session, flush_context):
    """Called by a session event, updates the model based documents."""
    to_delete = []
    to_add = []
    for model in session.new:
        if isinstance(model, Indexable):
            to_add.append(model)

    for model in session.dirty:
        if isinstance(model, Indexable):
            to_delete.append(model)
            to_add.append(model)

    for model in session.dirty:
        if isinstance(model, Indexable):
            to_delete.append(model)

    if not (to_delete or to_add):
        return

    writer = index.writer()
    for model in to_delete:
        model.remove_from_search_index(writer)
    for model in to_add:
        model.add_to_search_index(writer)
    writer.commit()


def update_documentation_index():
    from flask_website.docs import DocumentationPage
    writer = index.writer()
    for page in DocumentationPage.iter_pages():
        page.remove_from_search_index(writer)
        page.add_to_search_index(writer)
    writer.commit()


def reindex_snippets():
    from flask_website.database import Snippet
    writer = index.writer()
    for snippet in Snippet.query.all():
        snippet.remove_from_search_index(writer)
        snippet.add_to_search_index(writer)
    writer.commit()


from __future__ import with_statement
from flask import Blueprint, render_template, redirect


mod = Blueprint('mailinglist', __name__, url_prefix='/mailinglist')


@mod.route('/')
def index():
    return render_template('mailinglist/index.html')


@mod.route('/archive/', defaults={'page': 1})
@mod.route('/archive/page/<int:page>/')
def archive(page):
    return redirect('http://librelist.com/browser/flask/')


@mod.route('/archive/<int:year>/<int:month>/<int:day>/<slug>/')
def show_thread(year, month, day, slug):
    return redirect('http://librelist.com/browser/flask/%s/%s/%s/%s'
                    % (year, month, day, slug))

from flask import Blueprint, render_template, jsonify, redirect, \
     url_for
from flask_website.utils import request_wants_json
from flask_website.listings.extensions import extensions, unlisted

mod = Blueprint('extensions', __name__, url_prefix='/extensions')


@mod.route('/')
def index():
    if request_wants_json():
        return jsonify(extensions=[ext.to_json() for ext in extensions],
                       unlisted_extensions=[ext.to_json() for ext in unlisted])
    return render_template('extensions/index.html', extensions=extensions)


@mod.route('/creating/')
def creating():
    return redirect(url_for('docs.show', page='extensiondev'), 301)

from flask import Blueprint, render_template, jsonify
from flask_website.utils import request_wants_json
from flask_website.listings.projects import projects

mod = Blueprint('community', __name__, url_prefix='/community')


@mod.route('/')
def index():
    return render_template('community/index.html')


@mod.route('/irc/')
def irc():
    return render_template('community/irc.html')


@mod.route('/badges/')
def badges():
    return render_template('community/badges.html')


@mod.route('/poweredby/')
def poweredby():
    if request_wants_json():
        return jsonify((k, [p.to_json() for p in v])
                       for k, v in projects.iteritems())
    return render_template('community/poweredby.html', projects=projects)


@mod.route('/logos/')
def logos():
    return render_template('community/logos.html')

# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
    render_template, request, url_for

from flask_website.utils import format_creole, request_wants_json, \
    requires_admin, requires_login
from flask_website.database import Category, Comment, Snippet, db_session

mod = Blueprint('snippets', __name__, url_prefix='/snippets')


@mod.route('/')
def index():
    return render_template('snippets/index.html',
        categories=Category.query.order_by(Category.name).all())


@mod.route('/<int:id>/', methods=['GET', 'POST'])
def show(id):
    snippet = Snippet.query.get(id)
    if snippet is None:
        abort(404)
    if request_wants_json():
        return jsonify(snippet=snippet.to_json())
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if text:
            db_session.add(Comment(snippet, g.user, title, text))
            db_session.commit()
            flash(u'Your comment was added')
            return redirect(snippet.url)
    return render_template('snippets/show.html', snippet=snippet)


@mod.route('/comments/<int:id>/', methods=['GET', 'POST'])
@requires_admin
def edit_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    snippet = comment.snippet
    form = dict(title=comment.title, text=comment.text)
    if request.method == 'POST':
        if 'delete' in request.form:
            db_session.delete(comment)
            db_session.commit()
            flash(u'Comment was deleted.')
            return redirect(snippet.url)
        elif 'cancel' in request.form:
            return redirect(snippet.url)
        form['title'] = request.form['title']
        form['text'] = request.form['text']
        if not form['text']:
            flash(u'Error: comment text is required.')
        else:
            comment.title = form['title']
            comment.text = form['text']
            db_session.commit()
            flash(u'Comment was updated.')
            return redirect(snippet.url)
    return render_template('snippets/edit_comment.html', form=form,
                           comment=comment)


@mod.route('/edit/<int:id>/', methods=['GET', 'POST'])
@requires_login
def edit(id):
    snippet = Snippet.query.get(id)
    if snippet is None:
        abort(404)
    if g.user is None or (not g.user.is_admin and snippet.author != g.user):
        abort(401)
    preview = None
    form = dict(title=snippet.title, body=snippet.body,
                category=snippet.category.id)
    if request.method == 'POST':
        form['title'] = request.form['title']
        form['body'] = request.form['body']
        form['category'] = request.form.get('category', type=int)
        if 'preview' in request.form:
            preview = format_creole(request.form['body'])
        elif 'delete' in request.form:
            for comment in snippet.comments:
                db_session.delete(comment)
            db_session.delete(snippet)
            db_session.commit()
            flash(u'Your snippet was deleted')
            return redirect(url_for('snippets.index'))
        else:
            category_id = request.form.get('category', type=int)
            if not form['body']:
                flash(u'Error: you have to enter a snippet')
            else:
                category = Category.query.get(category_id)
                if category is not None:
                    snippet.title = form['title']
                    snippet.body = form['body']
                    snippet.category = category
                    db_session.commit()
                    flash(u'Your snippet was modified')
                    return redirect(snippet.url)
    return render_template('snippets/edit.html',
        snippet=snippet, preview=preview, form=form,
        categories=Category.query.order_by(Category.name).all())


@mod.route('/category/<slug>/')
def category(slug):
    category = Category.query.filter_by(slug=slug).first()
    if category is None:
        abort(404)
    snippets = category.snippets.order_by(Snippet.title).all()
    if request_wants_json():
        return jsonify(category=category.to_json(),
                       snippets=[s.id for s in snippets])
    return render_template('snippets/category.html', category=category,
                           snippets=snippets)

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
from flask_openid import COMMON_PROVIDERS
from flask_website import oid
from flask_website.search import search as perform_search
from flask_website.utils import requires_login, request_wants_json
from flask_website.database import db_session, User
from flask_website.listings.releases import releases

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    if request_wants_json():
        return jsonify(releases=[r.to_json() for r in releases])

    return render_template(
        'general/index.html',
        latest_release=releases[-1],
        # pdf link does not redirect, needs version
        # docs version only includes major.minor
        docs_pdf_version='.'.join(releases[-1].version.split('.', 2)[:2])
    )


@mod.route('/search/')
def search():
    q = request.args.get('q') or ''
    page = request.args.get('page', type=int) or 1
    results = None
    if q:
        results = perform_search(q, page=page)
        if results is None:
            abort(404)
    return render_template('general/search.html', results=results, q=q)


@mod.route('/logout/')
def logout():
    if 'openid' in session:
        flash(u'Logged out')
        del session['openid']
    return redirect(request.referrer or url_for('general.index'))


@mod.route('/login/', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(url_for('general.index'))
    if 'cancel' in request.form:
        flash(u'Cancelled. The OpenID was not changed.')
        return redirect(oid.get_next_url())
    openid = request.values.get('openid')
    if not openid:
        openid = COMMON_PROVIDERS.get(request.args.get('provider'))
    if openid:
        return oid.try_login(openid, ask_for=['fullname', 'nickname'])
    error = oid.fetch_error()
    if error:
        flash(u'Error: ' + error)
    return render_template('general/login.html', next=oid.get_next_url())


@mod.route('/first-login/', methods=['GET', 'POST'])
def first_login():
    if g.user is not None or 'openid' not in session:
        return redirect(url_for('.login'))
    if request.method == 'POST':
        if 'cancel' in request.form:
            del session['openid']
            flash(u'Login was aborted')
            return redirect(url_for('general.login'))
        db_session.add(User(request.form['name'], session['openid']))
        db_session.commit()
        flash(u'Successfully created profile and logged in')
        return redirect(oid.get_next_url())
    return render_template('general/first_login.html',
                           next=oid.get_next_url(),
                           openid=session['openid'])


@mod.route('/profile/', methods=['GET', 'POST'])
@requires_login
def profile():
    name = g.user.name
    if request.method == 'POST':
        name = request.form['name'].strip()
        if not name:
            flash(u'Error: a name is required')
        else:
            g.user.name = name
            db_session.commit()
            flash(u'User profile updated')
            return redirect(url_for('.index'))
    return render_template('general/profile.html', name=name)


@mod.route('/profile/change-openid/', methods=['GET', 'POST'])
@requires_login
@oid.loginhandler
def change_openid():
    if request.method == 'POST':
        if 'cancel' in request.form:
            flash(u'Cancelled. The OpenID was not changed.')
            return redirect(oid.get_next_url())
    openid = request.values.get('openid')
    if not openid:
        openid = COMMON_PROVIDERS.get(request.args.get('provider'))
    if openid:
        return oid.try_login(openid)
    error = oid.fetch_error()
    if error:
        flash(u'Error: ' + error)
    return render_template('general/change_openid.html',
                           next=oid.get_next_url())


@oid.after_login
def create_or_login(resp):
    session['openid'] = resp.identity_url
    user = g.user or User.query.filter_by(openid=resp.identity_url).first()
    if user is None:
        return redirect(url_for('.first_login', next=oid.get_next_url(),
                                name=resp.fullname or resp.nickname))
    if user.openid != resp.identity_url:
        user.openid = resp.identity_url
        db_session.commit()
        flash(u'OpenID identity changed')
    else:
        flash(u'Successfully signed in')
    return redirect(oid.get_next_url())

