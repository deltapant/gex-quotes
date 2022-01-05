from flask import Flask, render_template
app = Flask(__name__, static_folder="..\\static")

#import config file to hide api_key

#use these quotes on davinci
gex_quote_samples= '''
Welcome to the only thing more evil than IRS Headquarters.
So this is where they decided to change Coke.
Looks like we got a fly in the spider's web
Screens up.
The horror!
Welcome to the only thing more evil than the Inland Revenue Headquarters.
And they said testing A-bombs on this island would have no effect.
Someone who is not me could stand to lose a few pounds.
I've got ten seconds to save the world.
Welcome to this week's episode of 'Touched By An Uncle'.
All that work and I'm back where I started. It's just like college.
My god! This is New York! I lived here... Worked here.
Dead fly martini. Shaken not stirred.
I am the last gecko.
Gecko. Gex Gecko.
This is the big one! I'm coming Elizabeth!
Ladies and gentlemen! The new Fall TV season!
So this is New Jersey.
Evening, Mr. Picasso!
To boldly go...I'm scared!
Oh William please... Give me a sponge bath. 
Don't take career advice from Joe Piscopo.
I haven't seen blasts like these since taco night at James Earl Jones' house.
Note to self: don't drink tap water at Jerry Garcia's.
'''

import os
import openai
import json
openai.api_key = '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'

@app.route('/quote-generator/')
def generate_gex_quote():

  #make api call with sample quotes generated

  generated_gex_quote = openai.Completion.create(
      engine="davinci",
      prompt= gex_quote_samples,
      max_tokens=25,
      stop= "\n"
    )
  #convert to json
  gex_json = json.dumps(generated_gex_quote)
  gex_quote= json.loads(gex_json)
  #get quote
  return gex_quote['choices'][0]['text']

@app.route('/')
def index():
  return render_template('home.html', data=generate_gex_quote())




if __name__ == '__main__':
  app.run(debug=True)
  
