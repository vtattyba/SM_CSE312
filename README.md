# SM_CSE312


Phase 3 Submission Located in Master<br>

### Running Facegram:
```

  1. python3 ./manage.py migrate
  
  2. python3 ./manage.py makemigrations
  
  3. python3 ./manage.py migrate
  
  4. python3 docker run -p 6379:6379 -d redis:5
  
  5. python3 ./manage.py runserver
  
  6. Navigate to localhost:8000


```
### Running Facegram with docker:
```

  1. docker-compose build
  
  2. docker-compose up --detach

  3. Navigate to localhost:8000
  
  NOTE : Docker uses port 8000 for the main app, 5432 for Postgres, and 6397 for redis.

```
### Phase 3 Demo: 
```
Coming 05/14/2020
```

### Phase 2 Demo:
```
https://www.youtube.com/watch?v=gyIRVaxqMIc
```


### Phase 1 Demo:
```
https://www.youtube.com/watch?v=fmAJfewY-68&t=31s
```


