def test_get_posts(http_session, api_base_url):
    """GET /posts should return a list of posts and status 200."""
    resp = http_session.get(f"{api_base_url}/posts")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_create_post(http_session, api_base_url):
    """POST /posts should accept a new post and return 201/201-like response."""
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = http_session.post(f"{api_base_url}/posts", json=payload)
    # jsonplaceholder returns 201
    assert resp.status_code in (201, 200)
    data = resp.json()
    assert data.get("title") == "foo"
    assert data.get("body") == "bar"
