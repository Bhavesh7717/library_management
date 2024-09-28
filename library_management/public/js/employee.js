// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee', {
    refresh(frm){
        console.log("@@@@@@@@@@@")
        if (frm.doc.custom_is_member){
            cur_frm.add_custom_button("Library Member", function() {
                frappe.new_doc('Library Member', {
                    party_type: frm.doc.doctype,
                    party: frm.doc.name,
                    member_name: frm.doc.employee_name
                });
            }, "Create")
        }
    },
});
