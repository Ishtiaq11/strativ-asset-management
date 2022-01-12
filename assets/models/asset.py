from typing_extensions import Required
from odoo import models, fields

class Asset(models.Model):
    _name = "assets.asset"
    _descriptio = "Company Asset or Hardware"

    name = fields.Char(required=True)
    model_no = fields.Char()
    serial_no = fields.Char()
    type = fields.Selection(selection=[(0, 'Laptop'), (1, 'Monitor')])
