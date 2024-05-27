# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'addons_sekolah',
    'author': 'M Rendy Baguspriawan',
    'category': '',
    'version': '13.0.1.1.0',
    'description': """""",
    'summary': 'Odoo 13',
    'sequence': 10,
    'website': '',
    'depends': [
        'base'
     ],
    'license': 'LGPL-3',
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/school_siswa.xml',
        'views/school_guru.xml',
        'views/school_kelas.xml',
        'views/school_mata_pelajaran.xml',
        'views/school_jadwal.xml',
    ],
    'qweb': [],
    'application': True,
}
