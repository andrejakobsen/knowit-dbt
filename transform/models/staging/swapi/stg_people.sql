with source as (
    select
        *
    from
        {{ source('main', 'people') }}
),

staged as (
    select
        cast(replace(url[30:], '/', '') as tinyint) as people_id
        , name
        , try_cast(height as tinyint) as height
        , try_cast(mass as tinyint) as mass
        , case
            when hair_color in ('n/a', 'none') then null
            else replace(hair_color, ', ', '/')
        end as hair_colors
        , case
            when gender in ('n/a', 'none') then null
            else gender
        end as gender
        , films
        , url
    from
        source
)

select * from staged
