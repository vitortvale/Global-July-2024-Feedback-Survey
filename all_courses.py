import streamlit as st
import pandas as pd
from main import main
from main import Course
import math

with open('./style.css') as f:
    css = f.read

st.set_page_config(layout="wide")

courselist = main()

def show_stats(course: Course, cols: list):
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Overall</h4>")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.overall}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Methodology</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.methodology}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Classroom</h4> ")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.classroom}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Staff</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.staff}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Recommendability</h4> ")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.recommendability}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Objectivity</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.objectivity}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Correspondance to Expectations</h4>") 
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.correspondaceToExpectations}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Textbooks/Presentations</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.textBooksPresentations}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Content</h4> ")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.content}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Ease to Understand Foreign Language</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.easeToUnderstandForeignLanguage}</h3 >")


def draw_stars(criteria: float):
    rounded_criteria = math.floor(criteria)
    stars = []
    for i in range(rounded_criteria):
        stars.append(st.html("<h1>&Star;</h1>"))
    st.html("".join(stars))





#cols[0] = st.image('img.jpeg')
#st.html('<img src = "img.jpeg"/>')

st.html(f"<h1 style = 'text-align:center;color:#d60202;font-size:80px;'>{courselist[0].code}</h1>")
#st.html(f"<h4 style = 'text-align:center;color:black;'>{courselist[0].name}</h4>")
cols = st.columns(4)
show_stats(courselist[0], cols)
draw_stars(courselist[0].classroom)












