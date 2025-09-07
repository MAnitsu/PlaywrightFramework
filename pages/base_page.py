# pages/base_page.py

from playwright.sync_api import Page

class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.ab_test = page.locator('a[href="/abtest"]')
        self.add_remove_elements = page.locator('a[href="/add_remove_elements"]')
        self.basic_auth = page.locator('a[href="/basic_auth"]')
        self.broken_images = page.locator('a[href="/broken_images"]')
        self.challenging_dom = page.locator('a[href="/challenging_dom"]')
        self.checkboxes = page.locator('a[href="/checkboxes"]')
        self.context_menu = page.locator('a[href="/context_menu"]')
        self.digest_auth = page.locator('a[href="/digest_auth"]')
        self.disappearing_elements = page.locator('a[href="/disappearing_elements"]')
        self.drag_and_drop = page.locator('a[href="/drag_and_drop"]')
        self.dropdown = page.locator('a[href="/dropdown"]')
        self.dynamic_content = page.locator('a[href="/dynamic_content"]')
        self.dynamic_controls = page.locator('a[href="/dynamic_controls"]')
        self.dynamic_loading = page.locator('a[href="/dynamic_loading"]')
        self.entry_ad = page.locator('a[href="/entry_ad"]')
        self.exit_intent = page.locator('a[href="/exit_intent"]')
        self.file_download = page.locator('a[href="/download"]')
        self.file_upload = page.locator('a[href="/upload"]')
        self.floating_menu = page.locator('a[href="/floating_menu"]')
        self.forgot_password = page.locator('a[href="/forgot_password"]')
        self.form_authentication = page.locator('a[href="/login"]')
        self.frames = page.locator('a[href="/frames"]')
        self.geolocation = page.locator('a[href="/geolocation"]')
        self.horizontal_slider = page.locator('a[href="/horizontal_slider"]')
        self.hovers = page.locator('a[href="/hovers"]')
        self.infinite_scroll = page.locator('a[href="/infinite_scroll"]')
        self.inputs = page.locator('a[href="/inputs"]')
        self.jquery_ui_menus = page.locator('a[href="/jqueryui/menu"]')
        self.javascript_alerts = page.locator('a[href="/javascript_alerts"]')
        self.javascript_error = page.locator('a[href="/javascript_error"]')
        self.key_presses = page.locator('a[href="/key_presses"]')
        self.large_dom = page.locator('a[href="/large"]')
        self.multiple_windows = page.locator('a[href="/windows"]')
        self.nested_frames = page.locator('a[href="/nested_frames"]')
        self.notification_message = page.locator('a[href="/notification_message"]')
        self.redirect_link = page.locator('a[href="/redirector"]')
        self.secure_file_download = page.locator('a[href="/download_secure"]')
        self.shadow_dom = page.locator('a[href="/shadowdom"]')
        self.shifting_content = page.locator('a[href="/shifting_content"]')
        self.slow_resources = page.locator('a[href="/slow"]')
        self.sortable_data_tables = page.locator('a[href="/tables"]')
        self.status_codes = page.locator('a[href="/status_codes"]')
        self.typos = page.locator('a[href="/typos"]')
        self.wysiwyg_editor = page.locator('a[href="/tinymce"]')

    def select_link(self):
        pass