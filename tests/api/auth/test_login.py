class TestLoginEndpoint:
	url = '/auth/login'

	def test_login_account_does_not_exist(self, client, login_payload):
		response = client.post(self.url, json=login_payload)

		assert response.status_code == 401


	def test_login_wrong_combination(self, client, db_with_user, invalid_login_payload):
		response = client.post(self.url, json=invalid_login_payload)

		assert response.status_code == 401


	def test_login_success(self, client, db_with_user, login_payload):
		response = client.post(self.url, json=login_payload)

		assert response.status_code == 200


	def test_login_already_logged_in(self, client, db_with_user, login_payload):
		r = client.post(self.url, json=login_payload)
		response = client.post(self.url, json=login_payload, headers=r.headers)

		assert response.status_code == 307
