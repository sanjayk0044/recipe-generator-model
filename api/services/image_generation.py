from ddgs import DDGS
import time

def fetch_images_from_duckduckgo(recipe_names: list):
    image_urls = []
    for recipe_name in recipe_names:
        try:
            results = DDGS().images(query=recipe_name, num_results=1)  # Fetch 1 image
            if results:
                # Extract the URL for the image
                image = results[0]['image']  # Get the first image URL
                image_urls.append(image)  # Append the image URL directly
            else:
                print(f"No images found in DuckDuckGo search for '{recipe_name}'")
                image_urls.append(None)  # Append None if no image found
        except Exception as e:
            print(f"An error occurred with DuckDuckGo search for '{recipe_name}': {e}")
            image_urls.append(None)  # Append None on exception
        time.sleep(0.5)  # Introduce a delay of 500 milliseconds
    return image_urls