from odoo import http


class GreenCheckWebsite(http.Controller):

    @http.route(
        "/diagnostic-ia",
        type="http",
        auth="public",
        website=True
    )
    def diagnostic_ia(self):

        return http.request.render(
            "greencheck_theme.greencheck_diagnostic_page"
        )