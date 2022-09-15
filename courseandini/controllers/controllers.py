from crypt import methods
import json


from odoo import http, models, fields
from odoo.http import request


class andinicourse(http.Controller):
    @http.route('/courseandini/getdaftarcourse', auth='public', method=['GET'])
    def getdaftarcourse(self, **kw):
        # Mengambil semua barang dari table barang
        daftarcourse = request.env['courseandini.daftarcourse'].search([])
        items = []

        for item in daftarcourse:
            items.append({
                'name_course': item.name_course,
                'lama_course': item.lama_course,
                'harga_course': item.harga_course,
                'stok_course': item.stok_course,
                'klp_course': item.klp_course,
                'mentor': item.mentor
            })
        
        return json.dumps(items)

		# Perubhannya di sini
    @http.route('/courseandini/getmentor', auth='public', method=['GET'])
    def getMentor(self, **kw):
        mentor = request.env['courseandini.mentor'].search([])
        items = []

        for item in mentor:
            items.append({
                'nama_perusahaan': item.name_mentor,
                'alamat': item.alamat,
                'no_telepon': item.no_tlp,
                'course': item.course
            })
        
        return json.dumps(items)