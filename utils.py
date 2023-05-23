import streamlit as st
st.title("小冯速成相册")
imgs = [
   "pic1.jpg",
   "pic2.jpg",
   "pic3.jpg",
   "pic4.jpg",
   "pic5.jpg",
   "pic6.jpg",
   "pic7.jpg",
]

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image(imgs[0])
    st.image(imgs[6])

with col2:
    st.header("A dog")
    st.image(imgs[2])
    st.image(imgs[3])

with col3:
    st.header("An owl")
    st.image(imgs[4])
    st.image(imgs[5])
