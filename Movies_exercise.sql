use movie;

select mov_title, mov_year from movie;

select mov_year from movie where mov_title = "American Beauty";

select * from movie where mov_year = 1999;

select * from movie where mov_year < 1998;

select movie.mov_title, reviewer.rev_name
from movie, reviewer
order by movie.mov_title, reviewer.rev_name;

select rev_name from reviewer
where rev_id in (select rev_id from rating
where rev_stars >= 7);

select mov_title from movie
where mov_id in (select mov_id from rating
where num_o_ratings is null);

select rev_name from reviewer
where rev_id in (select rev_id from rating
where rev_stars is null);

select dir_lname from director;

