# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "theme_1"
app_title = "theme_1"
app_publisher = "Pranav C"
app_description = "Theme v13"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pranav.chandran@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/theme_1/images/theme_1.png"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/theme_1/css/theme_1_app.css"
# app_include_js = "/assets/theme_1/js/theme_1.js"

# include js, css files in header of web template
web_include_css = "/assets/theme_1/css/theme_1_web.css"
# web_include_js = "/assets/theme_1/js/theme_1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "theme_1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

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

# before_install = "theme_1.install.before_install"
# after_install = "theme_1.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "theme_1.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"theme_1.tasks.all"
# 	],
# 	"daily": [
# 		"theme_1.tasks.daily"
# 	],
# 	"hourly": [
# 		"theme_1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"theme_1.tasks.weekly"
# 	]
# 	"monthly": [
# 		"theme_1.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "theme_1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "theme_1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "theme_1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

