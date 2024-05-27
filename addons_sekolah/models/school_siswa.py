from odoo import models, fields

class Siswa(models.Model):
    _name = 'school.siswa'
    _description = 'Data Siswa'

    nis = fields.Char(string='NIS', required=True)
    name = fields.Char(string='Nama Siswa', required=True)
    jns_kelamin = fields.Selection([('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Char(string='Agama')
    nm_ayah = fields.Char(string='Nama Ayah')
    nm_ibu = fields.Char(string='Nama Ibu')
    usia = fields.Integer(string='Usia')
    alamat = fields.Text(string='Alamat')
    kelas_id = fields.Many2one('school.kelas', string='Kelas')