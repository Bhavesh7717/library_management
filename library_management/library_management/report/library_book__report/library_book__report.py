# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

import frappe 
from frappe.query_builder.utils import DocType



def execute(filters=None):
	columns, data = get_colums(),get_data(filters)
	return columns, data

def get_colums():
	return [
		{
			'fieldname':'library_member',
			'label':'Member Name',
			'fieldtype':'link',
			'width':130

		},
		{
			'fieldname':'title',
			'label':'Book',
			'fieldtype':'Data',
			'width':130

		},
		{
			'fieldname':'price',
			'label':'Price',
			'fieldtype':'float',
			'width':130

		},
		{
			'fieldname':'stock_balance',
			'label':'Stock Balence',
			'fieldtype':'int',
			'width':130

		},
	]


def get_data(filters):
	tbl1 = DocType('Library Book')
	tbl2 = DocType('Library Stock Ledger')

	condition=(frappe.qb.from_(tbl1).inner_join(tbl2)
				.on(tbl1.name == tbl2.library_book)
				.select(
						tbl1.title,
						tbl1.price,                      
						tbl2.stock_balance,
						tbl2.library_member,                   
						# tbl1.returned_on
						))
	if filters:

		if filters.get("library_member"):
			condition =condition.where(tbl2.library_member ==filters.get('library_member'))

	return condition.run(as_dict=True)
