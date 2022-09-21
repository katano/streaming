import streamlit as st
import cv2
import numpy as np
import requests

# Title of the app
st.title( 'Mobile Camera Preview in Streamlit' )

# An empty image container that will hold the frames we'll fetch from the server
frame_window = st.image( [] )
