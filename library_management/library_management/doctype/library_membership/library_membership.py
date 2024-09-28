# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def validate(self):
		pass
	def fach_membership_type(self):

		records = frappe.db.sql(f"""
			select membership_type
			from`tabLibrary Member`
			where member_name ='{self.meber_name}'
			""",as_dict=True)

