create table IF NOT EXISTS CompanyInformation(
    companyname varchar(80) not null,
    telegramchannel varchar(20) not null unique,
    title varchar(30) not null,
    date datetime not null,
    location(50) not null,
    stack json
)

create table IF NOT EXISTS MetaData(
    nameofchannel varchar(80) not null,
    sizeofdataset int not null,
    foundjob int not null,
    perectange float not null
)

insert into CompanyInformation(companyname,telegramchannel,title,date,location,stack) values(?,?,?,?,?,?)
insert into MetaData(nameofchannel,sizeofdataset,foundjob,perectange) values(?,?,?,?)
