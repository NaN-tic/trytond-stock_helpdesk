# This file is part of the stock_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = [
    'Helpdesk', 'ShipmentOutHelpdesk'
    ]


class Helpdesk:
    __metaclass__ = PoolMeta
    __name__ = 'helpdesk'
    shipments = fields.Many2Many('shipment.out.helpdesk', 'helpdesk',
        'shipment', 'Stocks', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['shipment', 'generic']),
            },
        depends=['state'])

    @classmethod
    def __setup__(cls):
        super(Helpdesk, cls).__setup__()
        value = ('shipment', 'Shipment Out')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)


class ShipmentOutHelpdesk(ModelSQL):
    'Shipment Out - Helpdesk'
    __name__ = 'shipment.out.helpdesk'
    _table = 'shipment_out_helpdesk_rel'
    shipment = fields.Many2One('stock.shipment.out', 'Shipment Out',
        ondelete='CASCADE', select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)
