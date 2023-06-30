##################
#Importing Libraries
##################

import pandas as pd 
import streamlit as st
import altair as alt
from PIL import Image

###################
# Page Title
###################

image = Image.open('dna-count-web-app-logo.png')

st.image(image, use_column_width = True)

st.write(""" 
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA. 

***
""")

##################
# Input Text Box
##################

# st.sidebar.header('Enter DNA Sequence:')

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2 \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence Input:", sequence_input, height = 250)
sequence = st.text_area("Sequence Input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write(""" *** """)
         
### Prints the input DNA Sequence
st.header('Input DNA Query')
sequence

## DNA Nucleotide count
st.header('Output Nucleotide Count:')


### 1. Printing Dictionary
st.subheader("1. Print Dictionary")
def DNA_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C"))
    ])
    return d 

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

### 2. Print Text
st.subheader('2. Print Text')
st.write('There are ' + str(X["A"]) + ' Adenine (A)')
st.write('There are ' + str(X["T"]) + ' Thymine (T)')
st.write('There are ' + str(X["G"]) + ' Guanine (G)')
st.write('There are ' + str(X["C"]) + ' Cytosine (C)')


### 3. Displaying Data Frame
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient = 'index')
df = df.rename({0: 'Count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index':'Nucleotide'})
st.write(df)

### 4. Display Bar Chart Using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'Nucleotide',
    y = 'Count'
)

p = p.properties(
    width = alt.Step(80)
)

st.write(p)

### to understand what's dna and how does it work, watch this video for simplified understanding
## https://www.youtube.com/watch?v=zwibgNGe4aY
## https://www.genome.gov/genetics-glossary/Deoxyribonucleic-Acid
## https://askabiologist.asu.edu/dna-shape-and-structure
## https://medlineplus.gov/genetics/understanding/basics/dna/


