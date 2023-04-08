# MSA-Practice

Small project to practice MSA and Clean Architecture

## Bad Project installation

Requires python 3.10

```bash
docker run -d -p 6379:6379 redislabs/redismod
pip install fastapi "uvicorn[standard]" redis_om
uvicorn main:app --reload
```
