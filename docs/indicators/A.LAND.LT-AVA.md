# Availability: Land Tenure

The survey asks the question: To what extent is detailed and structured land tenure data available for re-use? 

{% include "feedback.md" %}


    
    **Definitions and Identification**
    
    A land tenure dataset identifies rights held over land. It can be used to understand the land ownership landscape in a country, to identify land concentration, to understand access to land and land tenure security, and for anti-corruption purposes.
    
    Land tenure datasets usually rely on the existence of a national land registration system and database, and should provide information regarding specific parcels of land, and then either:
    
    - the rights held with respect to those parcels (e.g. whether it is owned land, common land or unregistered); and/or
    - the actual subjects—people or entities—holding tenure rights.
    
    A dataset that only provides details of land parcels, without any information on tenure rights over them, is not considered as a land tenure dataset for this survey.
    
    In some cases, information on individual rights holders may be available under more restrictive licenses than general rights information. In these cases, you can indicate that data on individual subjects is ‘partially’ available.
    
    There may be cases in which available datasets only cover one kind of right hold: e.g. Datasets of state owned land, ownership by legal persons, or land concessions and customary land tenure. In these cases, conduct your assessment for the ‘most open’ dataset(s), and indicate via the elements and extent components which kinds of tenure or data subject are covered.
    
