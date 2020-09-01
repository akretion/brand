# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestCrmLead(TransactionCase):
    def setUp(self):
        super(TestCrmLead, self).setUp()
        self.lead = self.env.ref("crm.crm_case_1")
        self.contact_1 = self.env['res.partner'].create({
            'name': 'Part Fry',
            'email': 'part1@test.example.com',
        })
        self.lead.brand_id = self.env["res.brand"].create(
            {"name": "brand"})

    def test_create_quotation(self):
        """It should create branded quotation"""
        action = self.lead.action_new_quotation()
        so = self.env["sale.order"].with_context(action['context'])
        order = so.create({"name": self.lead.name,
            "partner_id": self.contact_1.id})
        self.assertEqual(order.brand_id, self.lead.brand_id)


