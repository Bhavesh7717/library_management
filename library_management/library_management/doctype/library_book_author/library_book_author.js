// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Book Author', {
	validate: function(frm) {
		if(frm.doc.middle_name){
			frm.set_value('full_name',frm.doc.first_name + " "+ frm.doc.middle_name+" "+frm.doc.last_name )
		}
		else{
			frm.set_value('full_name',frm.doc.first_name + " "+frm.doc.last_name )
		}
		frm.add_custom_button("Library Book", function() {
			// console.log(frm.doc.full_name);
				
			frappe.new_doc('Library Book',{
				author:frm.doc.name,
				
			})

		})
	}
});
