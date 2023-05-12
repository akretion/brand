# Copyright 2018 Tecnativa - David Vidal
# Copyright 2020 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    product_brand_id = fields.Many2one(comodel_name="product.brand", string="Brand")

    def _group_by_sale(self, groupby=""):
        res = super()._group_by_sale(groupby)
        res += """, t.product_brand_id"""
        return res

    # flake8: noqa
    # pylint:disable=dangerous-default-value
    def _query(self, with_clause="", fields={}, groupby="", from_clause=""):
        fields["product_brand_id"] = ", t.product_brand_id as product_brand_id"
        groupby += ", t.product_brand_id"
        return super()._query(with_clause, fields, groupby, from_clause)
