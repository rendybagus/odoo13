from odoo.tests.common import TransactionCase

class TestSchoolJadwal(TransactionCase):

    def setUp(self):
        super(TestSchoolJadwal, self).setUp()
        self.kelas = self.env['school.kelas'].create({
            'name': 'Kelas 1',
        })
        self.mata_pelajaran = self.env['school.mata_pelajaran'].create({
            'name': 'Matematika',
        })
        self.jadwal = self.env['school.jadwal'].create({
            'name': 'Jadwal 1',
            'hari': 'senin',
            'kelas_id': self.kelas.id,
            'jam': '08:00-09:00',
            'mata_pelajaran_id': self.mata_pelajaran.id,
        })

    def test_create_jadwal(self):
        """Test creating a new jadwal"""
        self.assertTrue(self.jadwal, "Jadwal creation failed")

    def test_jadwal_fields(self):
        """Test the fields of the jadwal"""
        self.assertEqual(self.jadwal.name, 'Jadwal 1', "Name field mismatch")
        self.assertEqual(self.jadwal.hari, 'senin', "Hari field mismatch")
        self.assertEqual(self.jadwal.kelas_id.name, 'Kelas 1', "Kelas field mismatch")
        self.assertEqual(self.jadwal.jam, '08:00-09:00', "Jam field mismatch")
        self.assertEqual(self.jadwal.mata_pelajaran_id.name, 'Matematika', "Mata Pelajaran field mismatch")
