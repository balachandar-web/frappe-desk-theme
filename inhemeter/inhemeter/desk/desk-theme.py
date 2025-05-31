import frappe

@frappe.whitelist()
def switch_theme(theme):
	themes = ["Dark", "Light", "Automatic", "Green", "Lavender", "Ocean", "Sunset"]
	if theme in themes:
		doc = frappe.get_doc("User", frappe.session.user)
		doc.desk_theme = theme
		doc.save()
