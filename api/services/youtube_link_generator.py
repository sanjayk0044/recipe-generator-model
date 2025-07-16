import requests
from datetime import datetime, timedelta
# Constants
MIN_VIEWS = 10_000
DAYS_OLD = 180
def search_dailymotion_video(recipe_name):
    search_query = f"{recipe_name} food recipe"
    api_url = "https://api.dailymotion.com/videos"
    params = {
        "search": search_query,
        "fields": "title,url,views_total,created_time",
        "limit": 10,
        "sort": "visited"  # Sort by popularity (views)
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
    except Exception as e:
        print(f":x: API request failed for '{recipe_name}': {e}")
        return "No suitable video found"
    videos = response.json().get("list", [])
    cutoff_timestamp = (datetime.now() - timedelta(days=DAYS_OLD)).timestamp()
    for video in videos:
        views = video.get("views_total", 0)
        created = video.get("created_time", 0)
        if views >= MIN_VIEWS and created <= cutoff_timestamp:
            return video.get("url")
    return "No suitable video found"

def get_video_links_for_recipes(recipes):
    results = {}
    for recipe in recipes:
        print(f":mag: Searching Dailymotion for: '{recipe} food recipe'")
        video_url = search_dailymotion_video(recipe)
        results[recipe] = video_url
    return results
