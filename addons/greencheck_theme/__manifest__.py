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
        "views/a_propos.xml",
        "views/contact.xml",
        "views/inscription.xml",
        "views/mon_espace.xml",
        "views/mon_espace_diagnostic.xml",
        "views/login.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "greencheck_theme/static/src/css/greencheck.scss",
            "greencheck_theme/static/src/css/diagnostic.scss",
            "greencheck_theme/static/src/css/footer.scss",
            "greencheck_theme/static/src/css/fonctionnement.scss",
            "greencheck_theme/static/src/css/a-propos.scss",
            "greencheck_theme/static/src/css/contact.scss",
            "greencheck_theme/static/src/css/homepage.scss",
            "greencheck_theme/static/src/css/mon-espace.scss",
            "greencheck_theme/static/src/css/inscription.scss",
            "greencheck_theme/static/src/css/login.scss",
            "greencheck_theme/static/src/js/main.js",
        ],
    },

    "theme": True,

    "application": True,

    "installable": True,
}