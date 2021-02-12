from odoo import models, fields, api, exceptions


class Course(models.Model):
    _name = 'openacademy.course'
    _description = "Cursos de OpenAcademy "

    name = fields.Char(String="Title", required=True)
    dscription = fields.Text()

    responsible_id = fields.Many2one(
        'res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
