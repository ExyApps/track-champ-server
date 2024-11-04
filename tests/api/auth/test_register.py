class TestRegisterEndpoint:
	url = '/auth/register'

	def test_register_success(self, client, db_empty, register_payload):
		r = client.post(self.url, json=register_payload)

		assert r.status_code == 201

	
	def test_register_email_in_use(self, client, db_with_user, register_payload):
		r = client.post(self.url, json=register_payload)

		assert r.status_code == 409

	
	def test_register_already_logged_in(self, client, db_with_user, login_payload):
		r = client.post('auth/login', json=login_payload)
		r = client.post(self.url, json={}, headers = r.headers)

		assert r.status_code == 307