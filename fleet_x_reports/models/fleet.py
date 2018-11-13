# -*- encoding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


import base64

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

    @api.multi
    def get_all_rented_vehicles(self):
        return self.env['fleet.vehicle'].search([('rental', '=', True)])

    @api.multi
    def _send_vehicle_rental_report(self):
        recipients = self.env.ref('fleet.fleet_group_manager').users
        data, report_format = self.env['ir.actions.report.xml'].render_report(
            self.get_all_rented_vehicles().ids,
            'vehicle_rental_report', {})
        att_id = self.env['ir.attachment'].create({
            'name': 'Rental Report',
            'type': 'binary',
            'datas': base64.encodestring(data),
            'datas_fname': 'Rental Report.odt',
            'res_model': 'fleet.vehicle',
            'res_id': 0,
            'mimetype': 'application/vnd.oasis.opendocument.text'
        })
        for recipient in recipients:
            self.send_report(recipient, att_id)
        print att_id

    @api.multi
    def send_report(self, recipient, attachment):
        mail_values = {
            'email_from': self.env.user.email,
            'reply_to': self.env.user.email,
            'recipient_ids': [(4, recipient.partner_id.id)],
            'subject': 'Vehicle Rental Report',
            'body_html': 'See attached report',
            'attachment_ids': [(4, attachment.id)],
        }
        self.env['mail.mail'].create(mail_values).send()
        return True
