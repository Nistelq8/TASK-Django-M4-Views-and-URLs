from django.http import HttpResponse

from .models import Pokemon

def get_pokemon(request,pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(pokemon)

def get_pokemons(request):
    pokemons = Pokemon.objects.all()
    print(pokemons)
    return HttpResponse(pokemons)