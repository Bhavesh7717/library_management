import frappe,json

@frappe.whitelist()
def customer_address(doc,address_details):
    doc= json.loads(doc)
    address_dis= json.loads(address_details)
    
    duplicate_address(doc)

    address_doc= frappe.new_doc("Address")
    address_doc.address_title= address_dis.get("address_title")
    address_doc.address_type= address_dis.get("address_type")
    address_doc.address_line1= address_dis.get("address_line1")
    address_doc.city= address_dis.get("city")

    address_doc.append("links",{
        "link_doctype":doc.get("doctype"),
        "link_name":doc.get("name")
    })

    address_doc.save()
    
def duplicate_address(doc):
    if frappe.get_all("Dynamic Link",filters={"parenttype":"Address","link_doctype": doc.get("doctype"), "link_name": doc.get("name")},fields=["parent"]):
        frappe.throw(f"""Address already exist {doc.get('doctype')} for customer {doc.get("name")}""")

