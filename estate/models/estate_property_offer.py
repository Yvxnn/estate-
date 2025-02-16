from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"

    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", store=True)
    # Existing fields
    price = fields.Float(string="Price")
    status = fields.Selection(
        string="Status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    # Accept Button Logic
    def action_accept(self):
        for record in self:
            if record.property_id.state == "sold":
                raise UserError("Cannot accept an offer for a sold property.")
            # Ensure only one offer is accepted
            if record.property_id.offer_ids.filtered(lambda o: o.status == "accepted"):
                raise UserError("Another offer has already been accepted.")
            record.status = "accepted"
            # Set the selling price and buyer for the property
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = "offer_accepted"
        return True

    # Refuse Button Logic
    def action_refuse(self):
        for record in self:
            record.status = "refused"
        return True