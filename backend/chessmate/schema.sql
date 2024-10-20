DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(256) NOT NULL
);

DROP TABLE IF EXISTS tournament;

CREATE TABLE tournament (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    city VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    admin_id INT NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES users (id)
);

DROP TABLE IF EXISTS players;

CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    tournament_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (tournament_id) REFERENCES tournament (id)
    UNIQUE (user_id, tournament_id)
);

DROP TABLE IF EXISTS followers;

CREATE TABLE follower (
    following_id INT NOT NULL,
    follower_id INT NOT NULL,
    PRIMARY KEY (following_id, follower_id),
    FOREIGN KEY (following_id) REFERENCES users (id),
    FOREIGN KEY (follower_id) REFERENCES users (id),
);