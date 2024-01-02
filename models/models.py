# -*- coding: utf-8 -*-

from odoo import models, fields, Command


class AccountMove(models.Model):
    _inherit = ["estate.property"]

    move_type = fields.Selection(selection=[
        ('entry', 'Journal Entry'),
        ('out_invoice', 'Customer Invoice'),
        ('out_refund', 'Customer Credit Note'),
        ('in_invoice', 'Vendor Bill'),
        ('in_refund', 'Vendor Credit Note'),
        ('out_receipt', 'Sales Receipt'),
        ('in_receipt', 'Purchase Receipt'),
    ], string='Type', required=True, store=True, index=True, readonly=True, tracking=True,
        default="entry", change_default=True)

    def sell_property(self):
        '''
        We calculate all billing price based on bellow condition.
        search all records from estate.property.model from estate.property
        '''
        records = self.env['estate.property.offer'].search(
            [('partner_id', '=', self.buyer.id), ('property_id', '=', self.id)])

        for record in records:
            buyer_price = record.price
            selling_price_fees = buyer_price * 0.06
            administrative_fees = 100.00
            billing_price = buyer_price + selling_price_fees + administrative_fees

            self.env['account.move'].create(
                {
                    'move_type': 'out_invoice',
                    'invoice_date': fields.Date.context_today(self),
                    'partner_id': self.buyer.id,
                    'invoice_line_ids': [Command.create({
                        'quantity': 1,
                        'name': self.name,
                        'price_unit': buyer_price,
                        'price_subtotal': billing_price,
                    })]
                }
            )
            return super(AccountMove, self).sell_property()
