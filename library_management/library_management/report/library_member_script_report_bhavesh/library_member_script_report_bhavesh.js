// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Member Script Report Bhavesh"] = {
	"filters": [
		{
			'label': 'Member Name',
			'fieldname':'member_name',
			'fieldtype': 'Data',
			
		},
		{
			'label': 'Membership Type',
			'fieldname':'membership_type',
			'fieldtype': 'Select',
			'options':["", "Gold", "Silver", "Bronze"]
		},
		{
			'label': 'Membership Status',
			'fieldname':'membership_status',
			'fieldtype': 'Select',
			'options':["", "New", "Current", "Expired","Pending","Cancelled"]
		},
		// {
		// 	'label': 'Member',
		// 	'fieldname':'member',
		// 	'fieldtype': 'data' 
		// }

	]
};
