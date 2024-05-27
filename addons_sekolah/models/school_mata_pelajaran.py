from odoo import models, fields

class MataPelajaran(models.Model):
    _name = 'school.mata_pelajaran'
    _description = 'Data Mata Pelajaran'

    name = fields.Char(string='Nama Mata Pelajaran', required=True)
    jurusan = fields.Char(string='Jurusan')
