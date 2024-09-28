frappe.ui.form.on('Customer', {
    refresh(frm){
        
        if (frm.doc.is_member){
            cur_frm.add_custom_button("Library Member", function() {
                frappe.new_doc('Library Member', {
                    party_type: frm.doc.doctype,
                    party: frm.doc.name,
                    member_name: frm.doc.customer_name
                });
            }, "Create")
        }
    },

    
    
});