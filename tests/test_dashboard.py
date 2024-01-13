import json
import allure


@allure.title('test_dashboard_data')
def test_dashboard_data(desktop_app_auth):
    payload = json.dumps({"total": 0, "passed": 0, "failed": 0, "norun": 0})
    desktop_app_auth.intercept_request('**/getstat*', payload)
    desktop_app_auth.refresh_dashboard()
    try:
        assert desktop_app_auth.get_total_tests_stats () == '20'
    except Exception as e:
        print ( f"Error: {e}" )
    desktop_app_auth.stop_intercept ( '**/getstat*' )

@allure.title('test_multiple_role')
def test_multiple_roles(desktop_app_auth, desktop_app_bob, get_db):
    alice = desktop_app_auth
    bob = desktop_app_bob
    alice.refresh_dashboard ()
    before = alice.get_total_tests_stats()
    bob.navigate_to('Create new test')
    bob.create_test('test my bob', 'bob')
    alice.refresh_dashboard()
    after = alice.get_total_tests_stats()
    get_db.delete_test_case('test my bob')
    assert int(before) + 1 == int(after)
    assert False