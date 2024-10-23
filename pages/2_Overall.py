import streamlit as st
from Home import main

courselist = main()


def generate_stars(rating):
        filled_star = '<span style="color: #E26464;">★</span>'
        half_star = '<span style ="color: #E26464;">⯨ </span>'
        stars = filled_star * int(rating)  
        if rating % 1 >= 0.5:
            stars += half_star 
        return stars

def organize_courses(parameter: str) -> dict[str,float]:
    organized_dict = {}
    match parameter:
        case "Overall":
             for course in courselist:
                  organized_dict.update({course.code:course.overall})
        case "Methodology":
             for course in courselist:
                  organized_dict.update({course.code:course.methodology})
        case "Classroom":
             for course in courselist:
                  organized_dict.update({course.code:course.classroom})
        case "Staff":
             for course in courselist:
                  organized_dict.update({course.code:course.staff})
        case "Recommendability":
             for course in courselist:
                  organized_dict.update({course.code:course.recommendability})
        case "Objectivity":
             for course in courselist:
                  organized_dict.update({course.code:course.objectivity})
        case "Correspondace To Expectations":
             for course in courselist:
                  organized_dict.update({course.code:course.correspondaceToExpectations})
        case "Textbooks/Presentations":
             for course in courselist:
                  organized_dict.update({course.code:course.textBooksPresentations})
        case "Content":
             for course in courselist:
                  organized_dict.update({course.code:course.content})
        case "Ease to Understand Foreign Language":
             for course in courselist:
                  organized_dict.update({course.code:course.easeToUnderstandForeignLanguage})

    return dict(sorted(organized_dict.items(),key=lambda item: item[1], reverse = True))

def main():
    cols = st.columns(7)


    with cols[0]:
        with st.expander("Criteria"):
            options = ['Overall', 'Methodology', 'Classroom', 'Staff', 'Recommendability',
                       'Objectivity', 'Correspondace to Expectations', 'Textbooks/Presentations',
                       'Content', 'Ease to Understand Foreign Language']


            selected_option = st.radio('Choose a filter:', options)

    match selected_option:
        case "Overall":
             organized_dict = organize_courses("Overall")
        case "Methodology":
             organized_dict = organize_courses("Methodology")
        case "Classroom":
             organized_dict = organize_courses("Classroom")
        case "Staff":
             organized_dict = organize_courses("Staff")
        case "Recommendability":
             organized_dict = organize_courses("Recommendability")
        case "Objectivity":
             organized_dict = organize_courses("Objectivity")
        case "Correspondace to Expectations":
             organized_dict = organize_courses("Correspondace To Expectations")
        case "Textbooks/Presentations":
             organized_dict = organize_courses("Textbooks/Presentations")
        case "Content":
             organized_dict = organize_courses("Content")
        case "Ease to Understand Foreign Language":
             organized_dict = organize_courses("Ease to Understand Foreign Language")

    with cols[1]:
        i = 1
        for coursename, evaluation in list(organized_dict.items())[0:5]:
                st.html(f"<h3 style = 'text-align:center;'>{i}º   {coursename}<h3>")
                st.html(f"<h3 style = 'text-align:center;'>{evaluation}  {generate_stars(evaluation)}<h3>")
                i +=1
    with cols[2]:
        i = 5
        for coursename, evaluation in list(organized_dict.items())[5:10]:
                st.html(f"<h3 style = 'text-align:center;'>{i}º   {coursename}<h3>")
                st.html(f"<h3 style = 'text-align:center;'>{evaluation}  {generate_stars(evaluation)}<h3>")
                i +=1
    with cols[3]:
        i = 10
        for coursename, evaluation in list(organized_dict.items())[10:15]:
                st.html(f"<h3 style = 'text-align:center;'>{i}º   {coursename}<h3>")
                st.html(f"<h3 style = 'text-align:center;'>{evaluation}  {generate_stars(evaluation)}<h3>")
                i +=1
    with cols[4]:
        i = 15
        for coursename, evaluation in list(organized_dict.items())[15:20]:
                st.html(f"<h3 style = 'text-align:center;'>{i}º   {coursename}<h3>")
                st.html(f"<h3 style = 'text-align:center;'>{evaluation}  {generate_stars(evaluation)}<h3>")
                i +=1
    with cols[5]:
        i = 20
        for coursename, evaluation in list(organized_dict.items())[20:25]:
                st.html(f"<h3 style = 'text-align:center;'>{i}º   {coursename}<h3>")
                st.html(f"<h3 style = 'text-align:center;'>{evaluation}  {generate_stars(evaluation)}<h3>")

                i +=1


if __name__ == "__main__":
    main()
