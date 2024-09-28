# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BulkLibraryTransactionTool(Document):
	@frappe.whitelist()
	def get_party_name_based_on_type(self):
		member_field = "is_member"
		party_name = 'customer_name as party_name'
		
		if self.party_type == "Employee":
			member_field = "custom_is_member"
			party_name = "employee_name as party_name"
	
		return frappe.get_all(self.party_type,{member_field:1}, ['name as party', party_name])

	@frappe.whitelist()
	def create_library_member(self):
		self.set("library_member_items",[])
		count, lm_list = 0, []
		for row in self.party_items:
			self.make_library_member(row, count, lm_list)
		frappe.msgprint("Records created")
		return lm_list

	def make_library_member(self, row, count, lm_list):
		lm = frappe.new_doc("Library Member")
		lm.party_type = row.get("party_type")
		lm.party = row.get("party")
		lm.membership_type = frappe.db.get_single_value("Library Setting", "default_membership_type")

		try:
			lm.save()
			count += 1
			frappe.db.commit()
			self.add_library_member_items(lm)

		except Exception:
			frappe.db.rollback()
			frappe.throw(f"Error while creatig Library Membership for {row.party}")

	def add_library_member_items(self, lm):
		self.append("library_member_items",{
			"member_id": str(lm.name),
			"member_name": str(lm.member_name),
			"membership_type": str(lm.membership_type)
		})
