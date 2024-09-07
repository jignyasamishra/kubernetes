from flask import Flask
import logging
import random

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    # Generate a random number
    random_number = random.randint(1, 100)
    
    # Log the request
    logger.info(f"Request received. Generated random number: {random_number}")
    
    # Randomly log warnings or errors
    if random_number < 10:
        logger.warning("Warning: Generated number is less than 10")
    elif random_number > 90:
        logger.error("Error: Generated number is greater than 90")
    
    return f"Hello, World! Random number: {random_number}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)