# Testing Flask backend and React frontend

## Sun Aug 14 10:04:14 PM MDT 2022
- Had trouble with `npm`, had to `apt purge nodejs` and reinstall, as per
<https://github.com/nodesource/distributions/issues/1398>
- Had trouble with SQLite, SQLAlchemy and threading, applied temporary fix
  mentioned here:
  <https://stackoverflow.com/questions/34009296/using-sqlalchemy-session-from-flask-raises-sqlite-objects-created-in-a-thread-c>
- Getting errors when I try to connect frontend and backend together (running
  on different ports):

    NetworkError when attempting to fetch resource.
