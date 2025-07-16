from flask import Flask, request, jsonify
from flask_cors import CORS
from api.services.gemini_service import generate_recipes
from api.services.image_generation import fetch_images_from_duckduckgo
from api.services.youtube_link_generator import get_video_links_for_recipes

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

@app.route('/recipes', methods=['POST'])
def create_recipes():
    """
    POST endpoint to generate recipes based on user preferences
    
    Request body:
    - JSON object containing user preferences
    
    Returns:
    - JSON response with generated recipes
    """
    try:
        # Get preferences from request JSON body
        preferences = request.get_json() or {}
        
        # Generate recipes
        recipes = generate_recipes(preferences)
        
        # Return recipes without verification
        return jsonify(recipes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/images', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not isinstance(data, list):
            return jsonify({"error": "Request body must be a JSON array of recipe names"}), 400
            
        # Fetch images for each recipe name
        images = fetch_images_from_duckduckgo(data)
        
        # Return properly formatted JSON response
        return jsonify(images), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/youtube', methods=['POST'])
def generate_youtube_link():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not isinstance(data, list):
            return jsonify({"error": "Request body must be a JSON array of recipe names"}), 400
            
        # Fetch images for each recipe name
        youtube_links = get_video_links_for_recipes(data)
        
        # Return properly formatted JSON response
        return jsonify(youtube_links), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
