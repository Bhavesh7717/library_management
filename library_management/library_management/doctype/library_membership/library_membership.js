// Copyright (c) 2024, Tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {

	from_date:function(frm){

		let mtype;
		let fromdate=frm.doc.from_date;	
		frappe.db.get_value('Library Member',{member_name: frm.doc.member_name},'membership_type')
		.then(
			(r)=>{
				if(r.message){
					mtype=r.message.membership_type;
					// frappe.msgprint(mtype);

					const gold="Gold";
					const silver="Silver";
					const bronze="Bronze";
					
					var todate;
					// console.log('aaaaaaaaaaaaaaaaaa',mtype,gold,mtype==gold,typeof mtype, typeof gold);

					if (mtype==gold){
						console.log('aaaaa');
						todate=frappe.datetime.add_months(fromdate,12);
					}
					else if (mtype==silver){
						todate=frappe.datetime.add_months(fromdate,6);
					}
					else if (mtype==bronze){
						todate=frappe.datetime.add_months(fromdate,3);
					}
					// else{
					// 	todate=''
					// }
					frm.set_value('to_date',todate);
			
				}
			}
		);
	}

});
