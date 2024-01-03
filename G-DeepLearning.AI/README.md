# Notes on dream LLM project 


<hr />

## Demo - Structured Data
### A. Write a python code:
- 1. what is NVIDIA's stock price?
    - writes python code that calls different api functionalities
    - executes that code 
    - gives the result in a nutural language
<br> 
- Response:
    - >>> data = link("NVIDIA") # takes natural language name of the company and disambiguates companies to Camp IQ or structured format
    - >>> today = getToday() # Built in python function
    - >>> print(getStockPrice(data, today)) 
    - NVIDIA's stock price is $401.32
- Context:
    - Linked comnpanies: [NVIDIA corp]()

- 2. Who is the VP of Investor Relations at Exxon? 
### B. understanding of time
- 3. How much was NVIDIA trading at five days ago? 
### C. Able to do maths
- 4. What is Exxon's stock price two days ago divide by its price two months ago plus its stock price two years ago? 
- 5. Is Exxon currently trading above it's average closing price over the last 10 days? If so, by how much? 

### D. Compare three different companies?
- 6. Which of the three companies has the greatest growth between: Googl, NVIDIA, Apple?

### E. Multilingual


<hr />

## Demo - Unstructured Data

### F.     Summarize Earning Calls 

Scaffolding technique in general 
- Answer 
- Reasoning 
- Context

### G. Upload a document to work with a document that you can upload. 
 

<hr />

## Demo - API Interaction

### H. Uses web APIs 
-  Switch from "Demo" to "Local"
    - "Demo" can use internet data 
    - "Local" will be using internal company data
- Example API 
    - developer.snpglobal.com/commodityinsights/servicecatalogue...
    - S&P Global Platts: World Refinery Database
- deatils of the API
    - there are these "odata" endpoints
    - there are all these different types of metadata 
        - API documentation 
        - syntax of how to use these API
        - details about the input variables - state, city, operator, refinery, etc. 
- Expose the documentation of the API to the model and create an LLM that directly calls the API. It is running the querry internally. 
- The LLM model uses the documentation to construct a queqy for the "Odata" querry 
- Example question: Yesterdays's outages in the data refinary?
    - Use python to get today's date 
    - subtract it by 1 and convert to string 
    - construct a odatabase query to create an API call 
    - Runs the python code to gets result 
    - Use Natural Language to answer in a human form

- Reasoning about a snap of time. "In the last year", "In the year so far", etc. 

- Ability needed:
    - Write and execute Python code 
    - interact with the data pulled 

<hr />

