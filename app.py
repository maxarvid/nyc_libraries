from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libraries.db'
db = SQLAlchemy(app)

class Library(db.Model):
  __tablename__ = 'libraries'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  dbn = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  libraries = Library.query.all()
  return render_template("list.html", libraries=libraries)

@app.route("/libraries/")
def libraries():
  libraries = Library.query.all()
  return render_template("list.html", libraries=libraries)

@app.route("/libraries/<dbn>/")
def library(dbn):
  library = Library.query.filter_by(dbn=dbn).first()
  return render_template("show.html", library=library)

'''@app.route("/search")
def search():
  name = request.args.get('query')
  libraries = Library.query.filter(Library.NAME.contains(name)).all()
  return render_template("list.html", libraries=libraries)
'''


if __name__ == '__main__':
  app.run(debug=True)