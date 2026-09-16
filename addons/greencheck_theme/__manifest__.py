{
    "name": "GreenCheck Theme",

    "version": "19.0.1.0",

    "category": "Website/Theme",

    "depends": [
        "website",
        "web",
    ],

    "data": [
        "views/theme.xml",
        "views/header.xml",
        "views/homepage.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "greencheck_theme/static/src/scss/style.scss",
        ],
    },

    "theme": True,

    "application": True,

    "installable": True,
}