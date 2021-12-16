from pdf_generator import pdf_creator
import streamlit as st


class WpApp:
    def __init__(self):
        self.sth = 0
        self.gen_pdf()

    @staticmethod
    def gen_pdf():
        trigger_pdf = st.button("generate")
        if trigger_pdf:
            pdf_creator.start()
            file = open('./pdf_generator/pdf_data/output/rt.pdf', 'rb')
            st.download_button(label="Download PDF", data = file, file_name="report.pdf")
