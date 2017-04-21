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
        AnalyticLine = request.env['account.analytic.line']
        domain = [('partner_id.id', '=', partner.id)]
        url_args = request.httprequest.args

        if url_args:
            start = url_args['start']
            end = url_args['end']
            domain += [
                ('date', '>=', str(start)),
                ('date', '<=', str(end))]

        timesheet_count = int(AnalyticLine.search_count(domain))
        pager = request.website.pager(
            url="/my/my_timesheets_date/",
            total=timesheet_count,
            page=page,
            step=self._items_per_page,
        )

        lines = AnalyticLine.search(
            domain, limit=self._items_per_page,
            offset=pager['offset']
        )
        values.update({
            'lines': lines,
            'pager': pager,
            'page_name': 'my_timesheets_date',
            'default_url': '/my_timesheets_date/',
            'AnalyticLine': AnalyticLine,
            'total_duration': sum(lines.mapped('unit_amount'))
        })

        return request.render(
            "website_timesheets_js.portal_my_timesheets_date", values)
