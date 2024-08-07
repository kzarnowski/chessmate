### Running app in dev mode


1. Connect to the database.
```
psql -d chessmate
```

2. Run flask application in debug mode. Remember to specify port since it may not work on default port.
```
flask run --debug --port 3001
```