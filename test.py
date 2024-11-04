import requests

r = requests.post(
	'http://localhost:5000/auth/register',
	json={
        'first_name': 'Andre',
        'last_name': 'Oliveira',
		'email': 'andre@email.com',
        'gender': 'Masculino',
        'date': '2000-01-01',
		'password': 'Password1!',
	}
)

print(r.status_code)
print(r.json())

r = requests.post(
	'http://localhost:5000/auth/login',
	json={
		'email': 'andre@email.com',
		'password': 'Password1!',
	}
)

print(r.status_code)
print(r.json())