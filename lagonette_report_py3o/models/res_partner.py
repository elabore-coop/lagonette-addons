from odoo import fields, models
from datetime import datetime

class ResPartner(models.Model):
    _inherit = "res.partner"

    membership_current_year = fields.Char(
        'current membership year',
        compute='_compute_membership_current_year'
    )

    def _compute_membership_current_year(self):
        for partner in self:
            if partner.membership_last_start :
                partner.membership_current_year = str(partner.membership_last_start.year)
            else:
                partner.membership_current_year = False