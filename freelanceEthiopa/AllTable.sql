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
