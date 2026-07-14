import frappe

def test(doc, method=None):
    """
    Triggers automatically when a Sales Invoice is validated (on Save/Submit).
    """
    # Just a simple check to prove the hook works
    frappe.msgprint(
        title="Validation Triggered",
        indicator="blue",
        message=f"The test function in marvin_custom has successfully intercepted Invoice: {doc.name or 'Draft'}"
    )
