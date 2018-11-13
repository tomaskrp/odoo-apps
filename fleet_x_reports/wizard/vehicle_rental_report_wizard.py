# -*- encoding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, api


class VehicleRentalReportWizard(models.TransientModel):
    _name = 'vehicle.rental.report.wizard'

    @api.multi
    def open_report(self):
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'vehicle_rental_report',
            'datas': {
                'ids': self.env['fleet.vehicle'].get_all_rented_vehicles().ids,
                'model': 'fleet.vehicle'
            }
        }
