from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars
import os


app = Flask(__name__)


# Create connection variable
conn = 'mongodb://localhost:27017'
mongo = pymongo.MongoClient(conn)


@app.route('/')
def home():
    mars_info= mongo.db.mars_info.find_one()
    return render_template('index.html', mars_info=mars_info)

# Route to execute the scrape function

@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

    # mars = mongo.db.mars
    # data = scrape_mars.scrape()
    # # import ipdb; ipdb.set_trace()
    # mars.update(
    #     {}, 
    #     data, upsert=True)
    # print(mars.find({}))

    # Redirect back to home page
    # return redirect("http://localhost:5000/", code=302)



    # mars_info=mongo.db.mars_info
    # mars_info = scraping()
    # surfing.update(
    #     {},
    #     data,
    #     upsert=True
    # )
    # return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
