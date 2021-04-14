# Availability: Road Traffic Accidents

The survey asks the question: To what extent is information on traffic accidents available as open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    Different government agencies and non governments institutions collect data and report on traffic crashes, whereas police departments, private and public hospitals, transportation agencies, etc. This kind of data, when structured collected, updated, and available, is a key input to inform policies towards reducing mortality rate as consequence of traffic crashes. 
    
    This data can be made available as statistics, with different categories and level of disaggregation (by region, type of accident, age, gender, etc.), and also can be released in a more granular way, publishing information of every crash registered. This latter way, can also have more or less details on causes and consequences, conditions, or description of people involved. 
    
    To assess this indicator, any of this data kinds is useful, and the difference will be in the level of disaggregation of statistic or columns available in a granular. However, only the latter will be able to receive the highest score in geographical reference element, which needs  latitude and longitude coordinates.
    
    For example, [Barcelona´s Open Data Portal](https://opendata-ajuntament.barcelona.cat/data/es/dataset/accidents-gu-bcn/resource/bcfc0866-7e2a-4054-9a93-fb3f371fc5eb) provides detailed data on traffic crashes, as well as the region of [Neiva](https://www.datos.gov.co/Transporte/Muertes-en-accidentes-de-tr-nsito/ffwz-fiy4), in Colombia, through their national Open Data Portal. UK Department of Transport, includes in its road traffic statistics, data [on road accidents](https://roadtraffic.dft.gov.uk/custom-downloads/road-accidents/reports/31276e4c-9c22-432c-9900-5d120129c79c)
    
=== "Research Guidance"
    
    **Starting points**
    
    - **Sources:**
        - For OECD countries, [IRTAD road safety database](https://www.itf-oecd.org/irtad-road-safety-database) shows yearly statistics, and links to each county's source.
    - **Search:**
        - National and local open data portals.
        - National and local statistics offices.
        - Transportation and or health agencies and their open data portals.
    
    - **Consult:**
        - Specialists on traffic crashes.
        - Geodata and transport data community.
    
    **What to look for?**
    
    To complete the assessment for this question you will need to access and explore the available data. This may involve running queries on datasets to check the various aspects. 
    
    Look for evidence of:
    
    - **Type of accident:** sideswipe collision, T-bone collision, car-pedestrian crash, etc.
    - **Cause(s) of the crash:** speeding, alcohol, bad road conditions, etc.
    - **Road type:** motorways, urban roads, etc.
    - **Type of** r**oad user:** pedestrians, cyclists, car occupants, etc.
    - **Age** of people involved
    - **Gender** of people involved
    - **Seat position in the car of** people involved
    - **Consequences of the crash:** fatalities, injuries, etc.
    - **Post crash care:** What kind of support did people involved received? How long did they last to get there?
    - **Safety data:** What safety elements were used, such as helmets or seatbelts? Which safety features did the vehicles have?
    - **Geospatial reference of the crash:** Look for the most precise reference. Province, regional, or neighborhood, or latitude and longitude references.
    
    **National and sub-national considerations**
    
    Focus on **national government** first, and then assess whether:
    
    - National datasets also include data from sub-national or local government units;
    - Equivalent data exists for a selection of sub-national or local government units, but is not nationally aggregated;
    
    If there is no evidence of road traffic accidents data being available at the national level, but there is a strong example of data availability from a sub-national government, or a specific agency, you may carry out an assessment for this data, and use the extent question to note that this only covers a very limited number of road traffic accidents.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: How open is the dataset?**
    
    * **Data is provided in machine-readable format(s)** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where this machine-readable data can be found. (Additional URLs can be included in the justification and supporting evidence)
    
        > If Partially or Yes: Please provide a comma separated list of the formats available? (E.g. csv, json)
    
        > If Partially: What prevents you from assessing this data as fully machine-readable? 
    
    * **The machine-readable dataset is available as a whole** (No, Partially, Yes)
     *Answer no if it's only possible to access individual records; Answer partially if it's possible to export extracts of the data; Answer yes if there are bulk downloads or APIs providing access to the whole dataset without financial, technical or legal barriers.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where bulk download access is available or described.
    
        > If Partially or Yes: If bulk access is provided through an API, please provide a link to where the API is described.
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **There are accessible and open official tools available to help users locate and explore individual records.** (No, Partialy , Yes)
     *Answer 'partially' if tools make it possible to get at extracts of data without having to download a full dataset. Answer 'yes' if there is an interactive tool that displays user-filtered extracts of the data to answer simple questions without downloading data at all.*
    
        > **Supporting questions** (conditional)
    
        > If Partialy  or Yes: Please provide URL
    
        > If Partialy : What are the main barriers to accessibility and usability?
    
    **Part 2: Which fields does the dataset contain?**
    
    * **The data contains information about the type of accident (sideswipe collision, T-bone collision, car-pedestrian crash, etc).** (No, Partially, Yes)
    
    * **The data contains potential cause(s) of the collision (speeding, alcohol, bad road conditions, etc.)** (No, Partially, Yes)
    
    * **The data contains the type of road where the event occurred (motorways, urban roads, etc.)** (No, Partially, Yes)
    
    * **The data contains information about the type of road user (pedestrians, cyclists, car occupants, etc.)** (No, Partially, Yes)
    
    * **The data contains the age of people subjects of data.** (No, Partially, Yes)
    
    * **Data includes information about individuals' sex or gender.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please briefly describe what data includes sex or gender information.
    
    * **Data contains the seat position in the car of people involved.** (No, Partially, Yes)
    
    * **The data contains detailed consequences of the crash (injuries, fatalities, hospitalization)** (No, Partially, Yes)
    
    * **Data contains information about the post crash-care, including waiting time.** (No, Partially, Yes)
    
    * **The data contains safety measures adopted by people involved (use of helmet, seatbelt, car safety features, etc.).** (No, Partially, Yes)
    
    * **Each record has a geospatial reference that allows to assign features to a spatial extent.** (No, Partially, Yes)
     *The geospatial reference might be latitude-longitute coordinates, an ID to associate it to a geospatial dataset, an address, etc. "Partially" is intended for cases where a geographical reference exists, but it could have been more precise, for example, when the neighbourhood is informed, but there are no clear reasons for not to inform latitude-longitude coordinates. Will be assessed with "Yes" datasets that have the most granular geographic references that can be expected for its kind.*
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     Road traffic injuries are the leading cause of death for children and young adults aged 5–29 years and approximately 1.35 million people die each year as a consequence of traffic crashes, while between 20 and 50 million people suffer non-fatal injuries. These events cost to some countries 3% of their gross domestic product. As with other phenomena, this connects with development status: more than 90% of fatal crashes occur in low- and middle-income countries, although they have only approximately 60% of the world's vehicles  ([WHO](https://www.who.int/news-room/fact-sheets/detail/road-traffic-injuries)).
     
     SDG 3, on good health and well-being, includes target 3.6, which seeks to reduce global deaths and injuries from road traffic accidents. This goal was framed by UN General Assembly resolution 74/299 on "Improving global road safety;" further, the General Assembly proclaimed 2021–2030 the Decade of Action for Road Safety ([WHO](https://www.who.int/groups/united-nations-road-safety-collaboration/decade-of-action-for-road-safety-2021-2030)).
     
     Accurate, updated, and detailed data on traffic crashes is key to informing and shaping policies to reduce road mortality. However, a great number of countries lack accurate and accessible data about traffic crashes, particularly low-income countries that need it the most to improve policies to reduce mortality [(World Bank)](https://blogs.worldbank.org/opendata/finding-missing-data-creating-actionable-information-solving-development-problems?cid=dec_tt_data_en_ext#_ftn1).