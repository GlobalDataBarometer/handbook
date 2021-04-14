# Availability: Beneficial ownership 

The survey asks the question: To what extent is company beneficial ownership information available as structured open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    A beneficial ownership register should contain details of the **natural persons** who have an **ownership or control stake** in registered companies.
    
    Currently existing registers may apply to all *companies* in a jurisdiction, or only to a small sub-set, such as companies involved in the extractives industry, another regulated sector, or in receipt of public procurement contracts. 
    
=== "Research Guidance"
    
    **Starting points**
    
    - **Sources:**
        - The [OpenOwnership map](https://www.openownership.org/map/) links to a number of public registers of beneficial ownership (but is not exhaustive or always entirely up to date)
        - Global Witness reporting on EU Beneficial Ownership registers from March 2020 [includes links to a number of available registers](https://www.globalwitness.org/en/campaigns/corruption-and-money-laundering/anonymous-company-owners/5amld-patchy-progress/)
        - The [Stolen Asset Recovery Initiative resource library](https://star.worldbank.org/resources?search=beneficial%20ownership) (search for 'beneficial ownership' and filter by country) contains a series of country guides (developed in 2016/17) aimed at public authorities seeking to access company and beneficial ownership information across borders. These can provide context on the kinds of data collected, and (as of their time of publication) accessible to the public.
    - **Search:**
        - Search the website of the National Company Register or Registrar for mentioned of beneficial ownership or related terms
        - 'Beneficial ownership' + [country]
        - 'Ultimate beneficial owner' + [country]
        - Beneficiary owners + [country]
    - **Consult:**
        - Transparency campaigners
    
    **What to look for?**
    
    Look for evidence that can answer the following questions:
    
    - Are the public able to access beneficial ownership information, or is it only provided to certain parties (e.g. law enforcement)?
        - Note: in cases where a register exists but is not public, the best sources of info for this are likely to be Anti-Money Laundering (AML) industry and government announcements about relevant legislative changes.
    - Is the data from the register available? Or only a search interface?
    - Is data available in bulk? Is there an API available?
    - Does the available data cover *all* companies, or only those that registered or updated their records after a certain date?
    
    **National and sub-national considerations**
    
    Where company registration is a sub-national responsibility, beneficial ownership registers may also be maintained sub-nationally. In these cases, look for and assess the best case example of data availability, and use the extent sub-question to indicate whether this represents common practice or not. 
    
    In cases where neither national nor sub-national government maintain registers, but data is available for a particular sector (e.g. extractives), carry out your assessment for that sector, and use the extent sub-question to indicate whether this represents common practice or not.

=== "Question sub-components"

    <a class='toggle_sup_q' href='javascript:Array.from(document.querySelectorAll("blockquote")).forEach(function(el) {if (el.style.display === "none") {el.style.display = "block"; } else { el.style.display = "none";  }});'>Show/hide supporting questions</a>
    
    **Existence**
    
    * **Is this data available online in any form?**
        * Data is not available online<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)</span></blockquote>
        * Data is available, but not as a result of government action<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>If government is not providing access to data, how is this data available? </span><span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
        * Data is available from government, or because of government actions<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Please provide a URL for where this data can be found</span></blockquote>
    
    **Elements**
    
    **Part 1: Dataset specific**
    
    * **The dataset contains unique identifiers for each company** (No, Partially, Yes)
    
    * **The dataset contains identifying information for each beneficial owner** (No, Partially, Yes)
     *Answer 'Partial' if a dataset contains only names and address or nationality. Answer 'Yes' if you find inclusion of other key identifiers such as Date of Birth (at least month and year), National ID Number or other persistent identifier.*
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please list the identifying information provided. 
    
    * **The dataset contains details of the interests held by each beneficial owner** (No, Partially, Yes)
    
    * **Data includes information about individuals' sex or gender.** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please briefly describe what data includes sex or gender information.
    
    * **The data is published according to one or more relevant data standards** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Which standards are in use?
    
    **Part 2: General checklist**
    
    * **Data is provided in machine-readable format(s)** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially or Yes: Please provide a URL where this machine-readable data can be found. (Additional URLs can be included in the justification and supporting evidence)
    
        > If Partially or Yes: Please provide a comma separated list of the formats available? (E.g. csv, json)
    
        > If Partially: What prevents you from assessing this data as fully machine-readable? 
    
    * **Is this data available online in any form?** (Data is not available online, Data is available, but not as a result of government action, Data is available from government, or because of government actions)
    
        > **Supporting questions** (conditional)
    
        > If Data is not available online: Are there other offline ways to access this data in the country? (e.g. attending an office to inspect it)
    
        > If Data is available, but not as a result of government action: If government is not providing access to data, how is this data available? 
    
        > If Data is available, but not as a result of government action or Data is available from government, or because of government actions: Please provide a URL for where this data can be found
    
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
    
    **Extent**
    
    * **How comprehensive is the data assessed for this question?**
        * The data assessed covers one or more localities, but there are many other localities without available data, or with data of a lesser quality.<blockquote class='supporting_questions'><strong>Supporting questions:</strong> <span class='supporting_question'>Which locality does this data cover?</span></blockquote>
        * The data assessed covers one or more localities, and is a representative example of the kind of data that can be found for all, or most, localities.
        * The data assessed provides national coverage.


=== "Indicator Justification"


     See the justification for [Governance: Beneficial Ownership](https://www.notion.so/Governance-Beneficial-ownership-0398cd5580ce40798a0bc55960da18b2).