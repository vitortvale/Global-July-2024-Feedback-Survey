import streamlit as st 
import pandas as pd
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


def main():

    coursedf = pd.read_excel("./surveys/course2024.xlsx")
    courselist = coursedf.to_numpy().tolist()
    L  = []
    for row in courselist:
        course = Course(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
        L.append(course)

    st.write("# Global July 2024 Feedback Survey 🌎")
    st.write("#### Here you can visualize the ratings given by everyone who participated in the event that took place at the Federal University of Juiz de Fora!")
    
    return L

if __name__ == "__main__":
    main()


