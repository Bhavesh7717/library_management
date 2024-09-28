# Copyright (c) 2024, Tushar and contributors
# For license information, please see license.txt

from datetime import datetime,timedelta
import frappe,json
from frappe import _
from frappe.model.document import Document
from frappe.query_builder import Order

class LibraryBookIssue(Document):
	def validate(self):
		pass

	def on_submit(self):
		now_stock=self.fetch_stock()

		if now_stock==0:
			frappe.throw('Book Stock Not Available!!')
		else:
			self.new_stock_ledger(now_stock,-1)

	def fetch_stock(self):	
		if not frappe.db.get_all('Library Stock Ledger',{'library_book': self.library_book}):
			copy=frappe.db.get_value("Library Book",{'name': self.library_book},['no_of_copies'])
			return copy
		else:
			stock=frappe.db.get_all("Library Stock Ledger",
							{'library_book': self.library_book}
						,['stock_balance']
						,order_by="date desc",limit=1)
			return stock[0].stock_balance

	def on_update_after_submit(self):
		frappe.msgprint('on-update')
			
		if self.is_return:
			frappe.msgprint('return checked!!')
			self.returned_on=datetime.now()
			frappe.msgprint(f'{self.returned_on}')
			now_stock=self.fetch_stock()
			self.new_stock_ledger(now_stock,1)
			
	def on_cancel(self):
		if self.is_return:
			frappe.throw("You can not cancel document after return!")
		else:		
			now_stock=self.fetch_stock()
			self.new_stock_ledger(now_stock,1)

	@frappe.whitelist()
	def ahed(self):
		now_stock=self.fetch_stock()
		self.new_stock_ledger(now_stock,-1)
		frappe.db.commit()

	def new_stock_ledger(self,now_stock,qty):
		stock_doc = frappe.new_doc("Library Stock Ledger")
		stock_doc.date = datetime.now()
		stock_doc.library_member = self.member
		stock_doc.library_book = self.library_book
		stock_doc.stock_balance = now_stock + qty	
		stock_doc.book_qty = qty
		stock_doc.save()		
		# frappe.db.commit()
		frappe.msgprint(f'ledger created for {qty} !!!')
	






# @frappe.whitelist()
# def set_book_stock(doc,today):

# 	if doc:
# 		frappe.msgprint('if doc----')
# 		doc=json.loads(doc)
# 		book=doc.get('library_book')
# 		now_stock=fetch_copy(book) # function2 call
	
# 		if now_stock<=0:
# 			# frappe.msgprint('now stock -->0 ----')
# 			# frappe.throw('Book Stock Not Available!')
# 			raise Exception("Book Stock Not Available!")
# 			# return 'Book Stock Not Avilable'
# 		else:
# 			# frappe.msgprint('----saved--')
# 			stock_doc = frappe.new_doc("Library Stock Ledger")
# 			stock_doc.date = today,
# 			stock_doc.library_member = doc.get('member'),
# 			stock_doc.library_book = doc.get('library_book'),

# 			if doc.get('is_return'):	
# 				qty=1
# 			else:
# 				qty=-1
				
# 			stock_doc.book_qty = qty
# 			stock_doc.save()		

# 			frappe.db.set_value('Library Stock Ledger',stock_doc.name,'stock_balance',now_stock+qty)
# 			frappe.db.commit()
			
# 			return {"status": "success"}
# 	else:
# 		return 0
	
# def fetch_copy(book):
# 	if not frappe.db.get_value("Library Stock Ledger",{'library_book': f'{book}'},['library_book']):         # first transaction
# 		copy=frappe.db.get_value("Library Book",{'name':f"{book}"},'no_of_copies')
# # else:       # repeat transaction
# 		pre_stock=frappe.db.get_value("Library Stock Ledger",   # doctype
# 							{'library_book':f"{book}"},      # filters
# 							"stock_balance",          # fetch
# 							order_by="Date DESC"
# 							)
# 		frappe.msgprint(f'----return stock--> {pre_stock}')
# 		return pre_stock