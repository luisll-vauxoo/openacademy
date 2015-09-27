from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'   # model's name
    
    name = fields.Char(string='Title', required=True)  # reserved field to identify record's name
    description = fields.Text(string='Description')

