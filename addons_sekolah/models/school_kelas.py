from odoo import models, fields

class Kelas(models.Model):
    _name = 'school.kelas'
    _description = 'Data Kelas'

    name = fields.Char(string='Name Kelas', required=True)
    nm_siswa_ids = fields.One2many('school.siswa', 'kelas_id', string='Nama Siswa')
    wali_kelas = fields.Many2one('school.guru', string='Wali Kelas')
