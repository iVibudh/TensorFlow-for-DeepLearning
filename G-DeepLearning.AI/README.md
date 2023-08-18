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


## Best Monitors for your workstation:
1. [ViewSonic VA3209M 32 Inch IPS Full HD 1080p Monitor with Frameless Design, 75 Hz, Dual Speakers, HDMI, and VGA Inputs for Home and Office](https://amzn.to/449E6i1) $210 but no reviews strange? 
2. [SAMSUNG 32-inch M5 Smart Monitor with Mobile Connectivity, FHD, Remote Access, Office 365 (LS32AM500NNXZA), Black (Renewed)](https://www.amazon.ca/gp/product/B08RCLHKN5?smid=A30HNTWRKP3TVT&th=1&linkCode=ll1&tag=thoughtfulpic-20&linkId=92af2acfd2928a48ef1c61cd66be87c8&language=en_CA&ref_=as_li_ss_tl) $285 - most expensive on the list
3. [Acer 32" 1080P 1920 X1080 @60Hz, 4ms, IPS HDMI, EB321HQ Awi](https://www.amazon.ca/gp/product/B0797M3SVG?smid=A3DWYIK6Y9EEQB&th=1&linkCode=ll1&tag=thoughtfulpic-20&linkId=711f0d2ce48f669e315bcc02968dded2&language=en_CA&ref_=as_li_ss_tl) $210 cheapest on the list but monitor not adjustable.
4. Alternate to no. 1 [ViewSonic 32 Inch 1080p Widescreen IPS Monitor with Ultra-Thin Bezels, Screen Split Capability HDMI and DisplayPort (VX3276-MHD)](https://www.amazon.ca/gp/product/B0787WGCXT?smid=A3DWYIK6Y9EEQB&th=1&linkCode=ll1&tag=thoughtfulpic-20&linkId=d3a48df8c97c289d99ae136291814824&language=en_CA&ref_=as_li_ss_tl)