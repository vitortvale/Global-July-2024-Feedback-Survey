import streamlit as st 
import pandas as pd
import numpy as np
from dataclasses import dataclass

st.set_page_config(layout="wide")


@dataclass
class Course:
    name: str
    code: str
    overall: float
    methodology: float
    classroom: float
    staff: float
    recommendability: float
    objectivity: float
    correspondaceToExpectations: float
    textBooksPresentations:float
    content: float
    easeToUnderstandForeignLanguage: float

def merge(course1: Course, course2: Course) -> list[Course]:
    course1.overall = (course1.overall + course2.overall)/2
    course1.methodology = (course1.methodology + course2.methodology)/2
    course1.classroom = (course1.classroom + course2.classroom)/2
    course1.staff = (course1.staff + course2.staff)/2
    course1.recommendability = (course1.recommendability + course2.recommendability)/2
    course1.objectivity = (course1.objectivity + course2.objectivity)/2
    course1.correspondaceToExpectations = (course1.correspondaceToExpectations + course2.correspondaceToExpectations)/2
    course1.textBooksPresentations = (course1.textBooksPresentations + course2.textBooksPresentations)/2
    course1.content = (course1.content + course2.content)/2
    course1.easeToUnderstandForeignLanguage = (course1.easeToUnderstandForeignLanguage + course2.easeToUnderstandForeignLanguage)/2


    return course1


def survey_handling(dfnp :np.ndarray, courses_with_comma: list[str]) -> list[Course]:

    dimensions = dfnp.shape
    rows, columns = dimensions
    courses = [] 
    indexes = []
    array = [] 
    answers = []

    for i in range(rows):
        if(dfnp[i][0].count(',') > 0): 
            courses.append((dfnp[i][0]).split(','))
            notes = (dfnp[i][1],dfnp[i][2],dfnp[i][3],dfnp[i][4],dfnp[i][5],dfnp[i][6],dfnp[i][7],dfnp[i][8],dfnp[i][9],dfnp[i][10])
            answers.append(notes)
            indexes.append(i)
        else:
            array.append(dfnp[i])

    for course in courses:        
        for j in range(len(course)):
            if j == len(course):
                break
            title = course[j]
            if any(substring in title for substring in courses_with_comma):
                course[j] = f"{course[j]},{course[j + 1]}"
                course.pop(j + 1)



    for k in range(len(courses) -1, -1, -1):        
        if len(courses[k]) == 0:
            courses.pop(k) 

    for course in courses:
        i = 0
        for m in range(len(course)):
            row = np.array([])
            ck = (course[k])
            ans = (answers[i])
            row = np.append(row,ck)
            row = np.append(row,ans)
            array.append(row)
            i += 1

    array = np.array(array) 

    for i in range(len(array)):
        coursename = array[i][0]
        if "[" in coursename:
            splitname = coursename.split("[")
            array[i][0] = splitname[0]

    coursenames = []
    for i in range(len(array)):
        coursenames.append(array[i][0])
    
    coursenames = np.unique(coursenames)


    arrdf = pd.DataFrame(array)


    L = []
    
    for i in range(len(coursenames)):
        c = 0
        split = coursenames[i].split("-")
        code = split[0]
        coursename = split[1]
        course = Course(coursename, code, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)                 
        for j in range(len(array)):
            if(coursenames[i] == array[j][0]):
                c += 1
                course.overall += float(array[j][1])
                course.methodology += float(array[j][2])
                course.classroom += float(array[j][3])
                course.staff += float(array[j][4])
                course.recommendability += float(array[j][5])
                course.objectivity += float(array[j][6])
                course.correspondaceToExpectations += float(array[j][7])
                course.textBooksPresentations += float(array[j][8])
                course.content += float(array[j][9])
                course.easeToUnderstandForeignLanguage += float(array[j][10])
        course.overall /= c
        course.methodology /= c
        course.classroom /= c
        course.staff /= c
        course.recommendability /= c
        course.objectivity /= c
        course.correspondaceToExpectations /= c
        course.textBooksPresentations /= c
        course.content /= c
        course.easeToUnderstandForeignLanguage /= c
        
        course.overall = np.round(course.overall, 2)
        course.methodology = np.round(course.methodology, 2)
        course.classroom = np.round(course.classroom, 2)
        course.staff = np.round(course.staff, 2)
        course.recommendability = np.round(course.staff, 2 )
        course.objectivity = np.round(course.objectivity, 2)
        course.correspondaceToExpectations = np.round(course.correspondaceToExpectations, 2)
        course.textBooksPresentations = np.round(course.textBooksPresentations, 2)
        course.content = np.round(course.content, 2)
        course.easeToUnderstandForeignLanguage = np.round(course.easeToUnderstandForeignLanguage, 2)

        L.append(course)

    return L

def treatment(file_root: str) -> list[Course]: #this name has to be changed asap
    survey_data = pd.read_excel(file_root)
    survey_data = survey_data.drop(survey_data.columns[[0,1,2,3,-1,-2,-3]], axis = 1) # dropped columns contained private and unuseful information
    survey_data = survey_data.drop(survey_data.index[0:425]) # dropped lines contained information from the previous years
    survey_data = survey_data.to_numpy()
    courses_with_comma = ["HIS01", "HIS03", "HIS05", "SSC01"] ##this list changes every year 
    courselist  = survey_handling(survey_data, courses_with_comma)
    courselist[6] = merge(courselist[6], courselist[7])
    courselist.remove(courselist[7])
    courselist[6].overall = np.round(courselist[6].overall, 2)
    courselist[6].methodology = np.round(courselist[6].methodology, 2)
    courselist[6].classroom = np.round(courselist[6].classroom, 2)
    courselist[6].staff = np.round(courselist[6].staff, 2)
    courselist[6].recommendability = np.round(courselist[6].staff, 2 )
    courselist[6].objectivity = np.round(courselist[6].objectivity, 2)
    courselist[6].correspondaceToExpectations = np.round(courselist[6].correspondaceToExpectations, 2)
    courselist[6].textBooksPresentations = np.round(courselist[6].textBooksPresentations, 2)
    courselist[6].content = np.round(courselist[6].content, 2)
    courselist[6].easeToUnderstandForeignLanguage = np.round(courselist[6].easeToUnderstandForeignLanguage, 2)
    courselist[8] = merge(courselist[8], courselist[9])
    courselist.remove(courselist[9])
    courselist[8].overall = np.round(courselist[8].overall, 2)
    courselist[8].methodology = np.round(courselist[8].methodology, 2)
    courselist[8].classroom = np.round(courselist[8].classroom, 2)
    courselist[8].staff = np.round(courselist[8].staff, 2)
    courselist[8].recommendability = np.round(courselist[8].staff, 2 )
    courselist[8].objectivity = np.round(courselist[8].objectivity, 2)
    courselist[8].correspondaceToExpectations = np.round(courselist[8].correspondaceToExpectations, 2)
    courselist[8].textBooksPresentations = np.round(courselist[8].textBooksPresentations, 2)
    courselist[8].content = np.round(courselist[8].content, 2)
    courselist[8].easeToUnderstandForeignLanguage = np.round(courselist[8].easeToUnderstandForeignLanguage, 2)
    courselist[8].code = "HIS02"
    return courselist
 

def main():
    courselist = treatment(('./surveys/2024.xlsx'))
    st.write("# Global July 2024 Stats 🌎")






    return courselist

if __name__ == "__main__":
    main()


