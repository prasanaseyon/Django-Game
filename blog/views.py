import json
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    DetailView,
    DeleteView,
)
from django.urls import reverse
from django.views import View

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



#class GameView(View):
    #def get(self, request, pk):
        #url = reverse('blog-view', args=[pk])
        #return render(request, 'blog/game_view.html')


#def game(request):
    # Read the game.html file and encode its contents
    #with open('game.html', 'r') as file:
        #game_html_content = file.read()

    # Load the existing JSON data from the file
    #with open('posts.json', 'r') as file:
        #data = json.load(file)

    # Assign the game HTML content to the first object in the JSON data
    #data[0]['game_html'] = game_html_content

    # Write the modified JSON data back to the file
    #with open('posts.json', 'w') as file:
        #json.dump(data, file)
    #url = reverse('blog-game')
    #return render(request, 'blog/game.html')

def game(request):
    model = Post
        


import json

def play_game(request, game_id):
    # Read the JSON file containing the game data
    with open('posts.json') as json_file:
        game_data = json.load(json_file)

    # Find the game with the matching game_id
    game = None
    for game_obj in game_data:
        if game_obj.get('user_id') == 1 and game_obj.get('url') == f"http://localhost:8000/courses/{game_id}/?format=json":
            game = game_obj
            break

    # Render the template with the game data
    return render(request, 'blog/game.html', {'game': game})



class PostDetailView(DetailView):
    model = Post
    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})
   

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

