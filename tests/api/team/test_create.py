class TestCreateEndpoint:
    url = 'team/create'

    def test_delete_successful(self, client, db_with_user, login_payload, team_payload):
        r = client.post('auth/login', json=login_payload)
        r = client.post(self.url, json=team_payload, headers=r.headers)

        assert r.status_code == 201

    
    def test_create_without_session(self, client, db_with_user, team_payload):
        r = client.post(self.url, json=team_payload)

        assert r.status_code == 307