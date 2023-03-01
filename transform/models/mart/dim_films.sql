with films as (
    select
        film_id
        , title
        , director
        , producers[1] as first_producer
        , producers[2] as second_producer
        , producers[3] as third_producer
        , release_date
    from
        {{ ref('stg_films') }}
    order by 1
)

select * from films
