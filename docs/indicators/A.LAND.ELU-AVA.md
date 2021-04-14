# Availability: Existing Land Use

The survey asks the question: To what extent is existing land use information available as open data? 

{% include "feedback.md" %}


    
## Definitions and identifications
    
    Land use is commonly defined as a series of operations on land, carried out by humans, with the intention to obtain products, and/or benefits through using land resources. Land use refers to the purpose the land serves, that might be residential, industrial, commercial, agricultural, forestry, or recreational.
    
    Within land use datasets, this indicator will focus on data on actual use of land: what kind of use is effectively going on in certain places. Having accurate data on this is essential to inform policies on social and economic development, natural values, environmental issues, housing, etc. Consequently, publishing land use data could be of interest to several agencies: land management, agriculture, environment, urban development, and so on.
    
    In practice, land use data collection can, amongst other approaches, be produced through satellites, surveys, or reconstructed from official documents and administrative data. Although some frameworks envisage national aggregation of land use statistics or geospatial records, granular land use data may be published by many different agencies and have different formats and features depending on the territorial extent of the publication, rural or urban dominance, and focus of the dataset. Data may also include only ground level activities, or also below and above ground land use and plans. The geographical extent of existing datasets we examined differed substantially, and researchers can expect to find points, polygons (custom or related to parcels) or grids to associate existing use to certain places. The INSPIRE Thematic Working Group on Land Use also caution that land use data tends to be very localized, and different publishing systems within a country may not be consistent with one another [(INSPIRE Thematic Working Group Land Use, 2013)](https://www.zotero.org/google-docs/?JIMmet), with the gap sometimes filled by commercial initiatives [(Deininger et al., 2011)](https://www.zotero.org/google-docs/?T3QQY3) or even research or civil society led efforts to bring together more integrated land use data.
    
    Given the diversity of possible structures for existing land use datasets, the Barometer’s existing land use availability indicator will ask for structured datasets that inform—for a given area—what kind of activities are taking place, with its geographical location. This dataset could be at national level, or could also be at local level following national directives to allow national compilations. **Metadata** describing land use nomenclatures and hierarchies is fundamental to make a better use of these kinds of datasets. Keeping existing land use data updated and keeping **registry of previous existing land uses** makes it possible to track land use evolution over time, adding a great value to this information, especially taking into account the importance of land use change analysis. Sub-question b7, that asks for historical data, is intended to track availability of data that makes land use change analysis possible, as well as concrete data on land use change. Drawing on the relevance of land-use data for climate change, we will include a specific check on whether forested areas are included as a category in a comprehensive existing land use dataset, or are available in distinct but compatible datasets, as well as protected areas.
    
    Forested areas “includes all land with woody vegetation consistent with thresholds used to define forest land in the national GHG inventory, sub-divided into managed and unmanaged, and also by ecosystem type as specified in the IPCC Guidelines. It also includes systems with vegetation that currently fall below, but are expected to exceed, the threshold of the forest land category”[(IPCC et al., 2003)](https://www.zotero.org/google-docs/?0BIIQw).
    
    *Example:  The* Australian Collaborative Land Use and Management Program (ACLUMP), has developed and [approved technical specifications](https://www.agriculture.gov.au/abares/aclump/land-use/mapping-technical-specifications) for land use mapping, and made available land use maps for [download](https://data.gov.au/dataset/ds-sa-9712e707-1a7a-464e-a4c3-980f40770d48/distribution/dist-sa-98a4aae3-54df-4381-8f98-a39fa4f30b4e/details?q=land%20use), to consume via APIs, and to [explore online](http://location.sa.gov.au/viewer/?map=hybrid&x=138.73858&y=-34.96443&z=12&uids=118&pinx=&piny=&pinTitle=&pinText=).
    
=== "Research Guidance"
    
    Start by looking for datasets at national scale that depict current land use with a geospatial reference, that may help people to understand what kind of activities land serves in a certain location. You might find digital maps and or other kind of downloadable files such as .xls, .shp, .geoJSON, etc. If there is no single national dataset or repository of local ones, look for land use datasets in smaller areas, and note that in the "extent" section of this indicator.
    
## Starting Points
    
    - **Search:**
        - Open Data Portals
        - National Geographic Institutes
        - Environment agencies
        - Land information offices
        - Geoportals
    
    - **Consult:**
        - Organisations that work with land issues.
        - Experts on Land Use land Use Change .
        - Geospatial data experts
        - Climate action advocates.
    
    **What to look for?**
    
    To complete the assessment for this question you will need to access and explore the available data. This may involve running queries on the dataset to check the variety of land uses and other features included. 
    
    Look for evidence of:
    
    - **Land use dictionary** to have a clear view of possible land uses and which nomenclature they are using.
    - Registry of **previous uses** that make possible to track changes over time.
    - **Forested areas** identified in the dataset assessed or another one found in the same environment.
    - **Protected areas** identified in the dataset assessed or another one found in the same environment.
    
    **National and sub-national considerations**
    
    Land use data might have different levels of detail, depending on the surface covered. National land use maps tend to show a small amount of categories for wide areas, while more local publications offer detailed data on land use on small units, such as parcels. If available we prioritise assessment of land use data at a national level. If you only find statistical data on land use at a national level, you can use the element on the Geospatial data to note it.
    
    As a methodological warning, it has been said that land use data tends to be very localized, and what is more, different publishing systems within a country may not be consistent with one another. And sometimes this gap is filled by commercial initiatives. In some cases, national maps are published putting together different local sources.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: General checklist**
    
    * **Data is provided in machine-readable format(s)** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where this machine-readable data can be found. (Additional URLs can be included in the justification and supporting evidence)
    
        > If Partially or Yes: Please provide a comma separated list of the formats available? (E.g. csv, json)
    
        > If Partially: What prevents you from assessing this data as fully machine-readable? 
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
    * **The machine-readable dataset is available as a whole** (No, Partially, Yes)
     *Answer no if it's only possible to access individual records; Answer partially if it's possible to export extracts of the data; Answer yes if there are bulk downloads or APIs providing access to the whole dataset without financial, technical or legal barriers.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where bulk download access is available or described.
    
        > If Partially or Yes: If bulk access is provided through an API, please provide a link to where the API is described.
    
    * **Dataset is available free of charge.** (No, Partially, Yes)
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **There are accessible and open official tools available to help users locate and explore individual records.** (No, Partialy , Yes)
     *Answer 'partially' if tools make it possible to get at extracts of data without having to download a full dataset. Answer 'yes' if there is an interactive tool that displays user-filtered extracts of the data to answer simple questions without downloading data at all.*
    
        > **Supporting questions** (conditional)
    
        > If Partialy  or Yes: Please provide URL
    
        > If Partialy : What are the main barriers to accessibility and usability?
    
    **Part 2: Dataset elements**
    
    * **The available data contains historical information that allows users to build a comprehensive picture of land use changes over time.** (No, Partially, Yes)
    
    * **Each record is categorised according to a standardised land use dictionary.** (No, Partially, Yes)
    
    * **Forested areas can be identified in available data, or in a related dataset.** (No, Partially, Yes)
    
    * **Protected areas can be identified in available data, or in a related dataset.** (No, Partially, Yes)
    
    * **Each record has a geospatial reference.** (No, Partially, Yes)
     *No: There is data about land use at a country level, but it is aggregated and cannot be mapped with detail.  Partially: Each record of land use has a geospatial reference, but it is not much detailed (e.g: state or province level). Yes: Each record has a geospatial reference to a precise location.*
    
    * **The data collection was based on:** (Satellite images, Remote sensing, Aerial photography, LiDAR, Administrative records, Volunteered geographic information (VGI), Other)
    
        > **Supporting questions** (conditional)
    
        > If Other:  What kind of source?
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     Good governance in land use has been highlighted as critical to achieve goals related to socioeconomic development, maintaining ecological systems and enabling adaptation to climate change (Quan, 2017). International organisations have highlighted effective land use and management as key in tackling environmental issues such as desertification, addressing food security, employment and migration challenges, and moving towards the 2030 Agenda for Sustainable Development.
     
     Economic development, urbanisation, and the growing demand for food and industrial materials have necessitated a rising need for land use management (Deininger et al. 2011). Therefore, the kind of activities taking place on a piece of land are key in informing policies and to tackling different land issues. When used in conjunction with land tenure or land ownership data, land use data opens up avenues to address environmental issues, corruption, land access issues, food sovereignty, housing and health and a plethora of challenges.
     
     Land use restrictions as well as land use decision processes should be transparent, efficient and predictable (Deininger et al., 2011). Thus, states are encouraged to conduct regulated spatial planning, and monitor and enforce compliance with those plans—in a way that promotes a diverse and well-balanced sustainable territorial development—taking into consideration the variety of tenure systems, and particular issues such as gendered aspects of land use and indigenous people land rights and uses (FAO, 2012). The Barometer is interested in current and historical land use data, with special attention on forest and protected areas.