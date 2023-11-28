create table Software(
	id int not null primary key,
	message text not null,
	date datetime not null
);


create table Compaines(
	NumberOfRequestMade int null,
	id int not null,
	CompanyName varchar(30) not null	
);