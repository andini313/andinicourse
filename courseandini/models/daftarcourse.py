from odoo import api, fields, models


class daftarcourse(models.Model):
    _name = 'courseandini.daftarcourse'
    _description = 'New Description'
    _rec_name = 'name_course'

    name_course= fields.Char(string='Nama Course')
    lama_course = fields.Char(string='Lama Course')
    harga_course = fields.Integer(string='Harga Course')
    stok_course = fields.Integer(string='Stok Course')
    mentor  = fields.Char(string='mentor')

    kelompokcourse_id = fields.Many2one(comodel_name='courseandini.kelompokcourse',
                                        string='Kelompok course',
                                        ondelete='cascade')   
                                        
    mentor_id = fields.Many2many(comodel_name='courseandini.mentor', string='Mentor')