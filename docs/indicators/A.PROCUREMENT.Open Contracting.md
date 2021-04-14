# Availability: Public Procurement Data

The survey asks the question: To what extent is detailed structured data on public procurement processes available as open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    Governments enter into many contracts for the provision of goods, services and public works. They may publish data about these in tender lists, through contract finder websites, procurement portals, or through open data portals. 
    
    In some cases, public procurement data may be be held in a single system. At other times, different stages of the procurement process (planning, tender, award, implementation) may be held in different datasets, or a government may publish 'notices' with or without identifiers that make it possible to connect up data from different stages of the procurement process. 
    
    Look for services that aggregate data from across government - not just single departmental websites. However, if no such service is available, check a selection of the biggest government departments and note if they publish their contract data in any form.
    
=== "Research Guidance"
    
    **Starting points**
    
    - **Sources:**
        - The Open Contracting Partnership [maintains a map of cities and countries publishing procurement data](https://www.open-contracting.org/worldwide/#/) using the Open Contracting Data Standard.
        - The [Global Public Procurement Database](https://www.globalpublicprocurementdata.org/gppd/) country profiles provide links to procurement agency websites, national e-Procurement systems, and links to 'OCDS' data where available.
        - Column EB, EC, ED and EE of the [data spreadsheet](https://www.doingbusiness.org/content/dam/doingBusiness/excel/db2020/DB2020_CwG_Data.xlsx) from the [World Bank Doing Business module on Contracting with Government](https://www.doingbusiness.org/en/data/exploretopics/contracting-with-the-government#data) includes a link to where **public works contracts for roads** are posted online for each country (based on data gathered before May 2020). This can be used to check whether public works contract data is in the same portal as other tender information.
    
    - **Search:**
        - National data portals for 'Contracts' or 'Procurement' datasets
        - The website of the National Procurement Agency for open data, APIs or data exports
    
    - **Consult:**
        - Transparency experts or journalists writing about procurement: ask about known limitations of contracting data.
    
    **What to look for?**
    
    To complete the assessment for this question you will need to access and explore the available data. This may involve running queries on the dataset to check the variety of procurements included. 
    
    Look for evidence of:
    
    - **Which stages of the procurement process is data available for?** Check for details of contact awards, and implementation information (spending and performance).
    - **Goods and services contracts** - these can range from low value to high value contracts covering a wide range of supplies to government.
    - **Public works contracts** - these are often higher value contracts, involving construction work - such as building schools and hospitals, roads and other infrastructure.
    - **Procurement from a range of government departments** - does the dataset appear to contain only procurement from a single department? Or from across government?
    - **Procurement from sub-national government units** - if you find procurement for sub-national entities in the dataset, does this appear to be comprehensive, or could it just be voluntary publication by a few local government units?
    - **Bulk data access** via downloads or APIs. For example, can you export a search as XLSX and does the resulting data contain relevant data fields? Or is there documentation for an API that allows access to full data records?
    - **Persistent data -** can you find data from last year? Or the year before? Does it appear that old data is being kept archived? Or does old data expire from the platform?
    - **Is the data is structured according to an established standard**, such as the [Open Contracting Data Standard (OCDS)](https://standard.open-contracting.org/)
    
    Dashboards and other public analytic tools may help you to assess the comprehensiveness and coverage of the data. 
    
    **National and sub-national considerations**
    
    Even within federal countries, national governments will carry out significant procurement activities. In some federal systems, national government (or supranational institutions) provide portals that centralise tenders and other procurement data. 
    
    Focus on **national government** first, and then assess whether:
    
    - National datasets also include data from sub-national or local government units;
    - Equivalent data exists for a selection of sub-national or local government units, but is not nationally aggregated;
    
    If there is no evidence of procurement data being available at the national level, but there is a strong example of data availability from a sub-national government, or a specific agency, you may carry out an assessment for this data, and use the extent question to note that this only covers a very limited number of procurements.

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
    
    **Part 2: What kinds of procurement, and stages of the procurement process does the dataset cover?**
    
    * **Procurement related to goods and services is included** (No, Partially, Yes)
    
    * **Procurement related to public works is included** (No, Partially, Yes)
    
    * **The planning phase is covered** (No, Partially, Yes)
    
    * **The tender stage is covered** (No, Partially, Yes)
    
    * **The award stage is covered** (No, Partially, Yes)
    
    * **Contract implementation** (No, Partially, Yes)
     *Answer yes if you can locate any data from after contract award and signature, such as spending transactions, confirmation that goods or services were delivered, contract amendments, or data on contract performance.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: What kind of implementation data is available?
    
    * **Data on past procurements is kept** (No, Partially, Yes)
    
    **Part 3: Which fields does the dataset contain?**
    
    * **The data contains names and unique identifiers for companies awarded contracts** (No, Partially, Yes)
    
    * **The data contains start and end dates for tender processes and/or contracts** (No, Partially, Yes)
    
    * **The data contains, or can be linked to, information on spending against the contract** (No, Partially, Yes)
    
    * **The data contains a description of the goods, services or works being procured** (No, Partially, Yes)
    
    * **The data contains identifiers or other features that connect together data on each stage of a single procurement process** ()
    
    * **The data is published according to one or more relevant data standards** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Which standards are in use?
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers a very limited number of public procurements, and few other sources of data are available. <blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please briefly describe the nature of the procurements the data covers</span></blockquote>
        * The data assessed covers, or is representative of the data available for, a significant number of public procurements, but there are large gaps in coverage<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please briefly describe any notable gaps in coverage</span></blockquote>
        * The data assessed covers, or is representative of the data available for, a large proportion of public procurement, but some gaps in coverage exist.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please briefly describe any notable gaps in coverage</span></blockquote>
        * The data assessed covers, or is representative of the data available for, almost all public procurement.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please briefly describe any notable gaps in coverage</span></blockquote>


=== "Indicator Justification"


     **Open Data Barometer Indicator**
     
     This indicator has been designed for continuity with an indicator in the Open Data Barometer that looked at **details of the contracts issued by the national or federal government.**