# ER Diagram

```text
+-----------------------------+
|          STUDENT            |
+-----------------------------+
| id (PK)                     |
| name                        |
| roll_no (UNIQUE)            |
| department                  |
| attendance                  |
| mathematics                 |
| dbms                        |
| python                      |
| machine_learning            |
| average_marks               |
+-----------------------------+
```

The current academic prototype uses a single normalized student record table because each submission stores one current snapshot per student.
