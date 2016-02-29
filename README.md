## Components

### Message generation
Random messages are generated via a management commande (generate_activity).  This command
creates a random message for a random state, city, and user then sleeps for up to 1 second.  It
runs in an infinite while loop.  This should be running in a terminal session at any time you
want to see the data aggregations.

### REST server
The single endpoint is /stat/get and will be available via the runserver command.  The endpoint
will return an aggregation of number of cities and users for the last previous 1 minute.

### Stat display
The following command can be run in a terminal session to show the desired behavior.  It will
loop at call the REST endpoint every minute.

    while [ -e /tmp ]; do curl -s http://localhost:8000/stat/get | python -m json.tool; sleep 1m; done
