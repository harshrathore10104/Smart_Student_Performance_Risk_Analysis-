# System Architecture

```text
+-----------------------+
|    Streamlit UI       |
| Dashboard / Forms     |
+-----------+-----------+
            |
            v
+-----------------------+
| Application Modules   |
| CRUD | Analytics | ML |
| Reports | Validation  |
+-----+----------+------+
      |          |
      v          v
+-----------+  +----------------+
| SQLite DB |  | Scikit-learn   |
+-----------+  +----------------+
      |
      v
+-----------------------+
| PDF / Charts / Output |
+-----------------------+
```
