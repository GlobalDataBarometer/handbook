# Availability: Planned Land Use

The survey asks the question: To what extent is planned land use information available as open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    Planned land use data is generally composed of spatial plans, defined by spatial planning authorities which depict intended or possible utilization of the land in the future.
    
    For the purposes of the Barometer we are primarily interested in the digitisation and availability of geospatial representations of planned land use, that provide adequate meta-data on the nature of the planned or permitted uses of the land.
    
    Regulations related to land-use planning are often drawn from a range of legal and administrative frameworks, and respond to country-specific planning laws and policies. This means the exact available datasets will differ from country to country, region to region, or land-type to land-type (urban/rural etc). For example, there may be some datasets with specific thematic zoning—planned mining zones, concession, protected areas—and other more detailed datasets that depict planned or permitted land uses for every parcel or another spatial unit within a city, municipality, state, province or country.  The focus of this indicator is in the latter, and it is expected to be more at a city or region level.
    
    Along with detailed and comprehensive spatial representation of permitted land uses, data can be found on specific building permits—authorization required to modify and or begin new buildings, focused on its structure—or development applications—process to ensure that new land developments meet planning land use requirements and takes into consideration the effect that they might have in the surrounding environment. The main assessment for this indicator is focused on the former, but some sub question elements will ask if the latter. Information is also available in the same environment, as could be the city's Open Data Portal.
    
    *Examples:* Buenos Aires city Open Data Portal publishes the [“Código urbanístico”,](https://data.buenosaires.gob.ar/dataset/codigo-urbanistico) mapping every land parcel in the city, with a code described in regulations, that explains what uses and kinds of buildings are permitted there. It is shared along with metadata describing each column, as well as a linked document explaining the legal framework and the context of data released. The City Government has also released a web tool to easily [explore this information](https://ciudad3d.buenosaires.gob.ar/). The Open Data portal also publishes a dataset on [building permits registered](https://data.buenosaires.gob.ar/dataset/obras-registradas).
    
=== "Research Guidance"
    
    Start by looking for national repositories of local land use plans. If there are none, explore in local  Open Data portal or government website. The kind of datasets that we are looking for here include a spatial representation of allowed land uses, and is also assessed if in the same environment data can be found on building permits and development applications.
    
    **Starting points**
    
    - **Search:**
        - Open Data Portals
        - Main cities websites
        - Geographic institutes
        - Land information agencies
    
    - **Consult:**
        - Spatial planning experts
        - Rural and urban development advocates
    
    **What to look for?**
    
    Look for evidence that can answer the following questions:
    
    - Are spatial plans that depict rights and obligations regarding land use publicly available?
    - Are these spatial plans georeferenced?
    - Can they be easily linked with laws and regulations from which they are derived?
    - Is there information about building permits and development applications?
    
    **National and sub-national considerations**
    
    Planned land use data might have different levels of detail, depending on the surface covered. National land use maps tend to show a small amount of categories for wide areas, while more local publications offer detailed data on land use on small units, such as parcels. 
    
    This indicator is focused on granular data, so it is expected to find data at a city or region level.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: General checklist**
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **Dataset is available free of charge.** (No, Partially, Yes)
    
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
    
    * **There are accessible and open official tools available to help users locate and explore individual records.** (No, Partialy , Yes)
     *Answer 'partially' if tools make it possible to get at extracts of data without having to download a full dataset. Answer 'yes' if there is an interactive tool that displays user-filtered extracts of the data to answer simple questions without downloading data at all.*
    
        > **Supporting questions** (conditional)
    
        > If Partialy  or Yes: Please provide URL
    
        > If Partialy : What are the main barriers to accessibility and usability?
    
    **Part 2: Dataset elements**
    
    * **Each record has a geospatial reference that allows to assign features to a spatial extent.** (No, Partially, Yes)
     *The geospatial reference might be latitude-longitute coordinates, an ID to associate it to a geospatial dataset, an address, etc. "Partially" is intended for cases where a geographical reference exists, but it could have been more precise, for example, when the neighbourhood is informed, but there are no clear reasons for not to inform latitude-longitude coordinates. Will be assessed with "Yes" datasets that have the most granular geographic references that can be expected for its kind.*
    
    * **Data is linked to spatial plans and regulations from where it is derived.** (No, Yes)
    
    * **Data is available on building permits.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes:  Please provide url to find the source.
    
    * **Data is available on development applications.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes:  Please provide the source url.
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     Good land use governance is critical to achieve goals related to socioeconomic development, maintaining ecological systems, and enabling adaptation to climate change Quan (2017). Information on permitted land uses is critical for different stakeholders to address developmental challenges that communities face, because according to Davies and Chattapadhyay (2019), sustainable development relies more on land use rather than land ownership.
     
     Therefore, effective land use and management is important to optimise the different development projects as well as charting the course for alignment with the 2030 Agenda for Sustainable Development. Consequently, the availability of information about planned land use is a key asset to inform land policies that have a bearing on almost every aspect of human life. Considering that efficient land use is a matter of public interest, Deininger et al. recommend in the Land Governance Assessment Framework that land use restrictions and land use decision processes are transparent, efficient, and predictable . Hence, states are encouraged to conduct regulated spatial planning, and monitor and enforce compliance with those plans in a way that promotes a diverse and well-balanced sustainable territorial development, taking into consideration the variety of tenure systems, and particular issues such as gendered aspects of land use and the land rights and uses of indigenous people (FAO, 2012).