from odoo import http
from odoo.http import request


class GreenCheckWebsite(http.Controller):

    @http.route(
        "/diagnostic",
        type="http",
        auth="public",
        website=True
    )
    def diagnostic(self):

        return request.render(
            "greencheck_theme.greencheck_diagnostic_page"
        )

    @http.route(
        "/diagnostic/upload",
        type="http",
        auth="public",
        methods=["POST"],
        csrf=False
    )
    def diagnostic_upload(self, **post):

        image = post.get("plant_image")

        if not image:
            return request.make_json_response({
                "success": False,
                "message": "Aucune image reçue"
            })

        # Création d'un diagnostic sans stocker l'image
        diagnostic = request.env["plant.diagnostic"].sudo().create({
            "name": "Diagnostic plante",
            "state": "draft",
        })

        state_label = dict(
            diagnostic._fields["state"].selection
        ).get(diagnostic.state)

        return request.make_json_response({
            "success": True,
            "filename": image.filename,
            "diagnostic_id": diagnostic.id,
            "state": diagnostic.state,
            "state_label": state_label,
        })

    @http.route(
        "/diagnostic/start",
        type="http",
        auth="public",
        methods=["POST"],
        csrf=False
    )
    def diagnostic_start(self, **post):

        diagnostic_id = post.get("diagnostic_id")

        if not diagnostic_id:
            return request.make_json_response({
                "success": False,
                "message": "Aucun diagnostic indiqué"
            })

        diagnostic = request.env["plant.diagnostic"].sudo().browse(
            int(diagnostic_id)
        )

        if not diagnostic.exists():
            return request.make_json_response({
                "success": False,
                "message": "Diagnostic introuvable"
            })

        diagnostic.action_start_analysis()

        state_label = dict(
            diagnostic._fields["state"].selection
        ).get(diagnostic.state)

        return request.make_json_response({
            "success": True,
            "diagnostic_id": diagnostic.id,
            "state": diagnostic.state,
            "state_label": state_label,
        })