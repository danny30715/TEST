from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html") #if you want to render a .html file,
                        # import render_template from flask and use
                        #render_template("index.html") here.

      
      
@app.route('/123')
def index2():
   return "321123123"
      
      
      
if __name__ == '__main__':
    app.debug = True
    app.run() 
