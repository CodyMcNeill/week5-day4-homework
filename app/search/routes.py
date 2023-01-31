from flask import render_template, request, redirect, url_for, Blueprint
from .forms import searchPoke
from ..models import Pokemon, db
from .services import get_poke_info

search = Blueprint('search', __name__)

@search.route('/pokedex', methods=['GET', 'POST'])
def pokedexPage():
    form = searchPoke()
    if request.method == 'POST':
        if form.validate_on_submit():
            search = form.searchBody.data.lower()
            data = get_poke_info(search)
            name = data['name']
            ability = data['ability']
            base_xp = data['base_xp']
            front_shiny = data['front_shiny']
            base_atk = data['base_atk']
            base_hp = data['base_hp']
            base_def = data['base_def']
            pokemon = Pokemon(name, ability, base_xp, front_shiny, base_atk, base_hp, base_def)
            pokemon.saveToDB()
            return render_template('search.html', name=name, ability=ability, base_xp=base_xp, front_shiny=front_shiny, base_atk=base_atk, base_hp=base_hp, base_def=base_def)
    return render_template('pokedex.html', form = form)