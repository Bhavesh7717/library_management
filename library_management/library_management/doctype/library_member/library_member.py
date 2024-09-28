# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	
	def before_insert(self):
		self.member_name = frappe.db.get_value(self.party_type, self.party, "employee_name" if self.party_type == "Employee" else "customer_name")
		self.validate_duplicate_party()

	def validate_duplicate_party(self):
		
		records = frappe.db.sql(f"""
			select name
			from`tabLibrary Member`
			where party_type = '{self.party_type}' and party ='{self.party}'
			""",as_dict=True)
		if records:
			frappe.throw("Member alredy exist!!!!&nbsp<a href='WWW.Google.com'>show member</a>")

	
		
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def filter_employee_list(doctype, txt, searchfield, start, page_len, filters):
	# doctypes = frappe.get_hooks("period_closing_doctypes")
	# if txt:
	# 	doctypes = [d for d in doctypes if txt.lower() in d.lower()]
	# return [(d,) for d in set(doctypes)]
	condition = ""
	if filters:
		condition += "WHERE"
		condition+= f" custom_is_member = '{filters.get('custom_is_member')}' AND "
		condition+= f" status = '{filters.get('status')}'"
	print(condition)
	return frappe.db.sql(f"""select name, employee_name from `tabEmployee` {condition}""", debug=1)
	# frappe.get_all("Employee",fields=["name"])