# Copyright (C) 2020 Akretion (http://www.akretion.com)
# @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CrmLead(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead", "res.brand.mixin"]

    def action_new_quotation(self):
        action = super().action_new_quotation()
        action['context']['default_brand_id'] = self.brand_id.id
        return action    
