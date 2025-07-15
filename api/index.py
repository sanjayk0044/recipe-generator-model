from flask import Flask, request, jsonify
from api.services.gemini_service import generate_recipes
from api.services.mongodb_service import get_mongodb_service

app = Flask(__name__)

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
