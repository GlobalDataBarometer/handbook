# Availability: Real-time healthcare system capacity

The survey asks the question: To what extent is information about the real-time capacity of the healthcare system available as open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    To be useful, data about the real-time capacity of the healthcare system should be available at the level of individual facilities and include details such as the number, type, and availability of beds, tests, vaccines, ventilators, and staff.
    
    Among other functions, it should be possible for different actors to use data about the real-time capacity of the healthcare system in various ways:
    
    - for everyday individuals to locate where to take loved ones for treatment or where to obtain vaccines;
    - for journalists, civil society organizations, and government officials to identify disparities in the healthcare system that will disproportionately impact members of marginalized communities;
    - for government officials to determine where and when to build surge or overflow facilities;
    - for healthcare providers to direct patients with COVID-19 symptoms to facilities with the current capacity to treat them;
    - for a wide range of actors to understand where resources are scarce and work to fill gaps in personal protective equipment (PPE), medical devices, vaccines, etc.
    
    This indicator emerges from data practices observed in conjunction with the coronavirus pandemic; the working assumption is that data will be found on COVID-19-related websites, run by the government, academia, or civil society.
    
    In countries where infection counts have significantly decreased, this data may have been available in 2020 but no longer be being updated in 2021. Many government COVID-19 response sites include archives of past data; we suggest checking the date ranges corresponding to peaks of infection in your country. However, if these peaks happened early in the global progression of the pandemic, we also recommend checking archives a couple of months later, as countries' data-reporting practices have evolved considerably over the course of the pandemic.
    
=== "Research Guidance"
    
    **Starting points**
    
    - **Search:**
        - National or sub-national government websites about how and where to go for testing and treatment of COVID-19.
        - Websites of civil society organizations or mutual aid societies that provide information about testing or treatment of COVID-19.
        - Websites of your country's national or local public health department, center for disease control, or center for health statistics.
    
    - **Consult:**
        - Public health officials.
        - Records and analytics staff at healthcare facilities who are likely to know what information is reported, to whom, and how often.
        - Open data experts, programmers, and technologists who have organized data collaboratives or participated in other data-related efforts for COVID-19 response and recovery.
    
    **What to look for?**
    
    To complete the assessment for this question you will need to access and explore the available data. This may involve running queries on datasets to check the variety of fields included.
    
    Look for evidence that can answer the following questions:
    
    - Does the data include information about the capacity of individual facilities that reflects real-time or very recent changes? Or does capacity information only speak to long-term capacity, not how it is currently being used?
    - Does the data include specific details, such as the number and availability of beds, staff, tests, vaccines, and ventilators?
    
    **National and sub-national considerations**
    
    In some countries, sub-national departments of health may have different practices with regard to what capacity data they make available. Additionally, in some countries, data may be available only for hospitals in major cities.
    
    Focus on **national government** first, and then assess whether:
    
    - National datasets also include data from sub-national or local government units;
    - Equivalent data exists for a selection of sub-national or local government units, but is not nationally aggregated;
    
    To assess countries where data about healthcare system capacity is organized sub-nationally, researchers should select the strongest example of sub-national practice, and then indicate whether this is an outlier, or an example of widespread practice.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: Data structure and openness.**
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **Dataset is available free of charge.** (No, Partially, Yes)
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
    * **The collection and publishing of this data is accessible through screen readers, call relays, or similar mechanisms.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please briefly describe the accessibility coverage available.
    
    * **Data is available in all the country’s official or national languages. If the country has no official or national languages, data is available in the major languages of the country.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please briefly describe the language coverage available.
    
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
    
    **Part 2: Data fields assessment.**
    
    * **The data includes information at the level of facilities.** (No, Partially, Yes)
    
    * **The data includes detailed information about the number and availability of regular beds and ICU beds.** (No, Partially, Yes)
    
    * **The data includes detailed information about the number, type, and availability of COVID-19 tests.** (No,  Partially, Yes)
    
    * **The data includes detailed information about the number, type, and availability of staff.** (No, Partially, Yes)
    
    * **The data includes detailed information about the number, type, and availability of COVID-19 vaccines.** (No, Partially, Yes)
    
    * **The data includes detailed information about the number and availability of medical devices such as ventilators.** (No, Partially, Yes)
    
    **Part 3: Barriers to data quality or availability.**
    
    * **This information is missing required data.** (There is no evidence of data gaps., There is evidence that a portion of mandated data is missing., There is evidence of widespread omissions in mandated data.)
     *In cases where a separate indicator has asked you to determine data requirements of a relevant governing framework, assess against that. In cases where there is no such related governance indicator, assess based on the parameters laid out in the publication of the information, your local knowledge, and any broader research you may have done for this theme.*
    
        > **Supporting questions** (conditional)
    
        > If There is evidence that a portion of mandated data is missing. or There is evidence of widespread omissions in mandated data.: Please briefly explain.
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     Healthcare system capacity data supports governments and other actors in distributing resources to ensure healthy lives and promote well-being for all at all ages (SDG 3). This is particularly critical in the urgency of a public health crisis like the coronavirus pandemic. As the WHO COVID-19 Strategic Preparedness and Response Plan (SPRP 2021) notes, "Health care systems and workers...are under extreme pressure in many countries in terms of capacity and capabilities, financial resources, and access to vital commodities and supplies including medical oxygen" (8). Real-time or very recent data about a healthcare system's capacity is critical to directing patients to available care and distributing resources equitably and effectively. 
     
     With the rise of highly infectious COVID-19 variants, the continued dynamic and uncertain course of the pandemic, and the uneven global distribution of vaccines, it will be considerable time before the pandemic is contained. In the meantime, real-time capacity data not only helps public health departments respond to changes in the pandemic, it also helps ensure the continuity of essential health services and provides a foundation from which to build readiness for other health emergencies.