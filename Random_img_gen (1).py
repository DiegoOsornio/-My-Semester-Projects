import random
import time
import requests
from PIL import Image
from io import BytesIO

def open_image(url):


        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.show()


def get_random_movie_recommendation():


    movie_recommendations = [

        {
            "url": "https://tinyurl.com/mpzyvctu",
            "description": "Inception: A mind-bending thriller with stunning visuals and a complex plot. Highly recommended for fans of Christopher Nolan.",
            "source": {
                "website": "IMDb",
                "author": "Warner Bros. Pictures",
                "article_name": "Inception",
                "date": "2010",
                "license": "© Warner Bros. Pictures"  }   }, {
            "url": "https://tinyurl.com/bdz99ct9",
            "description": "Fullmetal Alchemist: Brotherhood (Movie Poster): While originally an anime, many enjoy the live action movie. A classic story with great characters and a compelling storyline.",
            "source": {
                "website": "IMDb",
                "author": "Warner Bros. Pictures Japan",
                "article_name": "Fullmetal Alchemist",
                "date": "2017",
                "license": "© Warner Bros. Pictures Japan"    }   },   {
            "url": "https://tinyurl.com/hhbeznz5",
            "description": "Attack on Titan (Movie Poster): A thrilling live action adaptation of the popular anime. Intense action and a dark, gripping story.",
            "source": {
                "website": "IMDb",
                "author": "Toho",
                "article_name": "Attack on Titan",
                "date": "2015",
                "license": "© Toho" }  },{
        "url": "https://tinyurl.com/28kj29at",
            "description": "Spy x Family (Movie Poster): A fun mix of comedy and action, the movie poster shows the lighthearted nature of the franchise.",
            "source": {
                "website": "IMDb",
                "author": "TOHO animation",
                "article_name": "Spy x Family Code: White",
                "date": "2023",
                "license": "© TOHO animation" } }, {
            "url": "https://tinyurl.com/4pyukmjr",
            "description": "Jujutsu Kaisen 0 (Movie Poster): A prequel to the popular anime series. Great animation and action-packed scenes.",
            "source": {
                "website": "IMDb",
                "author": "TOHO animation",
                "article_name": "Jujutsu Kaisen 0",
                "date": "2021",
                "license": "© TOHO animation"}  } ]
    selected_movie = random.choice(movie_recommendations)
    return selected_movie

def display_movie_recommendation():

    recommendation = get_random_movie_recommendation()
    url = recommendation["url"]
    description = recommendation["description"]
    source = recommendation["source"]

    print("Loading your movie recommendation...")
    time.sleep(1)

    open_image(url)

    print("\nRecommendation:")
    print(description)
    print("\nSource:")
    print(f"Website: {source['website']}")
    print(f"Author: {source['author']}")
    print(f"Article Name: {source['article_name']}")
    print(f"Date: {source['date']}")
    print(f"License: {source['license']}")

def main():
    """
    Main function to run the movie recommendation program.
    """
    print("Welcome to the Random Movie Recommendation Program!")
    print("I will recommend a random movie for you to watch.")
    print("Press Enter to get a recommendation, or type 'exit' to quit.")

    while True:
        user_input = input("\n")
        if user_input.lower() == "exit":
            print("Thank you for using the program!")
            break
        else:
            display_movie_recommendation()

if __name__ == "__main__":
    main()
