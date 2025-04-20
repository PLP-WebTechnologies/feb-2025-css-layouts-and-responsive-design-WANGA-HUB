CREATE DATABASE movies;

show databases;
use movies;
create table SERIES(
    id int primary key auto_increment,
    TITLE varchar(100) not null,
    RELEASE_YEAR int not null,
    GENRE varchar(100) not null,
    EPISODES int not null,
    RATING decimal(2,1) not null
);

show tables;
select * from SERIES;

insert into series (title, release_year, genre, episodes, rating) values ('Breaking Bad', 2008, 'Drama', 62, 9.5);

insert into series (title, release_year, genre, episodes, rating) values ('The Wire', 2002, 'Crime', 60, 9.3);
insert into series (title, release_year, genre, episodes, rating) values ('The Sopranos', 1999, 'Crime', 86, 9.2);
insert into series (title, release_year, genre, episodes, rating) values ('Game of Thrones', 2011, 'Fantasy', 73, 9.3);
select * from series;
delete from series where title = 'Game of Thrones';
select * from series;
delete * from series;
select* from series;
use movies;
select * from series;
