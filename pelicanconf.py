#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nekoo'
SITENAME = u'Yet another site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/bootstrap2"
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]

STATIC_PATHS = ["images", "pdfs"]
DEFAULT_DATE = 'fs'

PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = ('author',)
