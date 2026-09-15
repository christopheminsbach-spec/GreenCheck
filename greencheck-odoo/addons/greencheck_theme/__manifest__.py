{
    "name": "GreenCheck Theme",
    "version": "19.0.1.0.0",
    "category": "Website",
    "summary": "GreenCheck AI website theme",

    "depends": [
        "website",
        "website_sale"
    ],

    "data": [
        "views/homepage.xml"
    ],

    "assets": {
        "web.assets_frontend": [
            "greencheck_theme/static/src/css/greencheck.scss",
            "greencheck_theme/static/src/js/main.js"
        ]
    },

    "theme": True,

    "installable": True,
    "application": False
}
