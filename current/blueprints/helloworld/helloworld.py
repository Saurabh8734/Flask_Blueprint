from flask import Blueprint, render_template, request, redirect

helloworld_bp = Blueprint("helloworld", __name__, template_folder="templates")

@helloworld_bp.route("/")
def index():
    return "Hello World!"

@helloworld_bp.route("/hello")
def hello():
    return "Hellow Saurabh!"

@helloworld_bp.route("/hello/<name>")
def hello_name(name):
    return f"Hellow {name}"

@helloworld_bp.route("/hellohtml")
def hello_html():
    return render_template("hello.html")