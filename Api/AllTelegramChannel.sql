-- blue print for the all channel tables and thier attribute
create table channelName(
    CompanyName varchar(20) not null,
    RequestData datetime not null,
    Location varchar(20) not null,
    JobPosition varchar(20) not null,
    Salary float not null,
    Phone int not null,
    Email varchar(20) not null
);

insert into CompanyName(CompanyName,RequestData,Location,JobPosition,Salary,Phone,Email) values(?,?,?,?,?,?,?)



select * from channelName;

select ?,? from channelName


create table SearchTermTitle(
    title varchar(30) not null
);

create table SearchTermCompanyName(
    companyname varchar(80) not null
);


create table Location(
    location varchar(50) not null
);

insert into Location(location) value(?)

select * from Location

count (location) from Location

insert into SearchTerm(title) values(?)

insert into SearchTermCompanyName(companyname) values(?)

select title from SearchTermTitle


select companyname from SearchTermCompanyName
