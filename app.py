from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(
    app,
    version="1.0"
)

@api.route("/hello")
class HelloWorld(Resource):
    """Hello world """
    def get(self):
        """ Hello world """
        return "world", 200

@api.route("/vowel-service")
class VowelService(Resource):
    """Reverse value of key "message"""
    def post(self):
        """vowel reversal"""
        vowels_in_word = ""
        new_message = ""
        # First find the vowel in the string provided in message
        # concatnate the vowels to the empty vowels_in_word string
        # above
        for chr in api.payload["message"]:
            if chr in "AEIOUaeiou":
                vowels_in_word = vowels_in_word + chr

        # Traverse the string again and at the position of any vowel
        # replace with the value of the last index of the vowels found
        # above. Then replace the vowels string witout the last character.
        # Else just concatnate the character into the new_message
        for chr in api.payload["message"]:
            if chr in "AEIOUaeiou":
                new_message = new_message + vowels_in_word[-1]
                vowels_in_word =  vowels_in_word[:-1]
            else:
                new_message = new_message + chr
        return new_message, 200

if __name__ == "__main__":
    app.run(debug=True)
