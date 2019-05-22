# -*- coding: utf-8 -*-

from odoo import models, fields, api

class issues_leaves(models.Model):
    _inherit = 'hr.leave'

    days_before_approval = fields.Integer(string="Saldo de días antes de la aprobación")

    @api.onchange('holiday_status_id')
    def _onchange_days_before_approval(self):
        if self.holiday_status_id:
            self.days_before_approval = self.holiday_status_id.virtual_remaining_leaves