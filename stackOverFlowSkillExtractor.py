import pandas as pd
import numpy as np

df = pd.read_csv('survey_results_public.csv')

justSkills = df[["LanguageHaveWorkedWith", "LanguageWantToWorkWith", "LanguageAdmired", "DatabaseHaveWorkedWith", "DatabaseWantToWorkWith", "DatabaseAdmired", "PlatformHaveWorkedWith", "PlatformWantToWorkWith", "PlatformAdmired", "WebframeHaveWorkedWith", "WebframeWantToWorkWith", "WebframeAdmired", "EmbeddedHaveWorkedWith", "EmbeddedAdmired", "MiscTechHaveWorkedWith", "MiscTechWantToWorkWith", "MiscTechAdmired", "ToolsTechHaveWorkedWith", "ToolsTechWantToWorkWith", "ToolsTechAdmired", "NEWCollabToolsHaveWorkedWith", "NEWCollabToolsWantToWorkWith", "NEWCollabToolsAdmired", "OfficeStackAsyncHaveWorkedWith", "OfficeStackAsyncWantToWorkWith", "OfficeStackAsyncAdmired" ]]

# justSkills.to_csv("justSkills.csv")
justSkillsSets = {
    "LanguageHaveWorkedWith": {},
    "LanguageWantToWorkWith": {},
    "LanguageAdmired": {}, 
    "DatabaseHaveWorkedWith": {},
    "DatabaseWantToWorkWith": {},
    "DatabaseAdmired": {},
    "PlatformHaveWorkedWith": {},
    "PlatformWantToWorkWith": {},
    "PlatformAdmired": {},
    "WebframeHaveWorkedWith": {},
    "WebframeWantToWorkWith": {},
    "WebframeAdmired": {},
    "EmbeddedHaveWorkedWith": {},
    "EmbeddedAdmired": {},
    "MiscTechHaveWorkedWith": {},
    "MiscTechWantToWorkWith": {},
    "MiscTechAdmired": {},
    "ToolsTechHaveWorkedWith": {},
    "ToolsTechWantToWorkWith": {},
    "ToolsTechAdmired": {},
    "NEWCollabToolsHaveWorkedWith": {},
    "NEWCollabToolsWantToWorkWith": {},
    "NEWCollabToolsAdmired": {},
    "OfficeStackAsyncHaveWorkedWith": {},
    "OfficeStackAsyncWantToWorkWith": {},
    "OfficeStackAsyncAdmired": {},
}
df.drop(0, axis=0, inplace=True)

allSkillsSet = {"deleteMeLater"}
for column in justSkills:
    # print(justSkillsSets)
    # print(df[column])
    # print(len(justSkills))
    for i in range(len(justSkills)):
        # print("Index: "+ str(i))
        # print("row: "+ str(justSkills.iloc[i][column]))
        
        dataList = str(justSkills.iloc[i][column]).split(";")
        
        

        for item in dataList:
            allSkillsSet.add(item)
            
            break

        # justSkillsSets[column].update(dataList)
        
print(allSkillsSet)

# print(allSkillsSet)




