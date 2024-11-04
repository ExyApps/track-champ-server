class TestLoginEndpoint:
	url = '/auth/login'

	def test_login_account_does_not_exist(self, client):
		response = client.post(
			self.url,
			json={
				'email': 'test@email.com',
				'password': 'test',
			}
		)

		assert response.status_code == 401


	def test_login_wrong_combination(self, client, db_session, user_model, email, invalid_lower_password):
		db_session.add(user_model)
		db_session.commit()

		response = client.post(
			self.url,
			json={
				'email': email,
				'password': invalid_lower_password,
			}
		)

		assert response.status_code == 401


	def test_login_success(self, client, db_session, user_model, email, password):
		db_session.add(user_model)
		db_session.commit()

		response = client.post(
			self.url,
			json={
				'email': email,
				'password': password,
			}
		)

		assert response.status_code == 200


	def test_login_already_logged_in(self, client, db_session, user_model, email, password):
		db_session.add(user_model)
		db_session.commit()

		r = client.post(self.url, json={'email': email, 'password': password})
		response = client.post(self.url, json={'email': email, 'password': password}, headers=r.headers)

		assert response.status_code == 307
