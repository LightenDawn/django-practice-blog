from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "star-burst-stream",
        "image": "kanna1.png",
        "author": "Kirito",
        "date": date(2021, 7, 22),
        "title": "Mountain Hiking",
        "excerpt": "I can't imaging that you come to this floor, and your next enemy is me the chain of the Cony! Defend my attack, loser. The divine blaze!",
        "content": """
        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.

        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.

        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.
        """
    },
    {
        "slug": "ryujin-no-kenokurae",
        "image": "kanna.png",
        "author": "Genji",
        "date": date(2021, 3, 12),
        "title": "Asuna Busuna",
        "excerpt": "I can't imaging that you come to this floor, and your next enemy is me the chain of the Cony! Defend my attack, loser. The divine blaze!",
        "content": """
        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.

        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.

        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.
        """
    },
    {
        "slug": "jizz-on-my-pants",
        "image": "kana.png",
        "author": "Me",
        "date": date(2021, 1, 17),
        "title": "Cockroach",
        "excerpt": "I can't imaging that you come to this floor, and your next enemy is me the chain of the Cony! Defend my attack, loser. The divine blaze!",
        "content": """
        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.

        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.

        Associated with moderation, the word means not too much, not too little, but just the right amount. It typically refers
        to the etiquette of taking your share.
        """
    }
]

# Create your views here.

def get_date(post):
    return post["date"]

def starting_pages(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_datail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
