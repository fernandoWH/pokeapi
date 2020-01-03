from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from pokeapi.services import get_pokemons, get_fotos_pokemos, get_caracteristicas
import requests

def ver_todos(requests):
	pokemons= get_pokemons('http://pokeapi.co/api/v2/pokemon',0)
	diccionario={}
	datos={}
	n=0
	if pokemons:
		for pokemon in pokemons:
			n=n+1
			name= pokemon['name']
			url= pokemon['url']
			i=url[34]
			d=url[35]
			id_pokemon=i+d
			foto =get_fotos_pokemos(url)
			diccionario = { 'nombre':name, 'foto':foto, 'url':url, 'id_pokemon':id_pokemon}

			datos[n]= diccionario		

	return render (requests, 'ver_todos.html',{'pokemons':datos})

	
def ver_uno(requests, id_pokemon,nombre_pokemon):
	url='http://pokeapi.co/api/v2/pokemon/'+id_pokemon
	caracteristicas=get_caracteristicas(url)
	nombre=nombre_pokemon
	peso=caracteristicas.get('weight')
	altura=caracteristicas.get('height')
	datos= caracteristicas.get('types', [])
	chabilidades=caracteristicas.get('abilities', [])
	cmoves=caracteristicas.get('moves', [])
	tipos={}
	dic_tipo={}
	habilidades={}
	movimientos={}
	n=0
	n2=0
	n3=0
	if datos:
		for t in datos:
			n=n+1
			tipo=t['type']
			nombre_tipo=tipo['name']
			url_tipo=tipo['url']
			i=url_tipo[31]
			d=url_tipo[32]
			id_tipo=i+d
			tipos= {'tipo':nombre_tipo, 'id_tipo':id_tipo}
			dic_tipo[n]=tipos

	if chabilidades:
		for h in chabilidades:
			n2=n2+1
			habilidad=h['ability']
			habilidad=habilidad['name']
			habilidades[n2]= habilidad

	if cmoves:
		for m in cmoves:
			n3=n3+1
			movimiento=m['move']
			movimiento=movimiento['name']
			movimientos[n3]= movimiento

	foto=get_fotos_pokemos(url)

	return render (requests, 'ver_uno.html',{'nombre':nombre, 'peso':peso, 'foto':foto, 'altura':altura, 'tipos':dic_tipo, 'habilidades': habilidades, 'movimientos':movimientos})


def ver_tipo(requests, id_tipo):
	url='http://pokeapi.co/api/v2/type/'+id_tipo
	
	caracteristicas=get_caracteristicas(url)
	pokemons_tipo=caracteristicas.get('pokemon', [])
	pokemons={}
	datos={}
	n=0

	if pokemons_tipo:
		for pokemon in pokemons_tipo:
			n=n+1
			pokemon=pokemon['pokemon']
			name=pokemon['name']
			url= pokemon['url']
			i=url[34]
			d=url[35]
			id_pokemon=i+d
			foto =get_fotos_pokemos(url)
			pokemons = { 'nombre':name, 'foto':foto, 'url':url, 'id_pokemon':id_pokemon}

			datos[n]= pokemons

			if n==10:
				break
	return render (requests, 'ver_todos.html',{'pokemons':datos})