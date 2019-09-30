#Day 10
import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] =  'test' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:HZL9r0wMsEHyce4Q@cluster0-u5agh.mongodb.net/test?retryWrites=true&w=majority'  

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index') #homepage
def index():
    #Connect to the DB with the mongo object
    collection = mongo.db.events #looks at mongo object ->goes to database ->finds collection 
    #Use the .find() method to return all of the events
    events = collection.find({})
    return render_template('index.html', events = events)

#This route will handle the POST of our form. It should also be able to redirect to homepage on a GET request
@app.route('/addevent', methods = ["GET", "POST"])
def add_event():
    #if we go through URL (GET) ->show us the form and page
    #if we POST through this URL ->send the info in and show us the homepage
    if request.method == "GET":
        return render_template('add_event.html')
    else:
        eventName = request.form["eventName"] #from the form, save the eventName from dict
        eventDate = request.form["eventDate"] #from the form, save the eventDate from dict
        event = {"event": eventName, "date": eventDate}
        collection = mongo.db.events #connect to mongoDB in this route
        collection.insert(event) #insert the event into that collection
        #we have all CRUD operations for MONGO - we can llok those up later
        return redirect('/') #we want them to go away from the form so they can't double-add the event (can be used instead of rendering template)
        #Used to direct the user to another route. In this case, directed to /