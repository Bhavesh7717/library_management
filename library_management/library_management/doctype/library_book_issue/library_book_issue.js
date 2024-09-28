// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Book Issue', {
	
	validate:function(frm){
		
		var today_date, due_date,re_date;

		today_date=frappe.datetime.get_today();
		frm.set_value('issue_date',today_date);
		console.log(frm.doc.issue_date);
		
		due_date=frappe.datetime.add_days(today_date,10);
		frm.set_value('due_date',due_date);
	
		
		frm.set_value('returned_on',"");
		console.log(frm.doc.returned_on);
	},

refresh:function(frm){
	if(frm.doc.is_return){
		frm.add_custom_button("Amend",function(){

			frm.call({
				"method":"ahed",
				// "args":{
				// 	doc: frm.doc,
				// },
				"doc":frm.doc,
				callback(resp){
					console.log(resp);
				}
			})
		})
	}
		
	}

});
