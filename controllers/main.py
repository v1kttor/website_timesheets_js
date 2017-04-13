# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

from odoo.addons.website_portal.controllers.main import website_account

items_per_page = 20


class website_account(website_account):

    @http.route()
    def account(self, **kw):
        response = super(website_account, self).account(**kw)
        partner = request.env.user.partner_id
        timesheet_count = request.env['account.analytic.line'].search_count([
            ('partner_id.id', '=', partner.id),
        ])
        response.qcontext.update({
            'timesheet_count': timesheet_count,
        })
        return response

    @http.route(
        ['/my/my_timesheets_date/', '/my/my_timesheets_date/page/<int:page>'],
        type='http', auth='user', website=True)
    def portal_my_timesheets_date(self, page=1, sortby=None, week=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        aal = request.env['account.analytic.line']

        path = request.httprequest.full_path
        path = str(path)
        # import pdb; pdb.set_trace()

        if path[30:40] and path[46:56]:
            first_date = path[30:40]
            last_date = path[46:56]

            domain = [
                ('partner_id.id', '=', partner.id),
                ('date', '>=', first_date),
                ('date', '<=', last_date)]
        else:
            domain = [('partner_id.id', '=', partner.id)]

        timesheet_count = int(aal.search_count(domain))
        pager = request.website.pager(
            url="/my/my_timesheets_date/",
            total=timesheet_count,
            page=page,
            step=self._items_per_page,
        )

        lines = aal.search(
            domain, limit=self._items_per_page,
            offset=pager['offset']
        )
        values.update({
            'lines': lines,
            'pager': pager,
            'page_name': 'my_timesheets_date',
            'default_url': '/my_timesheets_date/',
            'aal': aal,
            'total_duration': sum(lines.mapped('unit_amount'))
        })

        return request.render(
            "website_timesheets_js.portal_my_timesheets_date", values)
