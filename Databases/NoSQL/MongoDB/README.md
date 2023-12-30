1. Mongo DB pull from docker

```docker pull mongo:latest```

2. Check docker images list

```docker images```

3. Create a new folder and enter it

```mkdir mongodb-youtube-docker```

```cd mongodb-youtube-docker```

4. Run a new mongo db container

```docker run -d -p 2717:27017 -v ~/mongodb-youtube-docker:/data/db --name mymongo mongo:latest```

5. Show docker containers

```docker ps```

6. Open mongo db container bash

```docker exec -it mymongo bash```

7. Connect to mongo db

```mongosh localhost:27017```

8. Check DBs list

```show dbs;```

9. Add new record

```db.user.insertOne({"user": "Test User"})```

10. Show all records

```db.user.find()```

11. If you want to close you need write this command

```exit```
