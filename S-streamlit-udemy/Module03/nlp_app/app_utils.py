# Load NLP Pkgs
import spacy
nlp = spacy.load('en')
from spacy import displacy
from textblob import TextBlob
import pandas as pd 
from collections import Counter


# Fxns
def text_analyzer(my_text):
	docx = nlp(my_text)
	allData = [(token.text,token.shape_,token.pos_,token.tag_,token.lemma_,token.is_alpha,token.is_stop) for token in docx]
	df = pd.DataFrame(allData,columns=['Token','Shape','PoS','Tag','Lemma','IsAlpha','Is_Stopword'])
	return df 	

def get_entities(my_text):
	docx = nlp(my_text)
	entities = [(entity.text,entity.label_) for entity in docx.ents]
	return entities

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
# @st.cache
def render_entities(rawtext):
	docx = nlp(rawtext)
	html = displacy.render(docx,style="ent")
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)
	return result




# Fxn to get most common tokens
def get_most_common_tokens(my_text,num=5):
	word_tokens = Counter(my_text.split())
	most_common_tokens = dict(word_tokens.most_common(num))
	return most_common_tokens

# Fxn to Get Sentiment
def get_sentiment(my_text):
	blob = TextBlob(my_text)
	sentiment = blob.sentiment
	return sentiment


# Fxn to Read PDF
from PyPDF2 import PdfFileReader
import pdfplumber


def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text

def read_pdf2(file):
	with pdfplumber.open(file) as pdf:
	    page = pdf.pages[0]
	    return page.extract_text()
