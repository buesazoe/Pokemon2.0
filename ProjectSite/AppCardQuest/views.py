from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from AppCardQuest.models import PokemonCard, Collection, Trainer
from AppCardQuest.forms import TrainerForm, CollectionForm
from django.urls import reverse_lazy
import json

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'base'  # The name used in the template for the list of objects
    template_name = "base.html"   # The template file to be rendered

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data you want to pass to the template
        return context

class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemoncard.html"
    # Update this with the correct path to your JSON file
    json_file_path = 'data/pokemon_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context

    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])


class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainer.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TrainerList, self).get_queryset(*args, **kwargs)
        return qs.order_by('name')



class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')


class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_delete.html'
    success_url = reverse_lazy('trainer-list')


class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(CollectionList, self).get_queryset(*args, **kwargs)
        return qs


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection-list')


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection-list')


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_delete.html'
    success_url = reverse_lazy('collection-list')
