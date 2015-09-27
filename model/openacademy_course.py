# -*- coding: utf-8 -*-
from openerp import models, fields, api
'''
This module create model of Course
'''

class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course'   # model's name
    
    name = fields.Char(string='Title', required=True)  # reserved field to identify record's name
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                      ondelete='set null',
                                      string="Responsible", index=True)
