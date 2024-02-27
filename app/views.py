from django.http import HttpResponse
from django.shortcuts import render
from app.game import Game
import json


def index(request):
    return render(request, "index.html")


def process(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    print("Processing request...")
    result = json.loads(request.body.decode("utf-8"))
    game = Game.from_dict(result["board"])
    game.make_move(result["row"], result["col"])
    return HttpResponse(json.dumps(game.state()), status=200)
