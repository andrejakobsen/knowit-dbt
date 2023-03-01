with source as (
    select
        *
    from
        {{ source('main', 'films') }}
),

staged as (
    select
        try_cast(episode_id as tinyint) as film_id
        , title
        , director
        , str_split(producer, ', ') as producers
        , characters
        , release_date
        , url
    from
        source
)

select * from staged
