# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'FacturaMaqpower',
    'summary': 'Formato de factura integrado a FEL mexico enterprise',
    'version': '1.0',
    'author': 'Steve Piñero (Ogsistemas)',
    'maintainer': 'OgSistemas',
    'website': 'http://www.ogsistemas.com',
    'category': 'Hidden',
    'depends': ['base', 'l10n_mx_edi'],
    'data': [
        'views/report_invoice.xml',
        'views/report_header.xml',
    ],
    'installable': True,
    'license': 'OEEL-1',
    'images': ['static/src/img/fel.png'],
}