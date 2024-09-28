import frappe,json

@frappe.whitelist()
def insert_address(doc,add_details):
    doc=json.loads(doc)
    add_details=json.loads(add_details)

    validate_duplicate(doc)
    add = frappe.new_doc('Address')

    add.address_title = add_details.get('address_title')
    add.address_type = add_details.get('address_type')
    add.address_line1 = add_details.get('address_line1')
    add.city = add_details.get('city')

    add.append("links",{
        "link_doctype": doc.get("doctype"),
        "link_name" : doc.get("name") 
    })
    add.save()
    frappe.msgprint(f"Address Successfully Created for {doc.get('doctype')} - {doc.get('name')} !!")

def validate_duplicate(doc):
    if frappe.get_all("Dynamic Link",
                         filters={
                             "parenttype": "Address",
                             "link_doctype": doc.get("doctype"),
                             "link_name" : doc.get("name")
                         },
                         fields=["parent"]):
        frappe.throw(f"Address Already Exist for {doc.get('doctype')} - {doc.get('name')} !!")