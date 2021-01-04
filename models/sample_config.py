# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, date, time, timedelta
import calendar
#from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from itertools import groupby
from pytz import timezone, UTC
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_is_zero
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang


class SampleConfig(models.TransientModel):
    _name = 'sample.config'
    _inherit = 'res.config.settings'

    name = fields.Char('configuración de Muestras', default='sample config')
    peso_minimo_muestra = fields.Float('Peso Mínimo Muestra', tracking=True, store=True)
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', compute='_compute_weight_uom_name',store=False)

    def _compute_weight_uom_name(self):
        self.weight_uom_name = self._get_weight_uom_name_from_ir_config_parameter()

    @api.model
    def _get_weight_uom_name_from_ir_config_parameter(self):
        return self._get_weight_uom_id_from_ir_config_parameter().display_name

    @api.model
    def _get_weight_uom_id_from_ir_config_parameter(self):
        """ Get the unit of measure to interpret the `weight` field. By default, we considerer
        that weights are expressed in kilograms. Users can configure to express them in pounds
        by adding an ir.config_parameter record with "product.product_weight_in_lbs" as key
        and "1" as value.
        """
        product_weight_in_lbs_param = self.env['ir.config_parameter'].sudo().get_param('product.weight_in_lbs')
        if product_weight_in_lbs_param == '1':
            return self.env.ref('uom.product_uom_lb', False) or self.env['uom.uom'].search([('measure_type', '=' , 'weight'), ('uom_type', '=', 'reference')], limit=1)
        else:
            return self.env.ref('uom.product_uom_kgm', False) or self.env['uom.uom'].search([('measure_type', '=' , 'weight'), ('uom_type', '=', 'reference')], limit=1)
