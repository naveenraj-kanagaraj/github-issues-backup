import json
from github import Github
git = Github("<Your Github access token>")
org = git.get_organization('<Organisation Name>')
repo = org.get_repo('<Repository Name>')
issue = repo.get_issues()
data = []
count = 0
for i in issue:
    
    row = {
       "number" : i.number,
       "title" : i.title,
       "Description" : i.body,
       "Reported by" : i.user.login,
       "Assignee"    : str(i.assignee),
       "type"        : str(i.labels)
    }
    count = count + 1
    data.append(row)


result = json.dumps(data)

print result
print count
