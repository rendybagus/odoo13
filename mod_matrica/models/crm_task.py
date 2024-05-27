from odoo import models, fields

class CrmTask(models.Model):
    _name = 'crm.task'
    _description = 'CRM Task'

    name = fields.Char(string='Task', required=True)
    deadline = fields.Date(string='Deadline')
    status = fields.Selection([
        ('todo', 'To do'),
        ('progress', 'Progress'),
        ('done', 'Done')
    ], string='Status', default='todo')
    lead_id = fields.Many2one('crm.lead', string='Lead', ondelete='cascade')