-- Btree
CREATE INDEX dur_index ON “Film”(duration);
DROP INDEX if exists dur_index;

explain analyze select * from “Film” where duration  = ’2:06:00’ ;
explain analyze select * from “Film” where duration  < ’1:01:00’ ;
explain analyze select * from “Film” where duration  between ’1:30:00’  and ‘1:32:00’;
explain analyze select * from “Film” where id_film < 1000 ORDER BY duration;
explain analyze select * from “Film” where duration  = ’2:06:17.575575’ ;


--BRIN
create index dur_brin_index on “Film” using brin (duration) with(pages_per_range=128);
DROP INDEX if exists dur_brin_index;

explain analyze select count(name) from “Film” where duration = ’2:06:00’;
explain analyze select count(name) from “Film” where duration = ’2:06:00’ and duration < ’1:01:00’;
explain analyze select count(name) from “Film” where duration between ’1:30:00’  and ‘1:32:00’;
explain analyze select * from “Film” where duration >= ‘01:00:00’ and duration  < ‘01:00:00’ + interval '1 hour' / double precision '2.5';
