# models/person.py

from datetime import date

from odoo16.odoo import fields, models


class Person(models.Model):
    _name = 'custom_age_task.person'

    name = fields.Char('Name', required=True)
    birthdate = fields.Date('Birthdate')
    age_group = fields.Selection([
        ('blue', '18 Years Old'),
        ('gray', '< 18 Years Old'),
        ('red', '> 18 Years Old'),
    ], string='Age Group', compute='_compute_age_group')

    def _compute_age_group(self):
        for person in self:
            if person.birthdate:
                age = (date.today() - person.birthdate).days // 365.25
                if age < 18:
                    person.age_group = 'gray'
                elif age == 18:
                    person.age_group = 'blue'
                else:
                    person.age_group = 'red'
            else:
                person.age_group = False
