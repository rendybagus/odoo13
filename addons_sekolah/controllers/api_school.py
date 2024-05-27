from odoo import http
from odoo.http import request, Response
from datetime import date
import werkzeug.wrappers
import json


class SchoolController(http.Controller):

    @http.route('/api/siswa', auth='public', type='http', methods=['GET'], csrf=False)
    def get_siswa(self):
        print('masuk')
        siswa_records = request.env['school.siswa'].sudo().search([])
        siswa_list = [{
            'id': siswa.id,
            'nis': siswa.nis,
            'name': siswa.name,
            'jns_kelamin': siswa.jns_kelamin,
            'tgl_lahir': siswa.tgl_lahir.strftime('%Y-%m-%d') if siswa.tgl_lahir else None,
            'agama': siswa.agama,
            'nm_ayah': siswa.nm_ayah,
            'nm_ibu': siswa.nm_ibu,
            'usia': siswa.usia,
            'alamat': siswa.alamat,
            'kelas_id': siswa.kelas_id.id if siswa.kelas_id else None
        } for siswa in siswa_records]
        Response_data = {
            'status': '200 OK',
            'message': 'Data Siswa berhasil diambil',
            'data': siswa_list
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/kelas', auth='public', type='http', methods=['GET'])
    def get_kelas(self):
        kelas_records = request.env['school.kelas'].sudo().search([])
        kelas_list = [{
            'id': kelas.id,
            'name': kelas.name,
            'wali_kelas' : kelas.wali_kelas.id if kelas.wali_kelas else None,
            'nm_siswa_ids': [nm_siswa.name for nm_siswa in kelas.nm_siswa_ids]
        } for kelas in kelas_records]
        Response_data = {
            'status': '200 OK',
            'message': 'Data Kelas berhasil diambil',
            'data': kelas_list
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/mata_pelajaran', auth='public', type='http', methods=['GET'])
    def get_mata_pelajaran(self):
        mata_pelajaran_records = request.env['school.mata_pelajaran'].sudo().search([])
        mata_pelajaran_list = [{
            'id': mata_pelajaran.id,
            'name': mata_pelajaran.name,
            'jurusan': mata_pelajaran.jurusan
        } for mata_pelajaran in mata_pelajaran_records]
        Response_data = {
            'status': '200 OK',
            'message': 'Data Mata Pelajaran berhasil diambil',
            'data': mata_pelajaran_list
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/guru', auth='public', type='http', methods=['GET'])
    def get_guru(self):
        guru_records = request.env['school.guru'].sudo().search([])
        guru_list = [{
            'id': guru.id,
            'name': guru.name,
            'nip': guru.nip,
            'jns_kelamin': guru.jns_kelamin,
            'mata_pelajaran': guru.mata_pelajaran.id if guru.mata_pelajaran else None,
            'usia': guru.usia,
            'no_telp': guru.no_telp,
            'alamat': guru.alamat
        } for guru in guru_records]
        Response_data = {
            'status': '200 OK',
            'message': 'Data Guru berhasil diambil',
            'data': guru_list
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/jadwal', auth='public', type='http', methods=['GET'])
    def get_jadwal(self):
        jadwal_records = request.env['school.jadwal'].sudo().search([])
        jadwal_list = [{
            'id': jadwal.id,
            'name': jadwal.name,
            'hari': jadwal.hari,
            'kelas_id': jadwal.kelas_id.id if jadwal.kelas_id else None,
            'jam': jadwal.jam,
            'mata_pelajaran_id': jadwal.mata_pelajaran_id.id if jadwal.mata_pelajaran_id else None
        } for jadwal in jadwal_records]
        Response_data = {
            'status': '200 OK',
            'message': 'Data Jadwal berhasil diambil',
            'data': jadwal_list
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/jadwal/', auth='public', type='json', methods=['POST'])
    def post_jadwal(self, **payload):
        jadwal = request.env['school.jadwal'].sudo().create({
            'name': payload.get('name'),
            'hari': payload.get('hari'),
            'kelas_id': payload.get('kelas_id'),
            'jam': payload.get('jam'),
            'mata_pelajaran_id': payload.get('mata_pelajaran_id')
        })
        Response_data = {
            'status': '200 OK',
            'message': 'Data Jadwal berhasil ditambahkan',
            'data': {
                'id': jadwal.id,
                'name': jadwal.name,
                'hari': jadwal.hari,
                'kelas_id': jadwal.kelas_id.id if jadwal.kelas_id else None,
                'jam': jadwal.jam,
                'mata_pelajaran_id': jadwal.mata_pelajaran_id.id if jadwal.mata_pelajaran_id else None
            }
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/jadwal/', auth='public', type='json', methods=['PUT'])
    def put_jadwal(self, **payload):
        jadwal = request.env['school.jadwal'].sudo().search([('id', '=', payload.get('id'))])
        jadwal.write({
            'name': payload.get('name'),
            'hari': payload.get('hari'),
            'kelas_id': payload.get('kelas_id'),
            'jam': payload.get('jam'),
            'mata_pelajaran_id': payload.get('mata_pelajaran_id')
        })
        Response_data = {
            'status': '200 OK',
            'message': 'Data Jadwal berhasil diubah',
            'data': {
                'id': jadwal.id,
                'name': jadwal.name,
                'hari': jadwal.hari,
                'kelas_id': jadwal.kelas_id.id if jadwal.kelas_id else None,
                'jam': jadwal.jam,
                'mata_pelajaran_id': jadwal.mata_pelajaran_id.id if jadwal.mata_pelajaran_id else None
            }
        }
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )

    @http.route('/api/jadwal/', auth='public', type='json', methods=['DELETE'])
    def delete_jadwal(self, **payload):
        jadwal = request.env['school.jadwal'].sudo().search([('id', '=', payload.get('id'))])
        Response_data = {
            'status': '200 OK',
            'message': 'Data Jadwal berhasil dihapus',
            'data': {
                'id': jadwal.id,
                'name': jadwal.name,
                'hari': jadwal.hari,
                'kelas_id': jadwal.kelas_id.id if jadwal.kelas_id else None,
                'jam': jadwal.jam,
                'mata_pelajaran_id': jadwal.mata_pelajaran_id.id if jadwal.mata_pelajaran_id else None
            }
        }
        jadwal.unlink()
        return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(Response_data)
            )