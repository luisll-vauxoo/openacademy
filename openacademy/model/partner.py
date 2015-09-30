# -*- coding: utf-8 -*-
from openerp import fields, models
'''
This module inherit from partner
'''

class Partner(models.Model):
    '''
    This class is inherited from res.partner
    '''
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session',
                                    string="Session as attendee",
                                    readonly=True)

