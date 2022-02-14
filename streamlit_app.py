import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Sashank Makanaboyina
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand"  target="_blank">Sashank Makanaboyina</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects"> Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Data Science), *University at Buffalo*, USA',
'2020-')
st.markdown('''
''')

txt('**Bachelors of Science** (Computer Science), *PES University*, India',
'2015-2019')
st.markdown('''
- Graduated with First Class.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Student Trainee**, Mercedes-Benz Research & Development, India','2019 - 2020')
st.markdown('''
- Developed an autonomic computing tool to reduce testing time of software development tools by ` 20% `by 
designing a proprietary software which leverages unsupervised machine learning models to auto correct coding
bugs during peer-to-peer reviews 
- Instrumental in providing proof of concept for the above project to which it was selected as an Innovation idea in a 
companywide hackathon and was given private funding of ` 60,000 USD ` to take the idea into business opportunity.
- Analyzed ` 200k ` JIRA tickets generated by users, based on timelines of recurring and repetitive requests for plugin 
upgradation by topic modeling techniques with custom made ETL applications to prepare unruly data for NLP 
models.
''')

txt('**Data Scientist Intern**, Avalon Labs, Mana Network (subsidiary), India',
'Jan 2019 - May 2019')
st.markdown('''
- Implemented internal rating system for clients by leveraging real-time market trends and industry performance 
metrics using statistical models designed in python and scikit- learn. Which resulted in clients having a more data 
focused usable score to leverage their product performance in the market.
- Analyzed client specific marketing trends using tools such as Google Analytics, SE ranking and Piwik to influence 
digital markets initiative in the clients marketing strategies.
- Created customized manual testing tool books to improve UI & UX experience of the product.
''')

st.markdown('''
## Projects
''')
txt4('Music Genre Classification ', 'Music Genre Classification using Random Forrest and Decision Tree Classifer to develop a model with `97% F1 Score`', 'https://shorturl.at/djwLM')
txt4('Genes sequences causing bladder cancer', 'A classification model using tableau and python to detect three types of bladder cancer among ` 7000+ ` unique gene expression', 'https://shorturl.at/yzKW3')
txt4('Cluster analysis of NGC 7531 spiral galaxy ', 'Analyzed a star formation of a sub spiral galaxy of ` 323 points ` in space to detect and categorize clusters of stars and HII regions','https://shorturl.at/ijlxI')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/sashank-makanaboyina/')
txt2('GitHub', 'https://github.com/scam2k')

