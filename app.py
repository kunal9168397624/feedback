from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    customerName = db.Column(db.String(20), nullable = True)
    rate = db.Column(db.Integer ,nullable = True)
    def __repr__(self) :
        return f"User('{self.id}','{self.customerName}','{self.rate}')"

sum=0
data = User.query.all()
for i in data:
    sum =  sum+i.rate

@app.route('/')
def home():
    return render_template("index.html",data=data,sum=sum)


if __name__=='__main__':
    app.run(debug=True)