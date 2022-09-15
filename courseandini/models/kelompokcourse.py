from odoo import api, fields, models


class kelompokcourse(models.Model):
    _name = 'courseandini.kelompokcourse'
    _description = 'New Description'

    name = fields.Selection([
        ('bisnis', 'Bisnis'),
        ('academi', 'Academi'),
        ('information technology', 'Information Technology')
    ], string='Nama Kelompok course')


    kode_course = fields.Char(string='Kode course')

    @api.onchange('name')
    def _onchange_kode_course(self):
        if self.name == 'bisnis':
            self.kode_course = 'BI01'
        elif self.name == 'academi':
            self.kode_course = 'AC02'
        elif self.name == 'Information Technology':
            self.kode_course = 'IT01'
    
    jumlah = fields.Char(string='Jumlah Course')

    daftarcourse_id = fields.One2many(comodel_name='courseandini.daftarcourse',
                                inverse_name='kelompokcourse_id',
                                string='Daftar course')
                                