import requests

def get_pokemons(url, offset):

	args= {'offset':offset} if offset else {}

	response= requests.get(url, params=args)

	if response.status_code==200:

		payload =response.json()
		results= payload.get('results', [])

		return results

def get_fotos_pokemos(url):

	response= requests.get(url)

	if response.status_code==200:

		payload =response.json()
		results= payload.get('sprites', [])
		foto = results['front_default']

		return foto

def get_caracteristicas(url):
	response= requests.get(url)

	if response.status_code==200:

		payload =response.json()
		results= payload.get('sprites', [])
		

		return payload