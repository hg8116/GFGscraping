from bs4 import BeautifulSoup
import requests
import re

username = input("Enter Username : ")
HostURL = "https://auth.geeksforgeeks.org/user/" + username + "/practice/"
ComparerUsername = input("Enter Other Username : ")
ComparerURL = "https://auth.geeksforgeeks.org/user/" + ComparerUsername + "/practice/"

HostPage = BeautifulSoup(requests.get(HostURL).text, "lxml")
ComparerPage = BeautifulSoup(requests.get(ComparerURL).text, "lxml")

HostData = [HostPage.find_all(class_="score_card_value")[0].text,
            HostPage.find_all(class_="score_card_value")[1].text,
            HostPage.find_all(class_="rankNum")[0].text]

ComparerData = [ComparerPage.find_all(class_="score_card_value")[0].text,
                ComparerPage.find_all(class_="score_card_value")[1].text,
                ComparerPage.find_all(class_="rankNum")[0].text]


print("\nCoding Score : " + HostData[0] + "   (" + f"{int(HostData[0]) - int(ComparerData[0])}" + ")")
print("Problem Solved : " + HostData[1] + "   (" + f"{int(HostData[1]) - int(ComparerData[1])}" + ") " + "\n")


print("< < < < < < < < < Solved Composition > > > > > > > > > ")

HostProblemComposition = re.findall(r"\d+", HostPage.find_all(class_="tabs tabs-fixed-width linksTypeProblem")[0].text)
CompProblemCompostion = re.findall(r"\d+",
                                   ComparerPage.find_all(class_="tabs tabs-fixed-width linksTypeProblem")[0].text)

content = ["School", "Easy  ", "Basic ", "Medium", "Hard  "]
for index, item in enumerate(HostProblemComposition):
    print(
        content[index]
        + "  : "
        + item
        + "    ("
        + f"{int(item) - int(CompProblemCompostion[index])}"
        + ") "
    )
print("________________________________________ \n")

HostAllProblems = set([x.text for x in HostPage.find_all(class_="problemLink")])
ComparerAllProblems = set([x.text for x in ComparerPage.find_all(class_="problemLink")])

print("\n< --- Problems solved by {} but not by {} --- > \n".format(username, ComparerUsername))
for i in [x for x in HostAllProblems if x not in ComparerAllProblems]:
    print(i)

print("\n")
print("\n< --- Problems solved by {} but not by {} --- > \n".format(ComparerUsername, username))
for i in [x for x in ComparerAllProblems if x not in HostAllProblems]:
    print(i)
