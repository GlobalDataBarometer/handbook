# Availability: National Map

The survey asks the question: To what extent is a digital national map available as structured open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    This indicator is focused on the availability of an official national map in digital format **provided by the authoritative national mapping or geographic institution**. A digital map will have key features, such as boundaries, rivers, forests, roads, human settlements, and other important infrastructure represented as distinct data points or layers that can be turned on or off (either in an online viewer, or in the exported bulk data), as opposed to showing this information through a simple scanned drawing or image. 
    
    Whilst most countries have an authoritative national map provider, the nature of these organisations can vary from country to country, and some mapping responsibilities may exist at a sub-national level. 
    
    Access to structured mapping data can be provided through bulk downloads (often in formats such as Shapefiles (.shp), Well Known Text (WKT), GeoJSON (.geoJSON), KML, Geopackages or Geodatabases). Mapping platforms may also provide APIs for accessing data. 
    
    Note: Web Mapping Services (WMS) provide access to tile ***images*** from a map, but generally do not provide access to structured data on map features. 
    
=== "Research Guidance"
    
    Start by identifying the National Agency in charge of providing official maps of the country. Once in their website look for the availability of a Digital National Map with relevant map features such as official administrative borders, roads and other important infrastructure. Once they are identified answer the "Existence" part of the indicator and proceed to assess the "Elements". 
    
    **Starting points**
    
    - **Sources:**
        - The International Cartographic Association provides a [list of its national members](https://icaci.org/national-members/), many of them the National Mapping Agencies in their countries.
        - This Wikipedia entry provides a crowdsourced [list](https://en.wikipedia.org/wiki/National_mapping_agency) of National Mapping Agencies.
    - **Consult:**
        - Geographers
        - Geospatial data communities
        - Geospatial data experts
    
    **What to look for?**
    
    Look for evidence that can answer the following questions:
    
    - Is there a digital national map provided by a National Mapping Agency with official and updated borders?
    - Does this map have other relevant features such as rivers, forests, roads, human settlements, and other important infrastructure represented as distinct data point? Or can they be found in the same environment?
    
    **National and sub-national considerations**
    
    If there is no national map provided by a national agency, look for sub-national mapping agencies, that may also have mapping responsibilities. Assess the most complete one, and express either it is an outlier or the general rule in the "Extent" component of this indicator.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: Data Structure and Openness**
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **Dataset is available free of charge.** (No, Partially, Yes)
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
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
    
    * **The collection and publishing of this data is accessible through screen readers, call relays, or similar mechanisms.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please briefly describe the accessibility coverage available.
    
    **Part 2: Data formats**
    
    * **Openly licenses and structured map data is available to download and open locally.** (No, Partially, Yes)
     *Look for evidence of formats such as ShapeFile (.shp), WKT, .geoJSON, KML, Geopackages or Geodatabases. Answer partially if only some of the digital features available can be downloaded as structured data, or under an open license.*
    
        > **Supporting questions** (conditional)
    
        > If Partially: 2: In which file formats is it available?
    
    * **Maps and their features ara accesible through Web Map Service(s).** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes:  Please provide urls of those services.
    
    * **There are accessible and open official tools available to help users locate and explore individual records.** (No, Partialy , Yes)
     *Answer 'partially' if tools make it possible to get at extracts of data without having to download a full dataset. Answer 'yes' if there is an interactive tool that displays user-filtered extracts of the data to answer simple questions without downloading data at all.*
    
        > **Supporting questions** (conditional)
    
        > If Partialy  or Yes: Please provide URL
    
        > If Partialy : What are the main barriers to accessibility and usability?
    
    **Part 3: Data features**
    
    * **Historical mapping data is available, to track change over time.** (No, Partially, Yes)
    
    * **Datasets have clear metadata explanations that help users to understand data source and the meaning of data fields** (No, Partially, Yes)
    
    * **S: Map features** (No, Partially, Yes)
    
    * **Available national maps has layers with features such as official national borders, sub-national or administrative borders,  rivers, forests, transport information and other relevant information.** (No, Partially, Yes)
    
    **Extent**
    
    * **S: Geographic Extent of National Map**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     National Mapping Agencies and or National Geographic Institutes are responsible for providing official, updated and reliable topographic information about a country, including:
     
     - Official borders;
     - Natural landscapes;
     - Human made landscape, infrastructure and build elements.
     
     Publicly provided mapping data plays an important role across many sectors (including business, defence, environmental action and spatial planning), and underpins many forms of data use and analysis. In many countries, national mapping data is the foundation for a significant market in private sector products and services. 
     
     This indicator provides continuity with Open Data Barometer indicator D1 which looked for *"detailed digital political map of the country provided by a national mapping agency with key features such as official administrative borders, roads and other important infrastructure"*.