def test_attempt_parse_request_missing_content_type_raises_bad_request_error(
    client, snapshot
):
    response = client.post("/", data="")
    assert response.status_code == 400
    snapshot.assert_match(response.text)


def test_attempt_parse_non_json_request_raises_bad_request_error(client, snapshot):
    response = client.post("/", data="", headers={"content-type": "text/plain"})
    assert response.status_code == 400
    snapshot.assert_match(response.text)


def test_attempt_parse_non_json_request_body_raises_bad_request_error(client, snapshot):
    response = client.post("/", data="", headers={"content-type": "application/json"})
    assert response.status_code == 400
    snapshot.assert_match(response.text)


def test_attempt_parse_json_scalar_request_raises_graphql_bad_request_error(
    client, snapshot
):
    response = client.post("/", json="json string")
    assert response.status_code == 400
    snapshot.assert_match(response.text)


def test_attempt_parse_json_array_request_raises_graphql_bad_request_error(
    client, snapshot
):
    response = client.post("/", json=[1, 2, 3])
    assert response.status_code == 400
    snapshot.assert_match(response.text)
