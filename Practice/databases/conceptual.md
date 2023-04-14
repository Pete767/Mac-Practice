### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
a SQL database management system allowing for better ease of use of SQL databases.

- What is the difference between SQL and PostgreSQL?
SQL is a database language and PostgreSQL is a system used to make navigation, creation and editing these databases easier.

- In `psql`, how do you connect to a database?
/c <name of db>

- What is the difference between `HAVING` and `WHERE`?
WHERE is more specific and HAVING will pull up an entire group

- What is the difference between an `INNER` and `OUTER` join?
inner is the overlap between two data groups and outer is everything even if there is no corresponding value on the other side

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
left will pull all values on only the left table even if there is no connection on the right, but only showing the right values that correspond to the left. The Right outer will do the same but for the right side

- What is an ORM? What do they do?
orm (object relational mapping) is a tool like SQLAlchemy which allows for interaction with relational databases

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  requests from the browser are limited in size and are made in key value pairs. server side requests can be more robust?

- What is CSRF? What is the purpose of the CSRF token?
cross site request forgery. a csrf token is given to a client by the server and used to validate that the same machine is accessing the materials as was authenticated, usually associated with a login so that others without the unique token cannot access sensitive content that requires validation.

- What is the purpose of `form.hidden_tag()`?
to hide elements that require certain permissions to view, however this only makes the hidden object invisible but still interactable unless other properties are also changed i believe.
