from bs4 import BeautifulSoup
import requests
import re
import timeit

username = input("Enter Username : ")
HostURL = "https://auth.geeksforgeeks.org/user/" + username + "/practice/"
ComparerUsername = "anindiangeek"  # this can be changed or taken as argument.
ComparerURL = "https://auth.geeksforgeeks.org/user/" + ComparerUsername + "/practice/"

HostPage = BeautifulSoup(requests.get(HostURL).text, "lxml")
ComparerPage = BeautifulSoup(requests.get(ComparerURL).text, "lxml")


# Data 1 includes OverallCoding score and Problems Solved
Data1 = HostPage.find_all(
    class_="mdl-cell mdl-cell--6-col mdl-cell--12-col-phone textBold"
)

Diff_data1 = ComparerPage.find_all(
    class_="mdl-cell mdl-cell--6-col mdl-cell--12-col-phone textBold"
)

OCS, PS = re.findall(r"\d+", Data1[0].text)[0], re.findall(r"\d+", Data1[1].text)[0]
diff_OCS, diffPS = (
    re.findall(r"\d+", Diff_data1[0].text)[0],
    re.findall(r"\d+", Diff_data1[1].text)[0],
)

print("\nCoding Score : " + OCS + "   (" + f"{int(OCS)-int(diff_OCS)}" + ")")
print("Problem Solved : " + PS + "   (" + f"{int(PS)-int(diffPS)}" + ") " + "\n")

# finding the Easy hard medium levels
print("< < < < < < < < < Solved Composition > > > > > > > > > ")
Data2 = HostPage.find_all(class_="mdl-tabs__tab")
diff_Data2 = ComparerPage.find_all(class_="mdl-tabs__tab")
ProblemSets = []  # School Basic Easy Medium Hard
diff_ProblemSets = []

for i in range(5):
    ProblemSets.append((re.findall(r"\d+", Data2[i].text)[0]))
    diff_ProblemSets.append((re.findall(r"\d+", diff_Data2[i].text)[0]))

content = ["School", "Easy  ", "Basic ", "Medium", "Hard  "]
for index, item in enumerate(ProblemSets):
    print(
        content[index]
        + "  : "
        + item
        + "    ("
        + f"{int(item)-int(diff_ProblemSets[index])}"
        + ") "
    )
print("________________________________________ \n")

# list of School Problems

Data3 = HostPage.find_all(
    "li", class_="mdl-cell mdl-cell--6-col mdl-cell--12-col-phone"
)
diffData3 = ComparerPage.find_all(
    "li", class_="mdl-cell mdl-cell--6-col mdl-cell--12-col-phone"
)

# print(Data3)
questions = []
diff_questions = []

for i in Data3:
    questions.append(i.text)
for i in diffData3:
    diff_questions.append(i.text)

s = set(diff_questions)
LeftOver = [x for x in questions if x not in s]

print("< --- Left Problems --- > \n")
for i in LeftOver:
    print(i)
