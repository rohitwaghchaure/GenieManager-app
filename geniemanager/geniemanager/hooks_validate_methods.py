from __future__ import unicode_literals
import frappe
import json
import frappe.utils
from frappe.utils import cstr, flt, getdate, comma_and
from frappe import _

def validate_company_methods(doc, method):
	validate_duplicate_warehouse(doc)

def validate_duplicate_warehouse(obj):
	warehouse_list = []
	if obj.get('locations'):
		data = [ data.location for data in obj.get('locations')]
		for warehouse in data:
			if data.count(warehouse) > 1:
				frappe.throw(_('You have enter location {0} more than once').format(warehouse))

def validate_quotation_methods(doc, method):
	validate_Location_CompanyItem(doc)

def validate_SalesOrder_methods(doc, method):
	validate_Location_CompanyItem(doc)

def validate_SalesInvoice_methods(doc, method):
	validate_Location_CompanyItem(doc)

def validate_Location_CompanyItem(obj):
	for item_data in obj.get('items'):
		if not frappe.db.get_value('Companies Location', {'parent': obj.company, 'location': item_data.location}, 'name'):
			frappe.throw(_('Validation Error: Location {0} not present in company {1}').format(item_data.location, obj.company))
		elif not frappe.db.get_value('Locations Item', {'parent': item_data.location, 'item': item_data.item_code}, 'name'):
			frappe.throw(_('Validation Error: Item {0} not present at location {1}').format(item_data.item_code, item_data.location))

