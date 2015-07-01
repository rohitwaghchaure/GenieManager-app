# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "geniemanager"
app_title = "geniemanager"
app_publisher = "geniemanager"
app_description = "geniemanager"
app_icon = "octicon-file-directory"
app_color = "grey"
app_email = "rohit.w@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/geniemanager/css/geniemanager.css"
# app_include_js = "/assets/geniemanager/js/geniemanager.js"

# include js, css files in header of web template
# web_include_css = "/assets/geniemanager/css/geniemanager.css"
# web_include_js = "/assets/geniemanager/js/geniemanager.js"

# Home Pages
# ----------

fixtures = ['Custom Field']

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "geniemanager.install.before_install"
# after_install = "geniemanager.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "geniemanager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Company": {
		"validate" : "geniemanager.geniemanager.hooks_validate_methods.validate_company_methods"
	},
	"Quotation" : {
		"validate" : "geniemanager.geniemanager.hooks_validate_methods.validate_quotation_methods"
	},
	"Sales Order" : {
		"validate" : "geniemanager.geniemanager.hooks_validate_methods.validate_SalesOrder_methods"
	},
	"Sales Invoice": {
		"validate" : "geniemanager.geniemanager.hooks_validate_methods.validate_SalesInvoice_methods"
	}

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"geniemanager.tasks.all"
# 	],
# 	"daily": [
# 		"geniemanager.tasks.daily"
# 	],
# 	"hourly": [
# 		"geniemanager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"geniemanager.tasks.weekly"
# 	]
# 	"monthly": [
# 		"geniemanager.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "geniemanager.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "geniemanager.event.get_events"
# }

