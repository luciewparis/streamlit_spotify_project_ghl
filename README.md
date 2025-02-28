# Project presentation

### Context

- **Why?** Present a real-life case study / final project to demonstrate the data and project management skills acquired during the ASOD Data Analytics Bootcamp
- **When?** Second half of Feb25
  
### Objectives


- **What?** We selected 3 topics to tell a story around successful (= most streamed) tracks and artists :
    - **What does a successful track sound like?** (technical analysis of audio features)
    - **What is the impact of a successful track on other platforms?** (music, social networks)
    - **How can we select a relevant mix of popular artists for a festival?**
    
Our analyses could primarily help Spotify teams to better understand the type of music that gets the most attention and the impact on social networks, which can lead to a wide range of possible evolutions; as well as sharing those insights with industry partners (artists, labels).
  
### Contributors
👨‍💻 @ Graziella EHOUNGBAN
👨‍💻 @ Hind LAASSOULI
👨‍💻 @ Lucie WU
 
# Project structure
- Folder INPUTS: contains the original data collected, that we need to explore and clean
  - The large .csv are ignored when pushing our code to github. They can be found on BigQuery (link to provide)
- Folder NOTEBOOKS: contains the python notebooks used to clean and do the analyses
- Folder DATA: contains the cleaned data files used to run our final analyses (usually light datasets)
- .env.template: contains the credentials required for the API calls (spotify) - to be filled in with your spotify app credentials
- Folder streamlit: contains the user interface of our Streamlit-based application. It is structured to organize the different pages and resources used in the application
  - home.py: Home page that introduces the application and allows navigation to other pages.
  - Folder pages: Contains the various secondary pages accessible from Streamlit's sidebar menu.
  - Folder images: Stores images used in the application.
  - requirements.txt: Lists the necessary Python libraries to run the application
