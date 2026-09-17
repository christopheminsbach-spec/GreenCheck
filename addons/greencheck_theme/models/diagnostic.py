from odoo import models, fields


class PlantDiagnostic(models.Model):
    _name = "plant.diagnostic"
    _description = "Diagnostic de plante GreenCheck"

    name = fields.Char(
        string="Nom du diagnostic",
        required=True,
        default="Nouveau diagnostic"
    )

    date_diagnostic = fields.Datetime(
        string="Date du diagnostic",
        default=fields.Datetime.now
    )

    state = fields.Selection(
        [
            ("draft", "Nouveau"),
            ("analyzing", "En analyse"),
            ("done", "Terminé"),
        ],
        string="État",
        default="draft",
        required=True
    )

    image = fields.Image(
        string="Photo de la plante"
    )

    ai_result = fields.Text(
        string="Résultat de l'analyse IA"
    )

    ai_confidence = fields.Float(
        string="Confiance IA"
    )

    recommendations = fields.Text(
        string="Recommandations"
    )

    def action_start_analysis(self):
        for diagnostic in self:
            diagnostic.state = "analyzing"

    def action_simulate_analysis(self):
        for diagnostic in self:
            diagnostic.ai_result = (
                "Plante identifiée : Rosier\n"
                "État général : bonne santé"
            )

            diagnostic.ai_confidence = 0.92

            diagnostic.recommendations = (
                "Arroser modérément.\n"
                "Placer la plante dans un endroit lumineux.\n"
                "Surveiller l'apparition éventuelle de parasites."
            )

            diagnostic.state = "done"