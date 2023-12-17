-- blue print for the all channel tables and thier attribute
create table channelName(
    CompanyName varchar(20) not null,
    RequestData datetime not null,
    Location varchar(20) not null,
    JobPosition varchar(20) not null,
    Salary float not null,
);

insert into CompanyName(CompanyName,RequestData,Location,JobPosition,)