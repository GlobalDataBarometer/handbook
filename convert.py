import notiontomarkdown
import os
import csv
from notion.client import NotionClient
import requests
import getpass
import io
import zipfile

## First login
email = 'scripts@globaldatabarometer.org' #@param {type:"string"}
password = os.environ.get('NOTION_PW')

s = requests.Session()
s.get("https://www.notion.so/login")

r = s.post('https://www.notion.so/api/v3/loginWithEmail', json = {'email':email,'password': password})
client = NotionClient(token_v2=r.cookies['token_v2'])
token = r.cookies['token_v2']

## Then get the pages we need

indicators = "https://www.notion.so/globaldatabarometer/6e263c9b092e444dad1c07c14f378fee?v=b037cc86a90a4c29b62bf5f2807e6776"
cvi = client.get_collection_view(indicators)

themes = "https://www.notion.so/globaldatabarometer/2f0962aa3430451ea645fcb830fdb0c1?v=65ff9b6d4bd34f9785ead2c1bac84cba"
cvt = client.get_collection_view(themes)


rows = []

for indicator in cvi.collection.get_rows():
    print(indicator)
    if indicator.component is None:
        component = "X"
    else:
        component = indicator.component[0]
    
    try:
        theme = str(indicator.theme[0].title).upper().split(" ")[0]
    except IndexError:
        theme = "GENERAL"

    question_id = "{}.{}.{}".format(component,theme,indicator.shortname)

    # Create a handbook page for this indicator
    cookies = {
        'token_v2': token,
    }
    markdownurl = notiontomarkdown.get_exported_url(indicator.id,cookies)
    page = requests.get(markdownurl)
    with zipfile.ZipFile(io.BytesIO(page.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                if ".md" in zipinfo.filename:
                    with open('docs/{}.md'.format(question_id),"wb") as docfile:
                        docfile.write(thefile.read())

    # Create the survey definition for this indicator 
    # NOTE: For now we use the theme as the section. This will change later
    if indicator.question:
        q = {}  # q = a new row in the questions sheet
        q['Section ID'] = theme
        q['Question ID'] = question_id
        q['Question'] = indicator.question
        q['Type'] = "Sum"
        q['SubQuestionsFirst'] = "Yes"
        q['WantJustification'] = "Yes"
        q['WantExamples'] = "Yes"
        q['HelpLink'] = "https://github.com/GlobalDataBarometer/handbook/blob/master/docs/{}.md".format(question_id)

        rows.append(q)

        q = {}
        q['Section ID'] = theme
        q['Question ID'] = "{}.a1".format(question_id)
        q['Question'] = indicator.existence_question
        q['Type'] = "Radio"
        q['Parent ID'] = question_id
        q['CSSClass'] = 'radio-list'
        options = []
        for opt in indicator.existence_options:
            options = options + opt.split(";")
        for n, option in enumerate(options):
            q['Option'+str(n)] = option
        
        rows.append(q)

        for n, element in enumerate(indicator.elements):
            if(element):
                q = {}
                q['Section ID'] = theme
                q['Question ID'] = "{}.b{}".format(question_id,n)
                q['Question'] = element.title
                q['Type'] = "Option"
                q['Parent ID'] = question_id
                if(element.get('option0')):
                    for i in range(5):
                        q['Option'+str(i)] = element.get('option'+str(i))
                else:
                    q['Multiplier'] = "0.5"
                    q['Option0'] = "No"
                    q['Option1'] = "Partially"
                    q['Option2'] = "Yes"

                for i in range(5):
                    q['Supporting'+str(i)] = element.get('supporting'+str(i))

                rows.append(q)
    
        for n, extent in enumerate(indicator.extent):
            if(extent):
                q = {}
                q['Section ID'] = theme
                q['Question ID'] = "{}.c1".format(question_id)
                q['Question'] = extent.title
                q['Type'] = "Radio"
                q['CSSClass'] = 'radio-list'
                q['Parent ID'] = question_id
                
                for i in range(5):
                    q['Option'+str(i)] = extent.get('option'+str(i))
            
                for i in range(5):
                    q['Supporting'+str(i)] = extent.get('supporting'+str(i))

                rows.append(q)

print(rows)

csvfile = open('survey/questions.csv','w')
fields = ["Section ID", "QuestionNumber", "Question ID", "Question", "Type", "Parent ID", "SubQuestionsFirst", "CSSClass", "Guidance10", "Guidance5", "Guidance0", "WantConfidence", "WantJustification", "JustificationNote", "HasPrivateNotes",
          "WantExamples", "Multiplier", "Option0", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7", "Option8", "Option9", "Supporting0", "Supporting1", "Supporting2", "Supporting3", "Supporting4", "Supporting5", "HelpLink"]
        
obj = csv.DictWriter(csvfile, fieldnames=fields)
obj.writeheader()
obj.writerows(rows)
