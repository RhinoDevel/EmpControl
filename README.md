# EmpControl
Log your workday and tasks done.

Log your workday:

- begin and end times
- break minutes
- vacation days
- sick days

and most importantly:

- TASKS!

Each task belongs to one of your workdays and includes:

- task type (you create these types)
- client (for whom did you do the task?)
- description

Clients belong to companies, workdays belong to workers
and the user (you) is one of these workers.

Everything is stored in a PostgreSQL database.

Current implementation state:

DONE:

- DB table layout and interface
- primitive (non-productive) console UI

TO-DO:

- GUI for production
- User handling (let each worker login and handle his/her own data).
- tools to analyze/evaluate entered data (work hours per week, sick days per month, etc.)
