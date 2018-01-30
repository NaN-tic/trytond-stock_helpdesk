# This file is part of the stock_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Helpdesk', 'ShipmentOutHelpdesk', 'ShipmentOutReturnHelpdesk',
    'ShipmentInHelpdesk', 'ShipmentInReturnHelpdesk']


class Helpdesk:
    __metaclass__ = PoolMeta
    __name__ = 'helpdesk'
    shipments_out = fields.Many2Many('shipment.out.helpdesk', 'helpdesk',
        'shipment', 'Shipments Out', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['shipment', 'generic']),
            },
        depends=['state', 'kind'])
    shipments_out_return = fields.Many2Many('shipment.out.return.helpdesk',
        'helpdesk', 'shipment', 'Shipments Out Return', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['shipment', 'generic']),
            },
        depends=['state', 'kind'])
    shipments_in = fields.Many2Many('shipment.in.helpdesk', 'helpdesk',
        'shipment', 'Shipments In', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['shipment', 'generic']),
            },
        depends=['state', 'kind'])
    shipments_in_return = fields.Many2Many('shipment.in.return.helpdesk',
        'helpdesk', 'shipment', 'Shipments In Return', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['shipment', 'generic']),
            },
        depends=['state', 'kind'])

    @classmethod
    def __setup__(cls):
        super(Helpdesk, cls).__setup__()
        value = ('shipment', 'Shipments')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)

    @classmethod
    def view_attributes(cls):
        return super(Helpdesk, cls).view_attributes() + [
            ('//page[@id="shipments"]', 'states', {
                    'invisible': ~Eval('kind').in_(['shipment', 'generic']),
                    })]


class ShipmentOutHelpdesk(ModelSQL):
    'Shipment Out - Helpdesk'
    __name__ = 'shipment.out.helpdesk'
    _table = 'shipment_out_helpdesk_rel'
    shipment = fields.Many2One('stock.shipment.out', 'Shipment Out',
        ondelete='CASCADE', select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)


class ShipmentOutReturnHelpdesk(ModelSQL):
    'Shipment Out Return - Helpdesk'
    __name__ = 'shipment.out.return.helpdesk'
    _table = 'shipment_out_return_helpdesk_rel'
    shipment = fields.Many2One('stock.shipment.out.return', 'Shipment Out Return',
        ondelete='CASCADE', select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)


class ShipmentInHelpdesk(ModelSQL):
    'Shipment In - Helpdesk'
    __name__ = 'shipment.in.helpdesk'
    _table = 'shipment_in_helpdesk_rel'
    shipment = fields.Many2One('stock.shipment.in', 'Shipment In',
        ondelete='CASCADE', select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)


class ShipmentInReturnHelpdesk(ModelSQL):
    'Shipment In Return - Helpdesk'
    __name__ = 'shipment.in.return.helpdesk'
    _table = 'shipment_in_return_helpdesk_rel'
    shipment = fields.Many2One('stock.shipment.in.return', 'Shipment In Return',
        ondelete='CASCADE', select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)
