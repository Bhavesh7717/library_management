frappe.ui.form.on('Customer', {
    refresh(frm){
        
        if (frm.doc.is_member){
            cur_frm.add_custom_button("Address", function() {
                let d = new frappe.ui.Dialog({
                    title: 'Address details',
                    fields: [
                        {
                            label: 'Address Title',
                            fieldname: 'address_title',
                            fieldtype: 'Data'
                        },
                        {
                            "fieldname": "address_type",
                            "fieldtype": "Select",
                            "in_list_view": 1,
                            "in_standard_filter": 1,
                            "label": "Address Type",
                            "options": "Billing\nShipping\nOffice\nPersonal\nPlant\nPostal\nShop\nSubsidiary\nWarehouse\nCurrent\nPermanent\nOther",
                            "reqd": 1
                        },
                        {
                            label: 'Address Line 1',
                            fieldname: 'address_line1',
                            fieldtype: 'Data',
                            "reqd": 1
                        },
                        {
                            label: 'City/Town',
                            fieldname: 'city',
                            fieldtype: 'Data',
                            "reqd": 1
                        }
                    ],
                    size: 'small', // small, large, extra-large 
                    primary_action_label: 'Submit',
                    primary_action(values) {
                        // frappe.db.insert({

                        //     doctype: "Address",
                        //     address_title: values.address_title,
                        //     address_type: values.address_type,
                        //     address_line1: values.address_line1,
                        //     city: values.city
                        // });



                        frm.call({
                            "method":"library_management.library_management.doctype.bhavesh_customer.customer_address",
                            "args":{
                                doc: frm.doc,
                                address_details: values
                            },
                            callback(resp){
                                console.log(resp)
                            }
                        })
                        console.log(values);
                        d.hide();
                    }
                });
                
                d.show();
                
            }, "Create")
        }
    },

    
    
});