=== "Research Guidance"
    
    Start by identifying the agency or agencies in charge of land registration and or collection and publication of land tenure data. Look for registres, cadastres and any other institution working with any type of land tenure data—. In some countries, there are departments in charge of the collection and publication of land related data, usually related with other kinds of geospatial data.
    
    **Starting points**
    
    - **Sources:**
        - The [World Bank Doing Business Ranking](https://www.doingbusiness.org/en/data/exploretopics/registering-property) contains a subindex on Transparency of information, inside the topic "Registering property", that tracks who is able to obtain information on land ownership at the agency in charge of immovable property registration, and links to them are provided. Be aware that this information is only gathered for the largest business cities in each country.
    - **Search:**
        - Releases of cadastral/registries data
        - Geospatial datasets
        - Government, CSO or international organisations reports on land tenure
    - **Consult:**
        - Organisations that work with land tenure issues—might be regarding tenure security, anti corruption, economic development, etc.
        - Experts on land registration/land rights
        - Geospatial data experts
        - Rural reform advocates/experts
        - Land information agencies
        - Land registration agencies and/or national cadaster
        - GeoData agencies
        - Open Data portals
    
    **What to look for?**
    
    Look for evidence that the data covers each of the following kinds of land tenure:
    
    - **Land tenure** involving natural persons and land tenure involving legal persons—some datasets may only cover land owned by individuals, or some countries may make data about corporate (company) land ownership more accessible as open data.
    - **State lands**—in some cases, data about the land owned by government entities is managed separately. It may not be included in the main tenure dataset—where a main tenure dataset is closed access—state lands may be in a separate open dataset. Land concessions information might also be along with state land data.
    - **Communal lands**—this is tenure held by communities, and may include records of indigenous lands and reservations.
    - **Open access lands**—this is land anyone can access, and may include national parks or common land.
    - **Urban tenure and rural tenure**—some tenure datasets only cover urban or rural land. Check whether both are included, or whether separate datasets exist for urban and rural areas.
    
    **National and sub-national considerations**
    
    Land data can often be fragmented when it exists, in spite of recent efforts to centralise it. Legal and policy national frameworks will guide you to local frameworks and local responsible agencies, and thus to local data sources.

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
    
    * **The machine-readable dataset is available as a whole** (No, Partially, Yes)
     *Answer no if it's only possible to access individual records; Answer partially if it's possible to export extracts of the data; Answer yes if there are bulk downloads or APIs providing access to the whole dataset without financial, technical or legal barriers.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where bulk download access is available or described.
    
        > If Partially or Yes: If bulk access is provided through an API, please provide a link to where the API is described.
    
    * **Data is openly licensed.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If No: If there are explicit restrictions placed on re-use of the dataset, briefly describe those here.
    
        > If Partially or Yes: If the data is provided with an explicit open license, please provide the name of the license, or a link to it here.
    
    * **Dataset is available free of charge.** (No, Partially, Yes)
    
    * **Data is timely and updated.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > When was the most recent update to this dataset?
    
    * **There are accessible and open official tools available to help users locate and explore individual records.** (No, Partialy , Yes)
     *Answer 'partially' if tools make it possible to get at extracts of data without having to download a full dataset. Answer 'yes' if there is an interactive tool that displays user-filtered extracts of the data to answer simple questions without downloading data at all.*
    
        > **Supporting questions** (conditional)
    
        > If Partialy  or Yes: Please provide URL
    
        > If Partialy : What are the main barriers to accessibility and usability?
    
    **Part 2: Types of land tenure**
    
    * **Datasets have information regarding indigenous people.** (No, Partially, Yes)
    
    * **The data covers land tenure involving natural persons.** (No, Partially, Yes)
     *In some cases, information on individual rights holders may be available under more restrictive licenses than general rights information. In these cases, you can indicate that data on natural persons is ‘partially’ available.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes:  Are individual owners identified in the dataset?
    
    * **The data covers land tenure involving legal persons.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes:  What information is provided to identify legal owners (e.g. company registration number, company name, address etc.)?
    
        > If Partially or Yes:  Is information provided on the beneficial ownership of land held by legal persons?
    
    * **The data covers land tenure involving state land.** (No, Partially, Yes)
    
    * **The data covers land tenure involving communal lands.** (No, Partially, Yes)
    
    * **The data covers land tenure involving open access lands.** (No, Partially, Yes)
    
    * **The data covers urban and rural tenure, and other relevant forms of tenure.** (No, Partially, Yes)
    
    * **The data covers and has information on land concessions.** (No, Partially, Yes)
    
    **Part 3: Other dataset elements**
    
    * **Each record has a geospatial reference that allows to assign features to a spatial extent.** (No, Partially, Yes)
     *The geospatial reference might be latitude-longitute coordinates, an ID to associate it to a geospatial dataset, an address, etc. "Partially" is intended for cases where a geographical reference exists, but it could have been more precise, for example, when the neighbourhood is informed, but there are no clear reasons for not to inform latitude-longitude coordinates. Will be assessed with "Yes" datasets that have the most granular geographic references that can be expected for its kind.*
    
    * **The data contains information on historical tenure (i.e. not only current records for each land parcel).** (No, Partially, Yes)
    
    * **The data contains information on land transactions and sale-values.** (No, Partially, Yes)
    
    * **The data contains gender disaggregation.** (No, Partially, Yes)
    
    * **Each tenure record contains information about the rights held over the land.** (No, Partially, Yes)
     *Freehold, lease, etc.*
    
    **Extent**
    
    * **Do the datasets available cover the tenure data of the majority of land?**
        * __The datasets available cover a small proportion of land tenure in the country__<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'> What kind of land tenure does it cover?</span></blockquote>
        * __The datasets available cover a big proportion of land tenure in the country, but not all.__<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'> What kind of land tenure does it cover?</span></blockquote>
        * __The datasets available cover all forms of land tenure in the country__<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'> What kind of land tenure does it cover?</span></blockquote>


=== "Indicator Justification"


     Land is a key element in every human civilization. The way in which societies interact with it has an impact on several spheres, from social and economic development to cultural and even religious implications. The eradication of hunger and poverty, and the sustainable use of the environment, depend in large measure on how people, communities and others gain access to land and other related assets (Food and Agriculture Organization of the United Nations, 2012). Even though data is recognized as a key asset for good land governance, collecting and publishing information about it has been a challenge for different stakeholders, due to technical, conceptual or political reasons.
     
     Land data might cover a wide range of topics, and data about them is crucial to ensure appropriate management of this key asset. Different initiatives, policy recommendations and research papers categorise land topics in different ways. Land tenure is highlighted in many of them as a fundamental aspect in understanding land dynamics.
     
     Land tenure comprises a wide range of fundamental and complex topics. LandVoc, an online Land Governance thesaurus, for example, classifies within this thematic area concepts such as land tenure systems, tenure regularizations, indigenous land rights, housing rights and land ownership. The GDB will focus on data related to different kinds of rights held by people and/or institutions over a piece of land.