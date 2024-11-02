import requests

r = requests.post(
	'http://localhost:5000/auth/login',
	json={
		'email': 'andre@email.com',
		'password': 'okok',
	}
)

print(r.status_code)
print(r.json())