// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bulk Library Transaction Tool', {
	
	party_type(frm) {
		$(".library_member_items-add-row").hide();
		frm.call({
			"method": "get_party_name_based_on_type",
			"doc": frm.doc,
			callback(resp) {
				$.each(resp.message || [], function (i, dict_value) {
					var row = frm.add_child("party_items");
					row.party_type = frm.doc.party_type;
					row.party = dict_value['party'];
					row.party_name = dict_value['party_name'];
				})
				frm.refresh_field("party_items");
			}
		})
	},
	clear_party_items(frm) {
		frm.set_value("party_items", [])
	},
	create_library_member(frm) {
		frm.call({
			"method": "create_library_member",
			"doc": frm.doc,
			callback(resp){
				frm.refresh_field("library_member_items");
			}
		})
	},
	onload: function(frm) {
        frm.fields_dict['library_member_items'].grid.add_new_row = false;
        frm.fields_dict['library_membership_items'].grid.add_new_row = false;
    },

	
});
