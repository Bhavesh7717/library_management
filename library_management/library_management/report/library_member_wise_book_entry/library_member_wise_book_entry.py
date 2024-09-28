# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder.utils import DocType

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
			{
				'fieldname' : 'library_book',
				'label' : 'Library Book',
				'fieldtype' : 'Data',
				"width": 150
			},
			{
				'fieldname' : 'member_name',
				'label' : 'Member Name',
				'fieldtype' : 'Data',
				"width": 150
			},
			
			{
				'fieldname' : 'book_qty',
				'label' : 'Book Qty',
				'fieldtype' : 'Int'
			},
			{
				'fieldname' : 'issue_date',
				'label' : 'Issue Date',
				'fieldtype' : 'Date',
				"width": 150
			},
			{
				'fieldname' : 'returned_on',
				'label' : 'Return Date',
				'fieldtype' : 'Date',
				"width": 150
			}

			]
def get_data(filters):
	tbl1=DocType('Library Book Issue')
	tbl2=DocType('Library Stock Ledger')

	records=(frappe.qb.from_(tbl1)
				.right_join(tbl2)         # whole document form member, common from membership
				.on(tbl1.member == tbl2.library_member)
				.select(
						tbl1.library_book,
						tbl1.member_name,                      
						tbl1.issue_date,
						tbl2.book_qty,                 
						tbl1.returned_on
						)
				)
	if filters:
		
		if filters.get('member_name'):
			records=records.where(tbl1.member_name == "mansi")

		if filters.get('membership_type'):
			records=records.where(tbl1.membership_type == filters.get('membership_type'))
		

	return records.run(as_dict=True)