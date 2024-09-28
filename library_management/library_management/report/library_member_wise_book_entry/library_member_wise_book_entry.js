// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Member Wise Book Entry"] = {
	"filters": [
		{
			'label': 'Member',
			'fieldname' : 'member',
			'fieldtype' : 'MultiSelectList',
			'get_data':function(){
				return  frappe.db.get_link_options('Library Member')
			}
		},
		{
			'fieldname': 'Library Book',
			'label': 'library_book',
			'fieldtype': 'Link',
			'options': 'Library Book'
		},
	],
	formatter: (value, row, column, data, default_formatter) => {
		value = default_formatter(value, row, column, data);

		if(column.fieldname === "book_qty" && data.book_qty){
			if(data.book_qty == 1){
				value = `<div style="color:#00ff00">${value}</div>`;
			}
			else{
				value = `<div style="color:#ff0000">${value}</div>`;
			}
			
		}
		return value;
	}
};
