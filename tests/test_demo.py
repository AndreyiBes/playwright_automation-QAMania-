import allure


@allure.title('test_wait_more_30_sec')
def test_wait_more_30_sec(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_page.open_page_after_wait(3)
    assert desktop_app_auth.demo_page.check_wait_page()


@allure.title('test_ajax')
def test_ajax(desktop_app_auth):
    desktop_app_auth.navigate_to ( 'Demo pages' )
    desktop_app_auth.demo_page.open_page_and_wait_ajax(6)
    assert 6 == desktop_app_auth.demo_page.get_ajax_responses_count()


@allure.title('test_handlers')
def test_handlers(desktop_app_auth):
    desktop_app_auth.navigate_to ( 'Demo pages' )
    desktop_app_auth.demo_page.click_new_page_button()
    desktop_app_auth.demo_page.inject_js()
    desktop_app_auth.navigate_to ( 'Test Cases' )
    assert desktop_app_auth.test_cases.check_test_exist('Check update test')



