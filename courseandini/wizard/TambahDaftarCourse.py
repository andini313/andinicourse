from odoo import api, fields, models


'''
Membuat model BarangDarang yang inherit
ke Transient Model, Odoo 14 ke atas harus
di daftarkan di security
'''
class TambahCourse(models.TransientModel):
    _name = 'courseandini.tambahcourse'

    daftarcourse_id = fields.Many2one(comodel_name='courseandini.daftarcourse', string='Nama Course', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_tambah_course(self):
        for line in self:
            self.env['courseandini.daftarcourse'].search([('id', '=', line.daftarcourse_id.id)]).write(
                {'stok_course': line.daftarcourse_id.stok_course +  line.jumlah}
            )