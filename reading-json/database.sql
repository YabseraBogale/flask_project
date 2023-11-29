create table Software(
	id int not null primary key,
	message text not null,
	date datetime not null
);


create table AllCompaines(
	NumberOfRequestMade int not null,
	CompanyName varchar(30) not null,	
);