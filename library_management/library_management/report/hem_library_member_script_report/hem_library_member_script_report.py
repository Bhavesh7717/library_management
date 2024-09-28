# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder.utils import DocType

def execute(filters=None):
	# columns, data = get_columns(), get_data(filters)
	columns, data = get_columns(), get_data_qb(filters)
	# columns, data = get_columns(), get_data_getall(filters)
	return columns, data

def get_columns():
	return [
		{
			'fieldname' : 'party_type',
			'label' : 'Party Type', 
			"width": 150,
		},
		{
			'filedname' : 'member_name',
			'label' : 'Member Name',
			'fieldtype' : 'Data',
			"width": 150,
		},
		{
			'filedname' : 'membership_type',
			'label' : 'Membership Type',
			'fieldtype' : 'Select',
			'option' : ["","Gold", "Silver", "Bronze"],
			"width": 150,
		},
		{
			'filedname' : 'membership_status',
			'label' : 'Membership Status',
			'fieldtype' : 'Select',
			'option' : ["","New","Pending"],
			"width": 150,
		},
		{
			'filedname' : 'from_date',
			'label' : 'From Date',
			'fieldtype' : 'Date',
			"width": 150,
		},
		{
			'filedname' : 'to_date',
			'label' : 'To Date',
			'fieldtype' : 'Date',
			"width": 150,
		}
	]


# ---------------------------METHOD - 1--------------------------#
# def get_data(filters):
# 	condition = ""
# 	if filters:
# 		condition = "WHERE 1=1"
# 		membership_type = filters.get("membership_type")
# 		if membership_type:
# 			condition += f" AND membership_type = '{membership_type}'"

# 		if filters.get('member_name'):
# 			condition+=f""" AND lm.member_name='{filters.get("member_name")}'"""

# 		if filters.get('membership_status'):
# 			condition+=f""" AND membership_status='{filters.get("membership_status")}'"""

# 	return frappe.db.sql(f"Select * from `tabLibrary Member` lm LEFT JOIN `tabLibrary Membership` lmsp ON lm.member_name = lmsp.member_name {condition}",as_dict=True)

# ---------------------------METHOD - 2--------------------------#
# def get_filters1(flrs):
# 	f={}
# 	if flrs:
# 		if flrs.get('member_name'):
# 			f['member_name'] = flrs.get('member_name')
# 		if flrs.get('membership_type'):
# 			f['membership_type'] = flrs.get('membership_type')
# 		return f
# def get_filters2(flrs):
# 	f={}
# 	if flrs:
# 		if flrs.get('membership_status'):
# 			f['membership_status'] = flrs.get('membership_status')
# 		return f

# def get_data_getall(flrs):
# 	lm = frappe.get_all(
#     		'Library Member',
#     		fields=['name', 'member_name', 'party','party_type', 'membership_type'],
# 			filters= get_filters1(flrs)
# 	)
# 	lms = frappe.get_all(
# 	    	'Library Membership',
#     		fields=['name', 'member_name', 'membership_status','from_date','to_date'],
# 			filters = get_filters2(flrs)
# 	)
# 	membership_map = {m['member_name']: m for m in lms} # -------------????????????
# 	result = []
# 	for member in lm:       #----4
# 		membership_name = membership_map.get(member['member_name'])
# 		# frappe.msgprint(membership_name)
# 		if membership_name:
# 			result.append({
# 				'name': member['name'],
# 				'party': member['party'],
# 				'party_type': member['party_type'],
# 				'member_name': member['member_name'],
# 				'membership_type': member['membership_type'],
# 				'membership_status': membership_name['membership_status'],
# 				'from_date': membership_name['from_date'],
# 				'to_date': membership_name['to_date']
# 			})
# 		else:
# 			result.append({
# 				'party': member['party'],
# 				'party_type': member['party_type'],
# 				'member_name': member['member_name'],
# 				'membership_type': member['membership_type'],
# 				'membership_status': None,
# 				'from_date': None,
# 				'to_date': None
# 			})
# 	return result


# -----------------------------METHOD - 3-------------------------#
def get_data_qb(filters):
	tbl1=DocType('Library Member')
	tbl2=DocType('Library Membership')
	
	records=(frappe.qb.from_(tbl1)
				.left_join(tbl2)         # whole document form member, common from membership
				.on(tbl1.member_name == tbl2.member_name)
				.select(tbl1.member_name,
						tbl1.party_type,
						tbl1.membership_type,
						tbl2.membership_status,
						tbl2.from_date,
						tbl2.to_date)
				)
	if filters:
		if filters.get('membership_type'):
			records=records.where(tbl1.membership_type == filters.get('membership_type'))
		
		if filters.get('member_name'):
			records=records.where(tbl1.member_name == filters.get('member_name'))
		
		if filters.get('membership_status'):
			records=records.where(tbl2.membership_status == filters.get('membership_status'))

	return records.run(as_dict=True)