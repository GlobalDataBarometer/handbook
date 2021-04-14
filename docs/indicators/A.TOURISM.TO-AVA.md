# Availability: Transit data

The survey asks the question: To what extent are public transport timetables available as structured open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    Transit data include full route maps and schedules of all transit lines serving the study area, locations of transit stops, and transit vehicle capacities, containing details of when (times) and where (stops) public transport services, such as buses and rail services, are expected to operate
    
    An increasing number of public transport (PT) agencies publish their route and schedule data with the General Transit Feed Specification (GTFS, [https://developers.google.com/transit/gtfs/](https://developers.google.com/transit/gtfs/)) as the standard, open format. GTFS specifies how to present public transport service supply with a series of CSV (comma-separated-values) plain text files constituting a GTFS feed. GTFS data is primarily used for PT passenger routing, but it can also be used for research, for instance for modeling PT-provided accessibility. The data standard offered by the GTFS format facilitated the process for agencies to integrate schedules and routes into Google Maps (now Google Transit), and for broader public disclosure of those same data sets. Thus GTFS standard is becoming more popular every day, it is not the only format in which PT data can be released, so for this indicator other kinds of datasets can also be assessed. 
    
    Public transport data should be re-used to build user friendly interfaces to plan trips, to perform analysis on places' connectivity, to inform public transport policies and planning, as well as manage the effects of tourism. 
    
=== "Research Guidance"
    
    Start by identifying the national agency in charge of transit data and access their official website. Look for the National Transit Map/s which are nationwide catalogues of fixed-guideway and fixed-route transit service in the country that is gleaned from publicly available information. If you do not find data at national level, identify local agencies and local open data portals.  Then look for the most comprehensive dataset of public transport data and assess it. If related relevant data is in the same environment you can assess more than one dataset to complete the elements assessment on the fields available.
    
    Examples:
    
    - [London Transit](http://www.londontransit.ca/open-data/) Open Data page, although not entirely up to date, offers good examples of different ways to release public transportation data: GTFS, Real Time GTFS, Spatial Data to explore with GIS software and Tabular Data.
    - [Community Transit](https://www.communitytransit.org/opendata), from Seattle, US, also offers public transport data in different formats.
    
    **Starting points**
    
    - **Sources:**
        - [Transit Feeds](http://transitfeeds.com/) provides is an extensive archive of official public transit data. You can search by location and find links to data providers websites
        - [Transit land](https://www.transit.land/) is a community edited data service that aggregates transit networks across metropolitan and rural areas around the world. Data providers websites can also be found as references.
    - **Search:**
        - National Transit Maps
        - Local transit agencies or companies or other institutions in charge of local tranportation services.
        - Cities Open Data Portals
    - **Consult:**
        - Public transport policy specialist
        - Transport researchers
        - Geospatial and transit data local communities.
    
    **What to look for?**
    
    To complete the assessment for this question you will need to access and explore the available data. This may involve reading meta-data and field descriptions, and making queries on the dataset to check the variety data. 
    
    Look for evidence of:
    
    - Public transport stops
    - Public transport routes
    - Scheduled times
    - Real time location of public transport facilities
    - Real time alerts on events that affect public transport service.
    
    **National and sub-national considerations**
    
    Focus on **national government** first, and then assess whether:
    
    - National datasets also include data from sub-national or local government units;
    - Equivalent data exists for a selection of sub-national or local government units, but is not nationally aggregated;
    
    If there is no evidence of public transit data being available at the national level, but there is a strong example of data availability from a sub-national government, or a specific agency, you may carry out an assessment for this data, and use the extent question to note that this only covers a very limited number of public transport services.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: How open is the dataset?**
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **The machine-readable dataset is available as a whole** (No, Partially, Yes)
     *Answer no if it's only possible to access individual records; Answer partially if it's possible to export extracts of the data; Answer yes if there are bulk downloads or APIs providing access to the whole dataset without financial, technical or legal barriers.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where bulk download access is available or described.
    
        > If Partially or Yes: If bulk access is provided through an API, please provide a link to where the API is described.
    
    * **Dataset is available free of charge.** (No, Partially, Yes)
    
    * **Data is provided in machine-readable format(s)** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where this machine-readable data can be found. (Additional URLs can be included in the justification and supporting evidence)
    
        > If Partially or Yes: Please provide a comma separated list of the formats available? (E.g. csv, json)
    
        > If Partially: What prevents you from assessing this data as fully machine-readable? 
    
    **Part 2: Which fields does the dataset contain?**
    
    * **The data contains public transport stops and routes.** (No, Partially, Yes)
    
    * **The data contains scheduled times.** (No, Partially, Yes)
    
    * **Data contains real time location of public transport.** (No, Partially, Yes)
    
    * **Data contains real time alerts that affect public transportation services.** (No, Partially, Yes)
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     SDG 11 calls for making "cities and human settlements inclusive, safe, resilient and sustainable", and its target 11.2 leads to a safe, affordable, accessible and sustainable transport system for all, expanding public transport with an inclusive approach. To achieve these goals, open public transport data is a key asset, as highlighted by the 2003 Digital Agenda for Europe and by World Bank Open Transport Team, that included it as part of next generation of tools and methodologies for managing and planning transport systems in resource constrained environments.
     
     Given the relevance of this indicator for both transportation and tourism & leisure thematic modules, this indicator plays a double importance. Transport is the cause and the effect of the growth of tourism. The improved facilities have incited tourism, and the expansion of tourism has incited the development of transport infrastructure. In an attempt to acknowledge the global role of tourism, the United Nations General Assembly declared 2017 the ‘International Year of Sustainable Tourism for Development’ (UNWTO, 2018). However, assessment of the achievement of sustainable development goals in tourism has revealed significant disparities in methods of measurement and consequently some difficulty in integrating various statistics at relevant spatial scales, e.g., local, national and global (UNWTO, 2018).
     
     Thus, open transport data has the potential to greatly benefit both citizens and the public sector. Public transport will only be widely used if the service is effective, efficient and user-friendly. Information that can help citizens (and tourists, specifically) plan their journey in advance can help enhance service and ultimately facilitate greater use. Additionally, although the transport service may be run by a private company, most of the information is non-sensitive and may be released openly. Therefore, municipalities and local governments should put forth effort in opening the information on public transport under machine-readable and easy to use formats. (Open Data Handbook).