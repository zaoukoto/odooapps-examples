# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatience(models.Model):
    # This will be installed in postgres table
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
        ], required=True, default='other')
    note = fields.Text(string='Description')
