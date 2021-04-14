# Availability: Functional areas

The survey asks the question: To what extent are geospatial functional areas available as structured open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    This indicator is concerned with data that describes the geographic boundaries used to set government responsibilities, administer elections, collect national statistics and carry out census data collection. 
    
    Geographical representation of functional areas can refer to a wide range of sub-themes, from administrative and statistical units to school catchments or agricultural zones. To narrow the scope of this indicator, we focus on a set of boundaries that allows to link relevant data to a spatial extent: 
    
    - **Administrative** boundaries: polygons for relevant administrative units, mainly smaller that state or provinces.
    - **Census** units boundaries: borders of census units that enable to map census results; these could be at a block level for example, or custom census units, but always need to be useful to get a geospatial extent of census results.
    - **National electoral** units boundarie**s**: the most granular electoral map of the country, that should work to map election results.
    - **Statistical** boundaries:  statistics are produced -and refer to- different places at different scales. We are looking for geospatial representation of relevant and constantly measured statistics on health, crime, education or poverty.
    
    These forms of data may be available as layers in a central geodata portal, or may be managed in a more distributed way, available from different agencies. In general, each form of functional area will be organised hierarchically (e.g. first level administrative boundaries covering states, containing second level administrative boundaries covering counties or municipalities and so-on) and structured data will contain information on this hierarchy. 
    
    This indicator is focused on datasets that enable geospatial analysis of different metrics, so it tracks the availability of boundaries data in formats suitable for representing polygons in space, such as .csv with WKT fields, .shp, .geoJSON, or in the forms of WMS or many others available. 
    
    Most datasets comprising functional areas geographies should include fields with their geometry, including: level (in the hierarchy), code, name, and function. 
    
=== "Research Guidance"
    
    - **Search:**
        - Geoportals
        - National Statistics Offices websites may provide these kinds of spatial datasets to map their statistics.
        - National mapping agencies portals
    
    - **Consult:**
        - Professionals that work with statistics and administrative public data
        - Experts in GIS and data for public good
        - Geospatial data communities
        - Open Data communities
    
    **What to look for?**
    
    Look for evidence that can answer the following questions:
    
    - Are there datasets with functional areas available online?
    - Are they free, updated, machine readable and accesible as a whole?
    - Which of these kinds of datasets are available?
        - Census units?
        - Electoral units?
        - Administrative borders?
        - Statistical units?
    
    **National and sub-national considerations**
    
    As was stated in the Governance questions, having integrated national frameworks and datasets is desirable to take the most of geospatial data, therefore some countries might have all these datasets available through the same website. However, we can not expect this to be the case everywhere, and each state or province could have its own geoportal, or even publish this information in different agencies websites. If this information is not centralized, at the "Extent" part of the question you will assess if the data found is an outlier or a general rule in the country.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: Data Coverage**
    
    * **A map with administrative boundaries is available.** (No, Partially, Yes)
    
    * **A map with census units is available.** (No, Partially, Yes)
    
    * **A map with electoral units is available.** (No, Partially, Yes)
    
    * **A map with statistical units is available.** (No, Partially, Yes)
    
    **Part 2: Data Structure and Openness**
    
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
    
    **Part 3: Data fields**
    
    * **The datasets have a field with the geometry of functional areas.** (No, Partially, Yes)
    
    * **The dataset have a field with the level of hierarchy each functional area.** (No, Partially, Yes)
    
    * **Each geometry has a code that enables the geospatial representation of data published in other datasets.** (No, Partially, Yes)
    
    * **The datasets have a field with the name of each functional area.** (No, Partially, Yes)
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     Geospatial datasets are key to tackle different kinds of challenges of a wide range of natures: social, economical, environmental, accountability, and so on. When it comes to picking up the availability of specific datasets to assess country against, there exist a plethora of options given the varied topics and themes in which geospatial data is crucial. That is why the Working Group on Global Fundamental Geospatial Data Themes from the UN-GGIM has selected and defined 14 Fundamental Data Themes,  that are meant to be a solid foundation to support global geospatial information management, specifically used to support the Integrated Geospatial Information Framework, among other global initiatives to strengthen geospatial information, within each countries, but also taking into consideration global initiatives and the 2030 Sustainable Development agenda.
     
     By Fundamental Data Themes, the UN-GGIM refers to "the minimum primary sets of data that can not be derived from other data sets, and that are required to spatially represent phenomena, objects, or themes important for the realisation of economic, social, and environmental benefits consistently" (UN-GGIM, 2019) across a country, at the local, national and regional levels.
     
     Within the selected fundamental datasets, this indicator will focus on **Functional Areas**, defined as "the geographical extent of administrative, legislative, regulatory, electoral, statistical, governance, service delivery and activity management areas", which are key to take the most of data analysis to inform located public policies, and which are not being covered by other GDB indicators.