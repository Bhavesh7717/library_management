// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Book', {
	no_of_copies: function(frm) {
		frm.set_value('stock_balance',frm.doc.no_of_copies);
	}
});
