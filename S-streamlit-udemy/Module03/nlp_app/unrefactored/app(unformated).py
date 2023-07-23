# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 


# Additional Pkgs
# Load EDA Pkgs
import pandas as pd 

# Text Cleaning Pkgs
import neattext as nt 
import neattext.functions as nfx

# utils

import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")


# Data Viz Pkgs
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

# External Utils
from app_utils import *


# Fxn to Get Wordcloud
from wordcloud import WordCloud 
def plot_wordcloud(my_text):
	my_wordcloud = WordCloud().generate(my_text)
	fig = plt.figure()
	plt.imshow(my_wordcloud,interpolation='bilinear')
	plt.axis('off')
	st.pyplot(fig)


# Fxn to Download Result
def make_downloadable(data):
	csvfile = data.to_csv(index=False)
	b64 = base64.b64encode(csvfile.encode()).decode()
	new_filename = 'nlp_result_{}_.csv'.format(timestr)
	st.markdown('### ** 📩 ⬇️ Download CSV file **')
	href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click here!</a>'
	st.markdown(href, unsafe_allow_html=True)



def main():
	st.title("NLP App with Streamlit")
	menu = ["Home","NLP(files)","About"]

	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Home: Analyse Text")
		raw_text = st.text_area("Enter Text Here")
		num_of_most_common = st.sidebar.number_input("Most Common Tokens",5,15)
		if st.button("Analyze"):

			with st.beta_expander("Original Text"):
				st.write(raw_text)

			with st.beta_expander("Text Analysis"):
				token_result_df = text_analyzer(raw_text)
				st.dataframe(token_result_df)

			with st.beta_expander("Entities"):
				# entity_result = get_entities(raw_text)
				# st.write(entity_result)

				entity_result = render_entities(raw_text)
				stc.html(entity_result,height=1000,scrolling=True)

			# Layouts
			col1,col2 = st.beta_columns(2)

			with col1:
				with st.beta_expander("Word Stats"):
					st.info("Word Statistics")
					docx = nt.TextFrame(raw_text)
					st.write(docx.word_stats())

				with st.beta_expander("Top Keywords"):
					st.info("Top Keywords/Tokens")
					processed_text = nfx.remove_stopwords(raw_text)
					keywords = get_most_common_tokens(processed_text,num_of_most_common)
					st.write(keywords)

				with st.beta_expander("Sentiment"):
					sent_result = get_sentiment(raw_text)
					st.write(sent_result)


			with col2:
				with st.beta_expander("Plot Word Freq"):
					fig = plt.figure()
					top_keywords = get_most_common_tokens(processed_text,num_of_most_common)
					plt.bar(keywords.keys(),top_keywords.values())
					plt.xticks(rotation=45)
					st.pyplot(fig)


				with st.beta_expander("Plot Part of Speech"):
					fig = plt.figure()
					sns.countplot(token_result_df['PoS'])
					plt.xticks(rotation=45)
					st.pyplot(fig)

				with st.beta_expander("Plot Wordcloud"):
					plot_wordcloud(raw_text)


			with st.beta_expander("Download Text Analysis Results"):
				make_downloadable(token_result_df)	





	elif choice =="NLP(files)":
		st.subheader("NLP Task")

		text_file = st.file_uploader("Upload Files",type=['pdf','docx','txt'])
		num_of_most_common = st.sidebar.number_input("Most Common Tokens",5,15)
		
		if text_file is not None:
			if text_file.type == 'application/pdf':
				raw_text = read_pdf(text_file)
				# st.write(raw_text)
			elif text_file.type == 'text/plain':
				# st.write(text_file.read()) # read as bytes
				raw_text = str(text_file.read(),"utf-8")
				# st.write(raw_text)
			else:
				raw_text = docx2txt.process(text_file)
				# st.write(raw_text)

			with st.beta_expander("Original Text"):
				st.write(raw_text)

			with st.beta_expander("Text Analysis"):
				token_result_df = text_analyzer(raw_text)
				st.dataframe(token_result_df)

			with st.beta_expander("Entities"):
				# entity_result = get_entities(raw_text)
				# st.write(entity_result)

				entity_result = render_entities(raw_text)
				stc.html(entity_result,height=1000,scrolling=True)

			# Layouts
			col1,col2 = st.beta_columns(2)

			with col1:
				with st.beta_expander("Word Stats"):
					st.info("Word Statistics")
					docx = nt.TextFrame(raw_text)
					st.write(docx.word_stats())

				with st.beta_expander("Top Keywords"):
					st.info("Top Keywords/Tokens")
					processed_text = nfx.remove_stopwords(raw_text)
					keywords = get_most_common_tokens(processed_text,num_of_most_common)
					st.write(keywords)

				with st.beta_expander("Sentiment"):
					sent_result = get_sentiment(raw_text)
					st.write(sent_result)


			with col2:
				with st.beta_expander("Plot Word Freq"):
					fig = plt.figure()
					top_keywords = get_most_common_tokens(processed_text,num_of_most_common)
					plt.bar(keywords.keys(),top_keywords.values())
					plt.xticks(rotation=45)
					st.pyplot(fig)


				with st.beta_expander("Plot Part of Speech"):
					try:

						fig = plt.figure()
						sns.countplot(token_result_df['PoS'])
						plt.xticks(rotation=45)
						st.pyplot(fig)
					except:
						st.warning("Insufficient Data")

				with st.beta_expander("Plot Wordcloud"):
					plot_wordcloud(raw_text)


			with st.beta_expander("Download Text Analysis Results"):
				make_downloadable(token_result_df)	

	else:
		st.subheader("About")





if __name__ == '__main__':
	main()