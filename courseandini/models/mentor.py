from odoo import api, fields, models


class mentor(models.Model):
    _name = 'courseandini.mentor'
    _description = 'New Description'

    name_mentor = fields.Char(string='Nama Mentor')
    alamat = fields.Char(string='Alamat')
    no_tlp = fields.Integer(string='No.Telpon')
    course = fields.Char(string='Course')

    course_id = fields.Many2many(comodel_name='courseandini.daftarcourse', string='daftar course')