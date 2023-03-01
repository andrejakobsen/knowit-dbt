with characters as (
    select
        people_id as character_id
        , height
        , mass
        , hair_colors
        , gender
    from
        {{ ref('stg_people') }}
    order by 1
)
select * from characters
