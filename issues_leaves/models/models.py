# -*- coding: utf-8 -*-

from odoo import models, fields, api

class issues_leaves(models.Model):
    _name = 'hr.holidays'

    days_before_approval = fields.Integer(related="holiday_status_id.remaining_leaves", string="Saldo de días antes de la aprobación")





