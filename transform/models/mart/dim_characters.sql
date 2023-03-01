with films as (
    select * from {{ ref  ('stg_films') }}
)
select title from films