AUTHOR = 'LauriK'
SITENAME = 'Kanervoita'
SITESUBTITLE = "A personal blog."
SITEURL = ""
THEME = "/home/lauri/projects/latensivu/themes/pelican-chameleon"
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'
CATEGORY_URL = "{slug}.html"
CATEGORY_SAVE_AS = "{slug}.html"

TAG_URL = "tag/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"
# Change THIS theme
BS3_THEME = 'https://cdn.jsdelivr.net/npm/bootswatch@3.4.1/brite/bootstrap.min.css'
BS3_THEME_NAME = 'Brite'
BS3_THEME_HOMEPAGE = 'https://bootswatch.com/3/brite/'

PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images", "extra/favicon.ico", 'files']
ARTICLE_PATHS = ["articles"]
INDEX_SAVE_AS = "index.html"
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Koti', 'index.html'),
    ('Juttuja', [
        ('Ruoka & juoma', '/ruoka-juoma.html'),
        ('Tietotekniikka', '/tietotekniikka.html'),
        ('Kasvit', '/kasvit.html'),
        ('Muut projektit', '/muut-projektit.html'),
        ]),
    ('Arkisto', [
        ('Tagit', 'tags.html'),
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ]),       
    ('Linkit', [
        ('Email', 'mailto: lautakane@gmail.com'),
        ('CV', ''),
        ('GitHub', 'https://github.com/Callun4/'),
        ]),

    ]

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'fi'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
