CREATE TABLE completion (
   id Serial primary key,
   league varchar(200),
   created timestamp Not Null,
   about varchar(200) Not Null
);

CREATE TABLE teams (
  id Serial primary key,
  name varchar(200) not null,
  holder_t jsonb,
  about text,
  atrib jsonb not null
);

CREATE TABLE league_teams (
  id Serial primary key
  team_id  references teams(id),
  league_id  references completion(id)
);

CREATE TABLE players (
  id Serial primary key,
  name varchar(200) not null,
  atrib jsonb not null,
  rating jsonb not null,
  team_id  references teams(id),
  about text
);

CREATE TABlE finished_game (
 id Serial primary key,
 home integer references teams(id),
 away  integer references teams(id),
 payload jsonb not null,
 league_id integer references completion(id)
);


---
---
