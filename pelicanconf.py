AUTHOR = 'QualiThree'
SITENAME = 'Getting Started With Dev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ('CreateCoders', 'https://createcoders.com/'),
    ('QualiThree', 'https://qualithree.com/'),
    ('WhatHashtag.com', 'https://whathashtag.com/'),
)

# Social widget
SOCIAL = (
    ('CreateCoders Instagram', 'https://instagram.com/createcoders'),
    ('CreateCoders Tiktok', 'https://www.tiktok.com/@createcoders'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Bootstrap Next Theme Config Below
THEME = 'theme/bootstrap-next/'

PYGMENTS_STYLE = 'monokai'
BOOTSTRAP_FLUID = True

# FAVICON = 'images/favicon.png'
# SITELOGO = 'images/my_site_logo.png'
# SITELOGO_SIZE = 400
# BANNER = '/path/to/banner.png'
# BANNER_SUBTITLE = 'This is my subtitle'
# BANNER_ALL_PAGES = True

HIDE_SITENAME = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
