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
			'fieldname':'party_type',
			'label':'Party Type',
			'fieldtype':'Data',
			'width':130

		},
		{
			'fieldname':'member_name',
			'label':'Party',
			'fieldtype':'Data',
			'width':130


		},
		{
			'fieldname':'membership_type',
			'label':'Membership Type',
			'fieldtype':'Data',
			'width':130


		},
		# {
		# 	'fieldname':'column_break',
		# 	# 'label':'Membership Type',
		# 	'fieldtype':'Column Break'

		# },
		{
			'fieldname':'member',
			'label':'Member',
			'fieldtype':'Data',
			'width':130


		},
		{
			'fieldname':'from_date',
			'label':'From Date',
			'fieldtype':'Date',
			'width':130


		},
		{
			'fieldname':'to_date',
			'label':'To Date',
			'fieldtype':'Date',
			'width':130


		},
		{
			'fieldname':'membership_status',
			'label':'Membership Status',
			'fieldtype':'Data',
			'width':130


		},
	]
# -----------------------------------Get  Data----------------------------------------------------

def get_data(filters):
	# condition=""
	# if filters:
	# 	condition= "WHERE 1=1"
	# 	if filters.get("member_name"):
	# 		condition += f" AND lm.member_name = '{filters.get('member_name')}'"

	# 	if filters.get("membership_type"):
	# 		condition += f" AND membership_type = '{filters.get('membership_type')}'"
		# frappe.msgprint(condition)
		# if filters.get("membership_status"):
		# 	condition += f" AND membership_status = '{filters.get('membership_status')}'"
	# return frappe.db.sql(f"""SELECT * from `tabLibrary Member` lm left join `tabLibrary Membership` lm2 on lm.member_name = lm2.member_name {condition}""", as_dict=1)
	
	
	
	# -----------------------------------frappe.qb-----------------------------------------------
	
	
	tbl1 = DocType('Library Member')
	tbl2 = DocType('Library Membership')

	condition= (frappe.qb.from_(tbl1).left_join(tbl2)
			.on(tbl1.member_name == tbl2.member_name)
			.select (
				tbl1.member_name,
				tbl1.party_type,tbl1.party,
				tbl1.membership_type,
				tbl2.member,
				tbl2.to_date,
				tbl2.from_date,
				tbl2.membership_status))
	
	if filters:
	
		if filters.get("member_name"):
			condition =condition.where(tbl1.member_name ==filters.get('member_name'))

		if filters.get("membership_type"):
			condition =condition.where(tbl1.membership_type == filters.get('membership_type'))
		# frappe.msgprint(condition)
		if filters.get("membership_status"):
			condition =condition.where (tbl2.membership_status == filters.get('membership_status'))
			
	return condition.run(as_dict=True)
