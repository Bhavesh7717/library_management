// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt


frappe.ui.form.on('Library Member', {
	onload: function(frm) {
		if (frm.doc.__islocal){
			frappe.db.get_value("Library Setting", {"name": "Library Setting"}, "default_membership_type", (r) => {
				frm.set_value("membership_type", r.default_membership_type)
			});
		}
	},
	setup(frm){
		frm.set_query("party", function(){
			if (frm.doc.party_type == "Employee"){
				return {
					query:"library_management.library_management.doctype.library_member.library_member.filter_employee_list",
					filters:{
						"custom_is_member":1,
						"status":"Active"
					}
				}
			}
			return {
				filters:{
					"is_member":1
				}
			}
			
		})
	},
	refresh:function(frm){
		frm.add_custom_button("Library Membership",function(){
		
				frappe.new_doc('Library Membership',{
					member:frm.doc.name,
					member_name:frm.doc.member_name,
					// "from_date":"20-09-2024"
					// to_date:today()
				

			})
	
		})
	}	
})