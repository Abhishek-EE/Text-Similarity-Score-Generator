"""
Routes and views for the flask application.
"""

from flask import Blueprint, render_template, request
import traceback
from . import SimilarityScoreGenerator as SSG




views = Blueprint('views',__name__)

@views.route('/', methods = ['GET','POST'])
def home():
    """Renders the home page."""
    return render_template("home.html")


@views.route('/send', methods = ['GET','POST'])
def my_form_post():
    if request.method == "GET":
        return render_template("home.html")
    else:
        try:
            text1 = request.form.get("Text1")
            processed_text1 = text1.lower()
            text2 = request.form.get("Text2")
            processed_text2 = text2.lower()
            scoregenerator = SSG.SimiliariytScoreGenerator(processed_text1,processed_text2)
            result = scoregenerator.calculate()  
            return render_template("send.html",result=result,text1=text1,text2=text2)
        except:
            traceback.print_exc()
            return "something went horribly wrong"
   


