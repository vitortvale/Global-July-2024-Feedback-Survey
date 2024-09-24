import streamlit as st 
import pandas as pd

df = pd.read_excel('./surveys/2024.xlsx') # remember to remove the first 424 lines
df = df.drop(df.columns[[0,1,2,3,-1,-2,-3]], axis = 1) # dropped columns contained private and unuseful information
df = df.drop(df.index[0:425]) # dropped lines contained information from the previous years
st.write(df)

dfnp = df.to_numpy()
st.write(dfnp)
###Some columns informing the course have multiple titles that should be in a different row, this is how the handling will be made:
#1. Interate through the course attended column, verify if it has a ','
#2. If if does, the comma-separated-values will become new differents strings
#3. Copy all the values from the other columns an array
#4. Create a new row with the new string(s) and copy the values in the array to their columns

dimensions = dfnp.shape
rows, columns = dimensions

# HIS01 - Fascismo en España, 1933-1945. Una perspectiva transnacional y de género [PRESENCIAL]
# HIS03 - Migraciones en América Latina pasado-presente: fronteras, cuerpos racializados y resistencias migrantes [PRESENCIAL]
# HIS05 - Historia, Genero y Autobiografía: aspectos teóricos y estudios de caso [PRESENCIAL]
# SSC01 - A Workers’ Own Way to Inquire: workers’ inquiry, method critique and co-research [PRESENCIAL]

#if an element of the array stats with HIS01,HIS02,HIS OR SSC01 copy the next value of the array to the one that stars with one of `em

courses = []
for i in range(rows):
    if(dfnp[i][0].count(',') > 0): 
        courses.append((dfnp[i][0]).split(','))
        st.write(courses)
        st.write(courses[0])
        
#for j in range(courses):

    
    



#each course will have its own dataframe that is gonna be stored in a df-type-array
#iterate through the array, creating course objects for each dataframe
#create a dictionary, with the course code being the key to the course object
#access to the courses will be possible using the dictionary 



