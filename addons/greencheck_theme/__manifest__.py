{
    "name": "GreenCheck Theme",

    "version": "19.0.1.0",

    "category": "Website/Theme",

    "author": "GreenCheck",

    "license": "LGPL-3",

    "depends": [
        "website",
    ],

    "data": [
        "views/theme.xml",
        "views/homepage.xml",
        "views/header.xml",
        "views/diagnostic.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "greencheck_theme/static/src/css/greencheck.scss",
        ],
    },

    "theme": True,

    "application": True,

    "installable": True,
}