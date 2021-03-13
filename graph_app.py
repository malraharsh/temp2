import streamlit as st

st.title("Activity's Graph")

st.sidebar.subheader('Choose color')
bg_color = st.sidebar.color_picker('bg_color')
color = st.sidebar.color_picker('color')
line = st.sidebar.color_picker('line')
point = st.sidebar.color_picker('point')

bg_color = bg_color[1:]
color = color[1:]
line = line[1:]
point = point[1:]

l = f"(https://activity-graph.herokuapp.com/graph?username=ashutosh00710&bg_color={bg_color}&color={color}&line={line}&point={point}&area=true&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)"
link = f"[![Ashutosh's github activity graph]{l}"
# print(link) 

st.markdown(link, unsafe_allow_html=True)

st.text_area('Copy This Link', value=link)