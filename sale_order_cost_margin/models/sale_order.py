from odoo import models, fields, api

class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'
    
    # الحقول موجودة بالفعل من وحدة sale_margin
    # purchase_price - تكلفة المنتج
    # margin - هامش الربح
    # margin_percent - نسبة هامش الربح
    
    @api.onchange('purchase_price', 'price_unit', 'product_uom_qty')
    def _compute_margin_fields(self):
        """إعادة حساب هامش الربح بعد تحديث سعر التكلفة"""
        for line in self:
            if line.product_id and line.product_uom_qty:
                # تأكد من قيمة سعر التكلفة
                if not line.purchase_price and line.product_id:
                    # إذا لم يتم تعيين سعر التكلفة، استخدم تكلفة المنتج الافتراضية
                    line.purchase_price = line.product_id.standard_price
                
                # حساب هامش الربح والنسبة المئوية
                line.margin = line.price_subtotal - (line.purchase_price * line.product_uom_qty)
                if line.price_subtotal:
                    line.margin_percent = (line.margin / line.price_subtotal) * 100
                else:
                    line.margin_percent = 0.0


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    
    margin_total = fields.Monetary(compute='_compute_margin_total', string='إجمالي الهامش', store=True)
    margin_percent_total = fields.Float(compute='_compute_margin_total', string='إجمالي نسبة الهامش (%)', store=True)
    
    @api.depends('order_line.margin')
    def _compute_margin_total(self):
        """حساب إجمالي هامش الربح للطلب بأكمله"""
        for order in self:
            order.margin_total = sum(order.order_line.mapped('margin'))
            if order.amount_untaxed:
                order.margin_percent_total = (order.margin_total / order.amount_untaxed) * 100
            else:
                order.margin_percent_total = 0.0
