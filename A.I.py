# Import the libraries
import random
import requests

# Define the chatbot class
class ScriptBot:

  # Initialize the chatbot with a name and a greeting
  def __init__(self, name, greeting):
    self.name = name
    self.greeting = greeting

  # Define the method to generate a response
  def respond(self, user_input):

    # If the user input is empty, return the greeting
    if not user_input:
      return self.greeting

    # If the user input is "bye", end the conversation
    elif user_input.lower() == "bye":
      return "Bye, have a nice day!"

    # If the user input is "what is your name?", return the name
    elif user_input.lower() == "what is your name?":
      return f"My name is {self.name}."

    # If the user input is "what can you do?", return the capabilities
    elif user_input.lower() == "what can you do?":
      return f"I can generate a few scripts for you. Just tell me what kind of script you want."

    # If the user input is "generate a script for X", try to generate a script for X
    elif user_input.lower().startswith("generate a script for "):

      # Extract the script type from the user input
      script_type = user_input.lower().replace("generate a script for ", "")

      # Check if the script type is valid
      if script_type in ["a poem", "a story", "a song", "a joke"]:

        # Call the API to generate a script for the script type
        url = f"https://api.scriptbot.com/{script_type}"
        response = requests.get(url)

        # Check if the API call was successful
        if response.status_code == 200:

          # Extract the script from the response
          script = response.text

          # Return the script
          return f"Here's your {script_type}:\n{script}"

        # If the API call was not successful, return an error message
        else:
          return f"Sorry, something went wrong. Please try again later."

      # If the script type is not valid, return an error message
      else:
        return f"Sorry, I can't generate a script for {script_type}. Please choose one of these options: a poem, a story, a song, or a joke."

    # If the user input is anything else, return a default message
    else:
      return "I'm sorry, I don't understand. Please ask me something else."


# Create an instance of the chatbot with a name and a greeting
bot = ScriptBot("Scripty", "Hello, I'm Scripty. I can generate a few scripts for you.")

# Start the conversation loop
while True:

  # Get the user input
  user_input = input("You: ")

  # Generate the bot response
  bot_response = bot.respond(user_input)

  # Print the bot response
  print(f"{bot.name}: {bot_response}")

  # Break the loop if the user input is "bye"
  if user_input.lower() == "bye":
    break
