from django.http import HttpResponse

from .models import Pokemon

def get_pokemon(request,pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_info = f"{pokemon.name} - {pokemon.type} - {pokemon.hp}"
    return HttpResponse(pokemon_info)

def get_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemon_list = "\n".join (f"{pokemon}" for pokemon in pokemons)
    return HttpResponse(pokemon_list)