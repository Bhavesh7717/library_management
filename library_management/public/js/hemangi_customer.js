frappe.ui.form.on('Customer', {
    refresh(frm){
        
        if (frm.doc.is_member){
            cur_frm.add_custom_button("hemangi_address", function() {
                
                let d = new frappe.ui.Dialog({
                    title: 'Address details',
                    fields: [
                        {
                            label: 'Address Title',
                            fieldname: 'address_title',
                            fieldtype: 'Data'
                        },
                        {
                            label: 'Address Line 1',
                            fieldname: 'address_line1',
                            fieldtype: 'Data',
                            reqd: 1
                        },
                        {
                            fieldname: 'col_break',
                            fieldtype: 'Column Break'
                        },
                        {
                            label: 'Address Type',
                            fieldname: 'address_type',
                            // fieldtype: 'Data'
                            fieldtype: 'Select',
                            options: ['Billing','Shipping'],
                            reqd: 1
                        },
                        {
                            label: 'City/Town',
                            fieldname: 'city',
                            fieldtype: 'Data',
                            reqd: 1
                        }
                        
                    ],
                    size: 'small', // small, large, extra-large 
                    primary_action_label: 'Submit',
                    primary_action(values) {
                        // console.log(values['address_type']);
                            
                        frm.call({
                            "method": "library_management.library_management.doctype.hem_customer_address.insert_address",
                            "args": {
                                doc : frm.doc,
                                add_details : values
                            },
                            callback:function(r){
                                console.log(r);
                                
                            }
                        })

                        d.hide();

                        // frappe.new_doc('Address',{
                        //     // address_title: values['address_title'],         // can write like this also
                        //     address_title: values.address_title,
                        //     address_type: values.address_type,
                        //     address_line1: values.address_line1,
                        //     city: values.city,
                        // });

                        // frappe.db.insert({
                        //     doctype: 'Address',
                        //     address_title: values.address_title,
                        //     address_type: values.address_type,
                        //     address_line1: values.address_line1,
                        //     city: values.city,
                        // });

                        // d.hide();
                    }
                });
                
                d.show();                
            }, "Create")
            
        }
    },
});