from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/sangeeth')
def main():
   return render_template('1.html')
   
if __name__ == '__main__':r
   app.run(debug=True)
    