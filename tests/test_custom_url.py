def test_url_and_status_code_via_cli(make_get_request, get_status_code):
    assert make_get_request.status_code == int(get_status_code)
