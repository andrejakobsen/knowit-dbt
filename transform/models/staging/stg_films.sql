with films as (
    select
        try_cast(episode_id as tinyint) as film_id
        , title
        , director
        , str_split(producer, ', ') as producers
        , characters
        , release_date
        , url
    from
        films
)
select * from films
