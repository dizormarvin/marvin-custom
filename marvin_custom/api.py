import frappe

def test(doc, method=None):
    # This runs securely in the backend automatically!
    frappe.msgprint("Validation Triggered")