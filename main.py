import random

favorite_anime = input("select your anime")
print("Alex's favorite anime is" + favorite_anime)

favorite_anime_list = ("One Piece", "Jojos Bizarre Adventure", "Mushishi", "Golden Kamuy", "Gintama")
print("Alex's favorite anime is " + random.choice(favorite_anime_list))
