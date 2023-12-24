from prime import Prime
from title import JobTitle
from companyname import CompanyName

Prime().CreateTable()
app=Prime()

title=JobTitle().GiveJobTitle()
name=CompanyName().GiveCompanyName()


for i in title:
    app.InsertIntoSearchTermTitle(i)

for i in name:
    app.InsertIntoSearchTermCompanyName(i)




