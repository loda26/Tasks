from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)

engine = create_engine("sqlite:///testdb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

app = Flask(__name__)

@app.route('/')
def index():
    session = Session()
    users = session.query(Users).all()
    return render_template('index.html', users=users)

@app.route('/submit', methods=['POST'])
def submit():
    session = Session()

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    user = Users(name=name, email=email, password=password)
    session.add(user)
    session.commit()

    return redirect('/')

@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = Session()
    user = session.query(Users).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return "User deleted successfully", 200
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
