with films as (
    select
        film_id
        , title
        , director
        , producers[1] as first_producer
        , producers[2] as second_producer
        , producers[3] as third_producer
        , producers[4] as fourth_producer
        , release_date
    from
        {{ ref('stg_films') }}
)

select * from films
