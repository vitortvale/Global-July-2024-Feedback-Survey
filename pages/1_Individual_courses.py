import streamlit as st
from Home import main
from Home import Course


courselist = main()

def show_stats(course: Course, cols: list):
    with cols[0]:
         st.markdown(f"<h1>{course.code}</h1>", unsafe_allow_html=True)
         st.markdown(f"<h3>{course.name}</h3>", unsafe_allow_html=True)
         
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Overall</h4>")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.overall} {generate_stars(course.overall)}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Methodology</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.methodology} {generate_stars(course.methodology)}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Classroom</h4> ")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.classroom} {generate_stars(course.classroom)}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Staff</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.staff} {generate_stars(course.staff)}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Recommendability</h4> ")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.recommendability} {generate_stars(course.recommendability)}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Objectivity</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.objectivity} {generate_stars(course.objectivity)}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Correspondance to Expectations</h4>") 
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.correspondaceToExpectations} {generate_stars(course.correspondaceToExpectations)}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Textbooks/Presentations</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.textBooksPresentations} {generate_stars(course.textBooksPresentations)}</h3 >")
    cols[1].html("<h4 style = 'text-align:center;color:black;'>Content</h4> ")
    cols[1].html(f"<h3 style ='font-size:40px;'>{course.content} {generate_stars(course.content)}</h3 >")
    cols[2].html("<h4 style = 'text-align:center;color:black;'>Ease to Understand Foreign Language</h4> ")
    cols[2].html(f"<h3 style ='font-size:40px;'>{course.easeToUnderstandForeignLanguage} {generate_stars(course.easeToUnderstandForeignLanguage)}</h3 >")


def generate_stars(rating):
        filled_star = '<span style="color: #E26464;">★</span>'
        half_star = '<span style ="color: #E26464;">⯨ </span>'
        stars = filled_star * int(rating)  
        if rating % 1 >= 0.5:
            stars += half_star 
        return stars

def main():
    cols = st.columns(4)

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: white; /* Sidebar background color */
            width: 300px; /* Set the width of the sidebar */
        }

        [data-testid="stSidebar"] .css-1d391kg {
            background-color: red; /* Content background color */
            color: red; /* Text color inside the sidebar */
        }

        [data-testid="stSidebar"] ::-webkit-scrollbar {
            color: red;
            width: 10px;
        }

        [data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
            background-color: red;
            border-radius: 10px;
        }

        [data-testid="stSidebar"] ::-webkit-scrollbar-thumb:hover {
            background-color: red;
        }
        </style>
        """, unsafe_allow_html=True
    )

    with st.sidebar:
        st.write("Courses")
            
        for course in courselist:
            if st.button(course.code):
                    show_stats(course, cols)


if __name__ == "__main__":
    main()













