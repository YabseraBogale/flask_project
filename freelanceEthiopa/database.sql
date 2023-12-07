create table Software(
	id int not null primary key,
	message text not null,
	date datetime not null
);

create table Compaine(
	CompanyName varchar(30) not null,
	JobTitle varchar(30) not null,
	location varchar(30) not null,
	NumberOfRequest int not null,
	Date datetime not null,
	TechnologyStackId int not null,
);

create table TechnologyStackId(
	Name varchar(10) not null,
	Id int not null
)