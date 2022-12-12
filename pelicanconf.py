AUTHOR = 'Zac Bir'
SITENAME = 'Neverending Pretending'
SITEURL = 'http://localhost:8080'
PORT = 8080

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

MENUITEMS = (
    ('Mastodon', 'https://dice.camp/@zacbir'),
    ('Itch.io', 'https://zacbir.itch.io'),
    ('Archives', '/archives.html')
)

# Social widget
SOCIAL = ()

SUMMARY_MAX_LENGTH = None

DEFAULT_PAGINATION = False

CATEGORIES = ()

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = 'zacbir-Kiera'

# PLUGIN_PATHS = ['/Users/zbir/Dev/zacbir.net/pelican-plugins']
PLUGINS = ['liquid_tags', 'search', 'neighbors', 'simple_footnotes']

LIQUID_TAGS = ["img"]

DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'static', '.well-known']

EXTRA_HEADER = '<link rel="me" href="https://dice.camp/@zacbir">'

COPYRIGHT = '2022'
