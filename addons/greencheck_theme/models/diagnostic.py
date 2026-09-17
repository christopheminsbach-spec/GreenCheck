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