from pdf_generator import pdf_creator
import streamlit as st
import networkx as nx
import osmnx as ox

class WpApp:
    def __init__(self):
        self.sth = 0
        self.gen_pdf()

    @staticmethod
    def gen_pdf():
        st.write("NETWORKX")
        st.write(nx.__version__)
        st.write("OSMNX")
        st.write(ox.__version__)
        trigger_pdf = st.button("generate")
        if trigger_pdf:
            pdf_creator.start()
            file = open('./pdf_generator/pdf_data/output/rt.pdf', 'rb')
            st.download_button(label="Download PDF", data = file, file_name="report.pdf")
