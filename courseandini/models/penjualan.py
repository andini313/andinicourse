from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Penjualan(models.Model):
    _name = 'courseandini.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='courseandini.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['courseandini.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result
    @api.ondelete(at_uninstall=False)
    def __ondelete_penjualan(self):
        if self.detailpenjualan_ids:
            penjualan = []
            for line in self:
                penjualan = self.env['courseandini.detailpenjualan'].search(
                    [('penjualan_id', '=', line.id)])
                print(penjualan)

            for ob in penjualan:
                print(ob.course_id.name_course + ' ' + str(ob.qty))
                ob.course_id.stok_course += ob.qty
    
    def write(self, vals):
        for line in self:
            data_asli = self.env['courseandini.detailpenjualan'].search([('penjualan_id', '=', line.id)])
            print(data_asli)

            for data in data_asli:
                print(str(data.course_id.name_course) + " " + str(data.qty) + ' ' + str(data.course_id.stok_course))
                data.course_id.stok_course += data.qty
      
        line = super(Penjualan, self).write(vals)
      
        for line in self:
            data_setelah_edit = self.env['courseandini.detailpenjualan'].search([('penjualan_id', '=', line.id)])
            print(data_asli)
            print(data_setelah_edit)

            for data_baru in data_setelah_edit:
                if data_baru in data_asli:
                    print(data_baru.course_id.name_course + " " + str(data_baru.qty) + ' ' + str(data_baru.course_id.stok_course))
                    data_baru.course_id.stok_course -= data_baru.qty
                else:
                    pass

        return line

    _sql_constraints = [
        ('no_nota_unik','unique(name)','nomor nota tidak boleh sama !!!')
    ]

class DetailPenjualan(models.Model):
    _name = 'courseandini.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='courseandini.penjualan',
        string='Detail Penjualan')
    course_id = fields.Many2one(
        comodel_name='courseandini.daftarcourse',
        string='List Course')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_course_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_satuan

    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id.harga_course:
            self.harga_satuan = self.course_id.harga_course
    
    @api.model
    def create(self, vals):
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
            # Mendapatkan data berdasarkan ID pada detailpenjualan_id
            self.env['courseandini.daftarcourse'].search(
                [('id', '=', line.course_id.id)]
            ).write({'stok_course': line.course_id.stok_course - line.qty})

        return line
    
    @api.constrains('qty')
    def check_quantity(self):
        for line in self:
            if line.qty < 1:
                raise ValidationError('Jumlah pembelian harus minimal 1, silahkan input dengan benar!')
            elif line.course_id.stok_course < line.qty:
                raise ValidationError('Stok yang tersedia tidak mencukupi.')

   