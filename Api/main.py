from pprint import pprint
from prime import Prime
from title import JobTitle
from companyname import CompanyName

app=Prime()

title=app.AllGetTitle()
name=app.AllGetCompanyName()

for i in range(0,10):
    pprint(name[i])




