from odoo import models, fields

class Asset(models.Model):
    _name = "assets.asset"
    _description = "Company Asset or Hardware"

    name = fields.Char(string="Name", required=True)
    model_no = fields.Char(string="Model No")
    serial_no = fields.Char(string="Serial No")
    type = fields.Selection(string="Asset Type", selection=[('0', 'Laptop'), ('1', 'Monitor')])
    note = fields.Text("Description")
