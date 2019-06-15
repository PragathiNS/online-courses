### Chapter 3:

1. Intro to Query Operators

2. Comparison Operators
- Based on the field's value
$gt
$lt
$gte
$lte
$eq
$ne		not equal to	
$in		[ "v1", "v2"]
$nin	reverse of $in

Quiz:
MongoDB Enterprise Cluster0-shard-0:PRIMARY> db.movieDetails.find({writers: {$in: ["Ethan Ceon", "Joel Coen"]}}).count()
3
MongoDB Enterprise Cluster0-shard-0:PRIMARY>

3. Element Operators
- presence or absence of a given field

$exists
$type 

Quiz:
{atmosphericPressureChange: {$exists: false}}

4. Logical Operators
$or
$and -> multiple constraints on the same field. Otherwise find is and implicit
$nor
$not

MongoDB Enterprise Cluster0-shard-0:PRIMARY> db.movieDetails.find({$or: [{"tomato.meter": {$gt: 95}},
... {"metacritic": {$gt: 88}}]}, {_id: 0, title: 1, "tomato.meter": 1, metacritic: 1})
{ "title" : "Once Upon a Time in the West", "tomato" : { "meter" : 98 }, "metacritic" : 80 }
{ "title" : "Star Wars: Episode IV - A New Hope", "tomato" : { "meter" : 94 }, "metacritic" : 92 }
{ "title" : "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "tomato" : { "meter" : 99 }, "metacritic" : 96 }
{ "title" : "2001: A Space Odyssey", "tomato" : { "meter" : 96 }, "metacritic" : 86 }
{ "title" : "The Adventures of Robin Hood", "tomato" : { "meter" : 100 }, "metacritic" : 97 }
{ "title" : "The Truman Show", "tomato" : { "meter" : 94 }, "metacritic" : 90 }
{ "title" : "Quiz Show", "tomato" : { "meter" : 96 }, "metacritic" : 88 }
{ "title" : "Evil Dead II", "tomato" : { "meter" : 98 }, "metacritic" : 69 }
{ "title" : "Alien", "tomato" : { "meter" : 97 }, "metacritic" : 83 }
{ "title" : "The Kid with a Bike", "tomato" : { "meter" : 96 }, "metacritic" : 87 }
{ "title" : "Drugstore Cowboy", "tomato" : { "meter" : 100 }, "metacritic" : 82 }
{ "title" : "Raiders of the Lost Ark", "tomato" : { "meter" : 96 }, "metacritic" : 90 }
{ "title" : "Lost in Translation", "tomato" : { "meter" : 95 }, "metacritic" : 89 }
{ "title" : "Big", "tomato" : { "meter" : 97 }, "metacritic" : 72 }
{ "title" : "Groundhog Day", "tomato" : { "meter" : 96 }, "metacritic" : 72 }
{ "title" : "The Night of the Hunter", "tomato" : { "meter" : 98 }, "metacritic" : 99 }
{ "title" : "Toy Story", "tomato" : { "meter" : 100 }, "metacritic" : 92 }
{ "title" : "Toy Story 3", "tomato" : { "meter" : 99 }, "metacritic" : 92 }
{ "title" : "Toy Story 2", "tomato" : { "meter" : 100 }, "metacritic" : 88 }
{ "title" : "The Straight Story", "tomato" : { "meter" : 96 }, "metacritic" : 86 }
Type "it" for more
MongoDB Enterprise Cluster0-shard-0:PRIMARY>

Quiz:
{$or: [{"watlev": {$eq : "always dry"}}, {"depth": 0}]}

5. Array Operators: $all
Quiz:
{"sections": {$all: ["AG1", "MD1", "OA1"]}} --> 10200

6. Array Operators: $size
Quiz:
{"sections": {$size: 2}} --> 2656

7. Array Operators: $elemMatch
Quiz:


8. regex Operators



Main:

{$and : [{"results": {$size: {$in : [1, 2, 3]}}}, {$and: [{"results": {$gte: 70}}, {"results": {$lt: 80}}]}]}

