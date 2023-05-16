import json
from django.contrib.auth.models import User
from .models import Post

def fetch_games_from_json():
    with open('games.json', 'r') as file:
        games_data = json.load(file)

    for game in games_data:
        user_id = game.get('user_id')
        url = game.get('url')
        image_url = game.get('image_url')
        name = game.get('name')
        language = game.get('language')
        price = game.get('price')
        game_html = game.get('game_html')

        author, _ = User.objects.get_or_create(id=user_id)

        post = Post(
            name=name,
            language=language,
            price=price,
            image_url=image_url,
            game_html=game_html,
            author=author
        )

        post.save()
