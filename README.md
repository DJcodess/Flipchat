# Fashion Product Recommendation Chatbot for Flipkart

## Overview

This chatbot is designed to provide fashion product recommendations using data from Flipkart's catalog. It utilizes a combination of machine learning techniques and openAI models to understand user preferences and suggest relevant fashion items available on Flipkart's platform.

## Features

- **Product Recommendation:** The chatbot leverages advanced algorithms to recommend fashion products based on user input and preferences. Users can describe their preferences, and the chatbot will provide tailored suggestions.

- **Query Interpretation:** The chatbot uses NLP to interpret user queries. Users can input descriptions, styles, occasions, or any relevant information about the type of fashion product they are looking for.

## How to Use

1. **Input Query:** Start a conversation with the chatbot by sending a text query describing your fashion preferences. For example: "I'm looking for casual summer dresses."

3. **Receive Recommendations:** Based on the information you provided, the chatbot will generate and display a list of recommended fashion products available on Flipkart. Each recommendation will include product details, images, prices, and links to the product page.

4. **Explore Recommendations:** Browse through the recommendations and click on the product links to view more details or make a purchase on Flipkart's platform.

## Running the Chatbot Locally

Follow these steps to run the chatbot on your local machine:

### Prerequisites

1. Make sure you have Python installed. You can download it from the official [Python website](https://www.python.org/downloads/).

2. Clone this repository to your local machine using the following command:
   
   ```bash
   git clone https://github.com/DJcodess/Chatbot.git
   ```

### Install the required dependencies
Install the required dependencies using pip:|
```bash
  pip install -r requirements.txt
```

## Run the Chatbot

1. Replace the openAI key with your openAI api key in dbsetup.py
2. Make sure a local instance of Redis Stack is up and running
3. run the dbsetup.py first to setup the local redis database.
4. In the project directory, locate the main Python file (app.py).
5. Run the chatbot application using the following command:
```bash
python app.py
```
The chatbot should now be running locally. Open your web browser and visit http://localhost:5000 to interact with the chatbot.

##  Stopping the bot
To stop the chatbot, go back to the terminal where the application is running and press Ctrl + C.
