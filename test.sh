#!/bin/bash

# GET
curl http://127.0.0.1:5000/students

# POST
curl -X POST http://127.0.0.1:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "Anna Verdi", "age": 21, "course": "Fisica"}'

# GET
curl http://127.0.0.1:5000/students/3

# PUT
curl -X POST http://127.0.0.1:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "Anna Verdi", "age": 22, "course": "Analisi"}'

# GET
curl http://127.0.0.1:5000/students/3

# DELETE
curl -X DELETE http://127.0.0.1:5000/students/3
