import frappe, json

@frappe.whitelist()
def create_customer_address(doc, address_details):
    # print(type(doc),address_details)
    doc= json.loads(doc)
    address_dict = json.loads(address_details)
    # print(type(doc),address_details)
    validate_duplicate_address(doc, address_details)
    address_doc = frappe.new_doc("Address")
    address_doc.address_title = address_dict.get("address_title")
    address_doc.address_type = address_dict.get("address_type")
    address_doc.address_line1 = address_dict.get("address_line1")
    address_doc.city = address_dict.get("city")
    
    address_doc.append("links",{
        "link_doctype": doc.get("doctype"),
        "link_name": doc.get("name"),
    })
    address_doc.save()
    frappe.msgprint("Address Create <b>{}</b>".format(address_doc.name))

def validate_duplicate_address(doc, address_details):
    for d in frappe.get_all("Dynamic Link",filters={"parenttype":"Address","link_doctype": doc.get("doctype"), "link_name": doc.get("name")},fields=["parent"]):
        frappe.throw(f"""Address already exist {d.parent} for customer {doc.get("name")}""")
    # if frappe.db.count("Dynamic Link",filters={"parenttype":"Address","link_doctype": doc.get("doctype"), "link_name": doc.get("name")}):
    #     frappe.throw(f"""Address already exist for customer {doc.get("name")}""")