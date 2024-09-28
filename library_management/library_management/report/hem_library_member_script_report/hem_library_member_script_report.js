// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Hem Library Member Script Report"] = {
	"filters": [
		{
			'label': 'Membership Type',
			'fieldname':'membership_type',
			'fieldtype': 'Select',
			'options':["", "Gold", "Silver", "Bronze"]
		},
		{
			'label': 'Member Name',
			'fieldname' : 'member_name',
			'fieldtype' : 'Data'
		},
		{
			'label': 'Membership Status',
			'fieldname' : 'membership_status',
			'fieldtype' : 'Select',
			'options':["", "New", "Current",'Expired', "Pending", 'Cancelled']
		}
				
	]
};
