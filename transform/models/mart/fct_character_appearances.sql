
with characters as (
    select * from {{ ref('dim_characters') }}
),

people as (
    select * from {{ ref('stg_people') }}
),

films as (
    select * from {{ ref('dim_films') }}
),

appearances as (
    select
        film_id
        , unnest(characters) as character_url
    from
        {{ ref('stg_films') }}
),

final as (
    select
        row_number() over () as appearance_id
        , c.character_id
        , f.film_id
        , f.release_date as appearance_date
    from
        appearances as a
        left join films as f
            on a.film_id = f.film_id
        left join people as p
            on a.character_url = p.url
        left join characters as c
            on c.character_id = p.people_id
    order by
        f.release_date, c.character_id
)

select * from final
