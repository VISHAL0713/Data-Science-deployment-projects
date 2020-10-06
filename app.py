from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def home():
    if request.method == "POST":
        FS = int(request.form["FS"])
        FU = int(request.form["FU"])
        with open('my_model','rb') as f:
            model = pickle.load(f)
        result = model.predict([[FS,FU]])
        if result[0] == 'YES':
            return render_template('home.html',data = ["you have diabetes","red"])
        else:
            return render_template('home.html',data=["Congratulations!!! you do not have diabetes","green"])
    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<name>')
def profile(name):
    return "Hello" + str(name)

    

if __name__ == "__main__":
    app.run(debug=True,port = 5000)