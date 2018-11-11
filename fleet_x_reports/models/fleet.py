# -*- encoding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, api


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    @api.multi
    def get_earliest_log_contract(self):
        return self.env['fleet.vehicle.log.contract'].search(
            [('vehicle_id', '=', self.id)], order='start_date asc', limit=1)

    @api.multi
    def get_start_date(self):
        earliest_contract = self.get_earliest_log_contract()
        if earliest_contract.start_date:
            return earliest_contract.start_date
        return ''

    @api.multi
    def get_expiration_date(self):
        earliest_contract = self.get_earliest_log_contract()
        if earliest_contract.expiration_date:
            return earliest_contract.expiration_date
        return ''

    @api.multi
    def get_mileage(self):
        return self.odometer - float(self.podometer)
