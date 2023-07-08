from flask import Flask, render_template, jsonify, request , send_file
import json
from bardapi import Bard
from datetime import datetime
import os
os.environ["_BARD_API_KEY"]="XQi9QMGpcYuQt_PMFIlPOQxN40YMccmta3Mih_pjQ8oJaPOVKs246TSm-WDgv0-qZzUNGA."

def get_location():
    file_path = os.path.realpath(__file__)
    return os.path.dirname(file_path)

def give_access_to_location():
    location = get_location()
    os.system("sudo chmod -R 777 {}".format(location))



app = Flask(__name__)
bard = Bard()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    if message.lower() == 'hello' or message.lower() == 'helo' or message.lower() == 'hlo' or message.lower() == 'hellow' or message.lower() == 'hi' or message.lower() == 'hii' or message.lower() == 'hy' or message.lower() == 'hye' or message.lower() == 'hey' :    
        now=datetime.now()
        hr=int(now.strftime('%H'))
        
        
        if(hr>=0 and hr<12):
            image_url='/static/chatb.gif'
            response = 'Good Morning! How may i assist You'
            return jsonify(response=response,image_url=image_url, show_image=True)
        else:
            response='Good AfterNoon! How may i assist You'
            image_url='/static/chat12.gif'
            return jsonify(response=response,image_url=image_url, show_image=True)

    if message.lower() == 'who are you' or message.lower() == 'who r u' or message.lower() == 'who r you' or message.lower() == 'what is your name' or message.lower() == 'what is ur name' or message.lower() == 'whats ur name' or message.lower() == 'whats ur nam' or message.lower() == 'what iz ur name' or message.lower() == 'wht is ur name' or message.lower() == 'your name?' or message.lower() == 'ur name?':
        response = 'I am a chatbot created by Amin.'
        image_url = '/static/chatbot.gif'  # Update the image URL path if necessary
    
        return jsonify(response=response, image_url=image_url, show_image=True) 
    #message=message+"i am looking for more concise answer not more tha 50 words"
    resp = bard.get_answer(message)
    response = resp["content"]
    response_lines = response.split("\n\n")
    short_response = "\n\n".join(response_lines[:2])  # Take the first 3 lines

    
    images = resp["images"]
    print(images)
    image_url = next(iter(images)) if images else ""
    
    
    return jsonify(response=short_response, image_url=image_url, show_image=True) 

    #return response,image_url


if __name__ == '__main__':
    app.run()
    give_access_to_location()
    


 