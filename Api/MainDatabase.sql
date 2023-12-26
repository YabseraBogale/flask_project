create table CompanyInformation(
    companyname varchar(80) not null, 
    telegramchannel varchar(20) not null unique,
    title varchar(30) not null,
    date datetime not null,
    location(50) not null,
    stack json
)

insert into CompanyInformation(companyname,telegramchannel,title,date,location,stack) values(?,?,?,?,?,?)
