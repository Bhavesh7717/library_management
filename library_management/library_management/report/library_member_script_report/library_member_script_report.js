// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Member Script Report"] = {
	"filters": [
		{
			'label': 'Membership Type',
			'fieldname':'membership_type',
			'fieldtype': 'Select',
			'options':["", "Gold", "Silver", "Bronze"]
		},
		{
			'label': 'Enable',
			'fieldname':'enable',
			'fieldtype': 'Check' 
		}
		
	]
};
