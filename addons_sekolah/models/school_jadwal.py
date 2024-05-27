from odoo import models, fields

class Jadwal(models.Model):
    _name = 'school.jadwal'
    _description = 'Data Jadwal'

    name = fields.Char(string='Name Jadwal', required=True)
    hari = fields.Selection([('senin', 'Senin'), ('selasa', 'Selasa'), ('rabu', 'Rabu'), ('kamis', 'Kamis'), ('jumat', 'Jumat')], string='Hari')
    kelas_id = fields.Many2one('school.kelas', string='Kelas')
    jam = fields.Char(string='Jam')
    mata_pelajaran_id = fields.Many2one('school.mata_pelajaran', string='Mata Pelajaran')
