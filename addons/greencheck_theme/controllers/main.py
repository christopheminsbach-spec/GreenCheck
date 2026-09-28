from odoo import http
from odoo.http import request
import base64


class GreenCheckWebsite(http.Controller):

    @http.route(
        "/diagnostic-ia",
        type="http",
        auth="public",
        website=True
    )
    def diagnostic(self):

        return request.render(
            "greencheck_theme.greencheck_diagnostic_page"
        )

    @http.route(
        "/fonctionnement",
        type="http",
        auth="public",
        website=True
    )
    def fonctionnement(self):

        return request.render(
            "greencheck_theme.greencheck_fonctionnement"
        )

    @http.route(
        "/a-propos",
        type="http",
        auth="public",
        website=True
    )
    def a_propos(self):

        return request.render(
            "greencheck_theme.greencheck_a_propos"
        )

    @http.route(
        "/contact",
        type="http",
        auth="public",
        website=True
    )
    def contact(self):

        return request.render(
            "greencheck_theme.greencheck_contact"
        )

    @http.route(
        "/inscription",
        type="http",
        auth="public",
        website=True
    )
    def inscription(self):

        return request.render(
            "greencheck_theme.greencheck_inscription"
        )

    @http.route(
        "/mon-espace",
        type="http",
        auth="user",
        website=True
    )
    def mon_espace(self):

        diagnostics = request.env["plant.diagnostic"].search(
            [
                ("user_id", "=", request.env.user.id)
            ],
            order="date_diagnostic desc"
        )

        return request.render(
            "greencheck_theme.greencheck_mon_espace",
            {
                "diagnostics": diagnostics,
            }
        )

    @http.route(
        "/mon-espace/diagnostic/<int:diagnostic_id>",
        type="http",
        auth="user",
        website=True
    )
    def mon_espace_diagnostic(self, diagnostic_id):

        diagnostic = request.env["plant.diagnostic"].search(
            [
                ("id", "=", diagnostic_id),
                ("user_id", "=", request.env.user.id)
            ],
            limit=1
        )

        if not diagnostic:
            return request.not_found()

        return request.render(
            "greencheck_theme.greencheck_mon_espace_diagnostic",
            {
                "diagnostic": diagnostic,
            }
        )

    @http.route(
        "/mon-espace/diagnostic/<int:diagnostic_id>/pdf",
        type="http",
        auth="user",
        website=True
    )
    def mon_espace_diagnostic_pdf(self, diagnostic_id):

        diagnostic = request.env["plant.diagnostic"].search(
            [
                ("id", "=", diagnostic_id),
                ("user_id", "=", request.env.user.id)
            ],
            limit=1
        )

        if not diagnostic:
            return request.not_found()

        report = request.env.ref(
            "greencheck_theme.action_report_diagnostic"
        )

        pdf_content, _ = report._render_qweb_pdf(
            report,
            res_ids=[diagnostic.id]
        )

        return request.make_response(
            pdf_content,
            headers=[
                ("Content-Type", "application/pdf"),
                (
                    "Content-Disposition",
                    'attachment; filename="diagnostic-greencheck-%s.pdf"'
                    % diagnostic.id,
                ),
            ],
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

        # Formats d'image autorisés
        allowed_mimetypes = {
            "image/jpeg",
            "image/png",
            "image/webp",
        }

        if image.content_type not in allowed_mimetypes:
            return request.make_json_response({
                "success": False,
                "message": (
                    "Format d'image non autorisé. "
                    "Utilisez JPG, PNG ou WEBP."
                )
            })

        # Limitation de la taille à 5 Mo
        max_image_size = 5 * 1024 * 1024

        # Lecture limitée à 5 Mo + 1 octet afin de détecter
        # immédiatement un fichier trop volumineux.
        image_data = image.stream.read(max_image_size + 1)

        if not image_data:
            return request.make_json_response({
                "success": False,
                "message": "L'image reçue est vide"
            })

        if len(image_data) > max_image_size:
            return request.make_json_response({
                "success": False,
                "message": (
                    "L'image est trop volumineuse. "
                    "La taille maximale est de 5 Mo."
                )
            })

        # Encodage de l'image
        image_base64 = base64.b64encode(image_data)

        # Validation des données du contexte
        max_context_length = 255

        plant_type = post.get("plant_type", "")
        location = post.get("location", "")
        exposure = post.get("exposure", "")

        context_values = {
            "plant_type": plant_type,
            "location": location,
            "exposure": exposure,
        }

        context_labels = {
            "plant_type": "Type de plante",
            "location": "Localisation",
            "exposure": "Exposition",
        }

        for field_name, field_value in context_values.items():
            if not isinstance(field_value, str):
                return request.make_json_response({
                    "success": False,
                    "message": (
                        "%s doit être une valeur textuelle."
                        % context_labels[field_name]
                    )
                })

        plant_type = plant_type.strip()
        location = location.strip()
        exposure = exposure.strip()

        context_fields = {
            "plant_type": plant_type,
            "location": location,
            "exposure": exposure,
        }

        context_labels = {
            "plant_type": "Type de plante",
            "location": "Localisation",
            "exposure": "Exposition",
        }

        for field_name, field_value in context_fields.items():
            if len(field_value) > max_context_length:
                return request.make_json_response({
                    "success": False,
                    "message": (
                        "%s ne peut pas dépasser 255 caractères."
                        % context_labels[field_name]
                    )
                })

        # Préparation des données du diagnostic
        diagnostic_values = {
            "name": "Diagnostic plante",
            "state": "draft",
            "image": image_base64,
            "plant_type": plant_type,
            "location": location,
            "exposure": exposure,
        }

        # Association au compte connecté
        public_user = request.env.ref("base.public_user")

        if request.env.user.id != public_user.id:
            diagnostic_values["user_id"] = request.env.user.id

        # Création du diagnostic
        diagnostic = request.env["plant.diagnostic"].sudo().create(
            diagnostic_values
        )

        # Mémorisation du diagnostic pour un visiteur public
        if request.env.user.id == public_user.id:
            request.session["greencheck_diagnostic_id"] = diagnostic.id

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

        try:
            diagnostic_id = int(diagnostic_id)
        except (TypeError, ValueError):
            return request.make_json_response({
                "success": False,
                "message": "Identifiant de diagnostic invalide"
            })

        diagnostic = request.env["plant.diagnostic"].sudo().browse(
            diagnostic_id
        )

        if not diagnostic.exists():
            return request.make_json_response({
                "success": False,
                "message": "Diagnostic introuvable"
            })

        # Contrôle d'accès au diagnostic
        public_user = request.env.ref("base.public_user")

        if request.env.user.id != public_user.id:
            if diagnostic.user_id.id != request.env.user.id:
                return request.make_json_response({
                    "success": False,
                    "message": "Accès au diagnostic non autorisé"
                })
        else:
            session_diagnostic_id = request.session.get(
                "greencheck_diagnostic_id"
            )

            if session_diagnostic_id != diagnostic.id:
                return request.make_json_response({
                    "success": False,
                    "message": "Accès au diagnostic non autorisé"
                })

        # Validation des données du contexte
        max_context_length = 255

        plant_type = post.get("plant_type", "")
        location = post.get("location", "")
        exposure = post.get("exposure", "")

        context_values = {
            "plant_type": plant_type,
            "location": location,
            "exposure": exposure,
        }

        context_labels = {
            "plant_type": "Type de plante",
            "location": "Localisation",
            "exposure": "Exposition",
        }

        for field_name, field_value in context_values.items():
            if not isinstance(field_value, str):
                return request.make_json_response({
                    "success": False,
                    "message": (
                        "%s doit être une valeur textuelle."
                        % context_labels[field_name]
                    )
                })

        plant_type = plant_type.strip()
        location = location.strip()
        exposure = exposure.strip()

        context_fields = {
            "plant_type": plant_type,
            "location": location,
            "exposure": exposure,
        }

        context_labels = {
            "plant_type": "Type de plante",
            "location": "Localisation",
            "exposure": "Exposition",
        }

        for field_name, field_value in context_fields.items():
            if len(field_value) > max_context_length:
                return request.make_json_response({
                    "success": False,
                    "message": (
                        "%s ne peut pas dépasser 255 caractères."
                        % context_labels[field_name]
                    )
                })

        # Mise à jour du contexte du diagnostic
        diagnostic.write({
            "plant_type": plant_type,
            "location": location,
            "exposure": exposure,
        })

        # Passage du diagnostic à l'état "En analyse"
        diagnostic.action_start_analysis()

        # Simulation de l'analyse IA
        diagnostic.action_simulate_analysis()

        state_label = dict(
            diagnostic._fields["state"].selection
        ).get(diagnostic.state)

        return request.make_json_response({
            "success": True,
            "diagnostic_id": diagnostic.id,
            "state": diagnostic.state,
            "state_label": state_label,
            "ai_result": diagnostic.ai_result,
            "ai_confidence": diagnostic.ai_confidence,
            "recommendations": diagnostic.recommendations,
        })