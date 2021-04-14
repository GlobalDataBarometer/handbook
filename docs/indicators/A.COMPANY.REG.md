# Availability: Company register

The survey asks the question: To what extent is company information available as structured open data? 

{% include "feedback.md" %}


    
=== "Definitions"
    **Definitions and Identification**
    
    A national company register should contain details of companies that are incorporated within that country. For the purpose of this indicator, focus on **limited liability companies** or equivalent. 
    
    If there are multiple forms of limited liability company in this country operating under different frameworks, you should **focus your assessment on the most common domestic form**, as identified in the [World Bank's Doing Business report](https://www.doingbusiness.org/en/data/exploreeconomies/).
    
    If there are notable variations in the assessment you would make for other common forms of company, please briefly comment on this in the free text justification.
    
=== "Research Guidance"
    
    **Starting points**
    
    - **Sources:**
        - The **[Open Company Data Index](http://registries.opencorporates.com/)** contains assessments for most countries in the world, and provides links to company register web pages in the small print at the bottom of country pages. Some assessments were carried out as early as 2012, so you will need to check the current state of data availability carefully with a primary review of the register.
        - The [World Bank's Doing Business report](https://www.doingbusiness.org/en/data/exploreeconomies/) provides details of the relevant registrar in each country.
    - **Search:**
        - The company register page for details of data downloads or APIs.
    
    - **Consult:**
        - Third-parties who appear to be using bulk data from the company register to ask whether they access this from an open data source, or via some other route.
    
    **National and sub-national considerations**
    
    In some countries company registration is a **sub-national responsibility,** carried out by individual states, regions or cities.
    
    To achieve the highest scores on this indicator, it should be possible to easily access data about **all companies** in a country. This might be achieved by:
    
    - Having a central register of companies;
    - Government providing an aggregation service that brings together data from local registers; or
    - Having standardised or comparable quality data availability from every sub-national register, such that a third-party can easily aggregate data from them.
    
    To assess countries where company registration is organised sub-nationally, researchers should select the strongest examples of sub-national practice, and then indicate whether this is an outlier, or an example of widespread practice. If relevant, note in the justification any barriers that might exist preventing third-parties from aggregating data from different sub-national registers.

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
    
    * **Basic company information, including company name, legal form, status, and registered address** (No, Partially, Yes)
    
        > **Supporting questions** (conditional)
    
        > If Partially: If one or more of the basic company data features is not covered, please list which (e.g. registered address)
    
    * **The data contains details of each director** (No, Partially, Yes)
    
    * **Structured data on company accounts is available for each registered company** (No, Partially, Yes)
    
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


     See the justification for [Governance: Company registration details](https://www.notion.so/Governance-Company-registration-details-634d143946804756b7dd51ec0960ee96).