from odoo import models, fields

class SegmentProduct(models.Model):
    _name = 'segment.product'
    _description = 'Segment Product'

    name = fields.Char(string='Name', required=True)