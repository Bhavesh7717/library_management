# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			'fieldname':'party_type',
			'label': 'Party Type',
			'fieldtype': 'Data' 
		},
		{
			'fieldname':'party',
			'label': 'Party',
			'fieldtype': 'Data' 
		},
		{
			'fieldname':'member_name',
			'label': 'Member Name',
			'fieldtype': 'Data' 
		},
		{
			'fieldname':'membership_type',
			'label': 'Membership Type',
			'fieldtype': 'Data' 
		},
		{
			'label': 'Enable',
			'fieldname':'enable',
			'fieldtype': 'Checkbox' 
		}
	]

def get_data(filters):
	print(filters)
	condition = ""
	if filters:
		condition = "WHERE 1=1"
		if filters.get("enable"):
			condition += f" AND enable = '{filters.get('enable')}'"
		
		if filters.get("membership_type"):
			condition += f" AND membership_type = '{filters.get('membership_type')}'"
	print(condition)
	return frappe.db.sql(f"""SELECT * from `tabLibrary Member` {condition}""", as_dict=1)
	# return frappe.get_all()
	# return frappe.qb.from_()