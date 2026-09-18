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
        "security/ir.model.access.csv",
        "views/theme.xml",
        "views/homepage.xml",
        "views/header.xml",
        "views/diagnostic.xml",
        "views/footer.xml",
        "views/fonctionnement.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "greencheck_theme/static/src/css/greencheck.scss",
            "greencheck_theme/static/src/css/diagnostic.scss",
            "greencheck_theme/static/src/css/footer.scss",
        ],
    },

    "theme": True,

    "application": True,

    "installable": True,
}