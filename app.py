from flask import Flask, request, render_template, redirect
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// database.sqlite3'
