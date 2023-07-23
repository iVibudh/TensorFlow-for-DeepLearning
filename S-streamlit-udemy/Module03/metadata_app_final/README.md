#### MetaData Extraction App
A Data App for extracting metadata from images,audio files and pdf and docx.

+ Packages
```bash
pip install 
```
	- streamlit
	- pandas
	- pillow
	- exifread
	- seaborn
	- matplotlib
	- pyPDF2
	- mutagen
	- tinytag
	- docx2txt
	- python docx

#### App Structure
+ Home
+ Image
+ Audio
+ PDF/Docx
+ About
	- Monitor
	- Stats of Uploads



### Deploying with Docker
+ Docker is an open platform for developing, shipping, and running applications. 
+ Docker enables you to separate your applications from your infrastructure so you can deliver software quickly

#### Requirements
+ Install Docker
+ Dockerfile
+ App + Requirements.txt

#### Steps to get Requirements.txt
+ Using Pipreqs
```bash
pip install pipreqs
```
+ Point Pipreqs to folder
```bash
pipreqs path\to\folder
```

+ Using Pip or Pipenv
- pip freeze > requirements.txt
- pipenv -r lock > requirements.txt









