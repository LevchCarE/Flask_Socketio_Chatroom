from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from string import ascii_uppercase # letters in the alphabet to generate the room code

#a decorator is a function that modifies the behavior of another function
#decorators are used to modify the behavior of the function, for example, the @app.route('/') 
# decorator is used to define the route for the index page
#the @socketio.on('event_name') decorator is used to define the event handler for the event_name event

# socketio is used to send and receive messages between the client and the serve. 
# Sockets are a live way to communicate instead of using db

import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app) # initialize socketio by passing the app= Flask(__name__) as argument

#method GET is used to get the data from the client and POST is used to send the data to the client
#remember that the client is the html file that we created in the templates folder

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')  #this is the index page that we created in the templates folder, 
                                        #we can change the folder name and html file name to any other name, but we need to specify the path to the html file


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')    

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    emit('message_response', 'Message received')


if __name__ == '__main__':  # this is the main function that runs the app
    socketio.run(app, debug=True, port=5000)  # run the app on port 5000, you can change the port number to any other number