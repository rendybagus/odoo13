from odoo import models, fields

class Guru(models.Model):
    _name = 'school.guru'
    _description = 'Data Guru'

    name = fields.Char(string='Name Guru', required=True)
    nip = fields.Char(string='NIP', required=True)
    jns_kelamin = fields.Selection([('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin')
    mata_pelajaran = fields.Many2one('school.mata_pelajaran', string='Mata Pelajaran')
    usia = fields.Integer(string='Usia')
    no_telp = fields.Char(string='Nomor Telepon')
    alamat = fields.Text(string='Alamat')
    kelas_ids = fields.One2many('school.kelas', 'wali_kelas', string='Kelas yang Diasuh')
