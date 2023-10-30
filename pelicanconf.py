AUTHOR = 'QualiThree'
SITENAME = 'Getting Started With AI'
SITEURL = ''  # When clicking the title

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ('index', 'blog')

PAGE_URL = 'topics/{slug}/'
PAGE_SAVE_AS = 'topics/{slug}/index.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}'
SITEMAP_SAVE_AS = 'sitemap.xml'

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
BOOTSTRAP_FLUID = False

# FAVICON = 'images/favicon.png'
# SITELOGO = 'images/my_site_logo.png'
# SITELOGO_SIZE = 400
# BANNER = '/path/to/banner.png'
# BANNER_SUBTITLE = 'This is my subtitle'
# BANNER_ALL_PAGES = True

BOOTSTRAP_THEME = 'lux'  # https://bootswatch.com/4/

HIDE_SITENAME = False
HIDE_SIDEBAR = True
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

CUSTOM_CSS = 'static/custom.css'