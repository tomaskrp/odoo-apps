# -*- coding: utf-8 -*-
# © 2018 Tomas Karpovic
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Fleet X Reports",
    "version": "10.0.1.0.0",
    "author": "Tomas Karpovic",
    "license": "AGPL-3",
    "category": "Fleet",
    "depends": [
        "fleet_x_vehicles",
        "fleet_x",
        "report_py3o_fusion_server",
    ],
    "data": [
        "data/fleet_vehicle_data.xml",
        "report/report.xml",
    ],
    'installable': True
}
