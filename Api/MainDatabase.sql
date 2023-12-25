create table CompanyInformation(
    companyname varchar(80) not null, 
    telegramchannel varchar(20) not null unique,
    title varchar(30) not null,
    date datetime not null,
    location(50) not null,
    techstackid int not null,
    foreign key (techstackid) references TechStack(id)
)

insert into CompanyInformation(companyname,telegramchannel,title,date,location,techstackid) values(?,?,?,?,?,?)

create table SearchTermTechStack(
    id int not null primary key,
    stack json
)

insert into TechStack(id,stack) values(?,?)
