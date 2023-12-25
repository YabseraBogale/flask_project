-- blue print for the all channel tables and thier attribute
create table channelName(
    CompanyName varchar(20) not null,
    RequestData datetime not null,
    Location varchar(20) not null,
    JobPosition varchar(20) not null,
    Salary float not null,
    -- if unknown it is going to be 000000
    Phone int not null,
    -- if unknown it is going to be unknown
    Email varchar(20) not null
);
-- insertaion in table
insert into CompanyName(CompanyName,RequestData,Location,JobPosition,Salary,Phone,Email) values(?,?,?,?,?,?,?)

-- see all in table

select * from channelName;

-- see selected column from channel name

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


-- Inserting into location

insert into Location(location) value(?)


-- selecting all location

select * from Location

-- counting all location database

count (location) from Location

-- Inserting into database from table SearchTerm
insert into SearchTerm(title) values(?)
insert into SearchTermCompanyName(companyname) values(?)
-- selecting title from SearchTerm
select title from SearchTermTitle
-- selecting companyname from SearchTerm
select companyname from SearchTermCompanyName
