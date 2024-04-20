CQL console:
https://astra.datastax.com/org/2f2e17db-6d78-497f-84e0-ad0f3bb24a71/database/7d896cf5-bf2d-4748-a48a-ed9e6c40e934/console

create table minichat.views (
    user_id int,
    anime_id int,
    happened_at timestamp,
    primary key (user_id, anime_id, happened_at)
);

create table minichat.clicks (
    user_id int,
    anime_id int,
    happened_at timestamp,
    primary key (user_id, anime_id, happened_at)
);

select * from minichat.views;