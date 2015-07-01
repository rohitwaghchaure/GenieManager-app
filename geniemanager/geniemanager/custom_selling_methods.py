from __future__ import unicode_literals
import frappe
import json
import frappe.utils
from frappe.utils import cstr, flt, getdate, comma_and
from frappe import _

def item_query(doctype, txt, searchfield, start, page_len, filters):
	response = [['']]
	if filters.get('location'):
		data = frappe.db.sql(''' select item from `tabLocations Item` where parent = "%s"'''%(filters.get('location')), as_list=1, debug=1)
		response = data if data else response
	return response

def location_query(doctype, txt, searchfield, start, page_len, filters):
	response = [['']]
	if filters.get('company'):
		data = frappe.db.sql(''' select location from `tabCompanies Location` where parent = "%s"'''%(filters.get('company')), as_list=1, debug=1)
		response = data if data else response
	return response