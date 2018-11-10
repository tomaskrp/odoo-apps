# -*- encoding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    rental = fields.Boolean(string='Rental')
