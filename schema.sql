CREATE TABLE IF NOT EXISTS 'trips' (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER
);

CREATE TABLE IF NOT EXISTS 'emails_to_invite' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    email TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'links' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    link TEXT NOT NULL,
    title TEXT NOT NULL
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);


CREATE TABLE IF NOT EXISTS 'participants' (
    id TEXT PRIMARY KEY,
    trips_id TEXT NOT NULL,
    email_to_invite_id TEXT NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trip(id),
    FOREIGN KEY (trip_id) REFERENCES emails_to_invite(id)

)

CREATE TABLE IF NOT EXISTS 'activites' (
    id TEXT PRIMARY KEY,
    trips_id TEXT NOT NULL,
    title TEXT NOT NULL,
    occurs_at DATETIME,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
)





