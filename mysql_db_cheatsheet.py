
---'''

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
AirvonMatthias:masterblog_api martinawill$ pip install Flask-WTF
Collecting Flask-WTF
  Using cached flask_wtf-1.2.2-py3-none-any.whl.metadata (3.4 kB)
Requirement already satisfied: flask in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from Flask-WTF) (3.0.3)
Requirement already satisfied: itsdangerous in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from Flask-WTF) (2.2.0)
Collecting wtforms (from Flask-WTF)
  Using cached wtforms-3.2.1-py3-none-any.whl.metadata (5.3 kB)
Requirement already satisfied: Werkzeug>=3.0.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (3.0.4)
Requirement already satisfied: Jinja2>=3.1.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (3.1.4)
Requirement already satisfied: click>=8.1.3 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (8.1.7)
Requirement already satisfied: blinker>=1.6.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (1.8.2)
Requirement already satisfied: markupsafe in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from wtforms->Flask-WTF) (3.0.1)
Using cached flask_wtf-1.2.2-py3-none-any.whl (12 kB)
Using cached wtforms-3.2.1-py3-none-any.whl (152 kB)
Installing collected packages: wtforms, Flask-WTF
Successfully installed Flask-WTF-1.2.2 wtforms-3.2.1
AirvonMatthias:masterblog_api martinawill$ source low/bin/activate
(low) AirvonMatthias:masterblog_api martinawill$ pip install Flask-WTF
Requirement already satisfied: Flask-WTF in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (1.2.2)
Requirement already satisfied: flask in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from Flask-WTF) (3.0.3)
Requirement already satisfied: itsdangerous in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from Flask-WTF) (2.2.0)
Requirement already satisfied: wtforms in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from Flask-WTF) (3.2.1)
Requirement already satisfied: Werkzeug>=3.0.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (3.0.4)
Requirement already satisfied: Jinja2>=3.1.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (3.1.4)
Requirement already satisfied: click>=8.1.3 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (8.1.7)
Requirement already satisfied: blinker>=1.6.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from flask->Flask-WTF) (1.8.2)
Requirement already satisfied: markupsafe in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from wtforms->Flask-WTF) (3.0.1)
(low) AirvonMatthias:masterblog_api martinawill$ sudo mysql.server start
Password:
Starting MySQL
 SUCCESS! 
(low) AirvonMatthias:masterblog_api martinawill$ 2025-01-21T12:40:44.6NZ mysqld_safe A mysqld process already exists
mysql -u root -p
Enter password: 
charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>My Blog</title>
</head>
<body>
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        <label for="post-title">Title:</label>
        <input type="text" id="post-title" name="title" required>
        <label for="post-content">ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
Content:</label>
        <textarea id="post-conten(low) AirvonMatthias:masterblog_api martinawill$ charset="UTF-8">
bash: syntax error near unexpected token `newline'
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>My Blog</title>
</head>
<body>
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        <label for="post-title">Title:</label>
        <input type="text" id="post-title" name="title" required>
        <label for="post-content">Content:</label>
        <textarea id="post-content" name="content" required></textarea>
        <bu(low) AirvonMatthias:masterblog_api martinawill$     <meta name="viewport" content="widtdth, initial-scale=1.0">
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$     <meta name="csrf-token" content="{{ csrf_token() }}">
bash: syntax error near unexpected token `newline'
    <title>My Blog</title>
</head>
<body>
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        <label for="post-title">Title:</label>
        <input type="text" id="post-title" name="title" required>
        <label for="post-content">Content:</label>
        <textarea id="post-content" name="content" required></textarea>
        <button type="submit">Add Post</button>
    </form>

(low) AirvonMatthias:masterblog_api martinawill$     <title>My Blog</title>
bash: syntax error near unexpected token `newline'
</head>
<body>
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        <label for="post-title">Title:</label>
        <input type="text" id="post-title" name="title" required>
        <label for="post-content">Content:</label>
        <textarea id="post-content" name="content" required></textarea>
        <button type="submit">Add Post</button>
    </form>

    <!-- Container to display posts -->
    <div i(low) AirvonMatthias:masterblog_api martinawill$ </head>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$ <body>
bash: syntax error near unexpected token `newline'
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        <label for="post-title">Title:</label>
        <input type="text" id="post-title" name="title" required>
        <label for="post-content">Content:</label>
        <textarea id="post-content" name="content" required></textarea>
        <button type="submit">Add Post</button>
    </form>

    <!-- Container to display posts -->
    <div id="post-container"></div>

    <script src="main.j(low) AirvonMatthias:masterblog_api martinawill$     <h1>Welcome to My Blog</h1>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$ 
    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        <label for="post-title">Title:</label>
        <input type="text" id="post-title" name="title" required>
        <label for="post-content">Content:</label>
        <textarea id="post-content" name="content" required></textarea>
        <button type="submit">Add Post</button>
    </form>

    <!-- Container to display posts -->
    <div id="post-container"></div>

    <script src="main.js"></script>
</body>
</html>(low) AirvonMatthias:masterblog_api martinawill$     <!-- Form to add a new post -->
bash: !--: event not found
(low) AirvonMatthias:masterblog_api martinawill$     <form id="add-post-form" method="POST" action="/api/v1/posts">
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <label for="post-title">Title:</label>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <input type="text" id="post-title" name="title" required>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <label for="post-content">Content:</label>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <textarea id="post-content" name="content" required></textarea>
bash: syntax error near unexpected token `<'
(low) AirvonMatthias:masterblog_api martinawill$         <button type="submit">Add Post</button>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$     </form>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$ 
(low) AirvonMatthias:masterblog_api martinawill$     <!-- Container to display posts -->
bash: !--: event not found
(low) AirvonMatthias:masterblog_api martinawill$     <div id="post-container"></div>
bash: syntax error near unexpected token `<'
(low) AirvonMatthias:masterblog_api martinawill$ 
(low) AirvonMatthias:masterblog_api martinawill$     <script src="main.js"></script>
bash: syntax error near unexpected token `<'
(low) AirvonMatthias:masterblog_api martinawill$ </body>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$ </html>
(low) AirvonMatthias:masterblog_api martinawill$ brew services start mysql
Service `mysql` already started, use `brew services restart mysql` to restart.
(low) AirvonMatthias:masterblog_api martinawill$ brew services restart mysql
Stopping `mysql`... (might take a while)
==> Successfully stopped `mysql` (label: homebrew.mxcl.mysql)
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
(low) AirvonMatthias:masterblog_api martinawill$ mysql -u root -p
Enter password: 
charset="UTF-8">
    <meta name="viewport" contentERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
(low) AirvonMatthias:masterblog_api martinawill$ charset="UTF-8">
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$     <meta name="viewport" content="width=device-width, initial-scale=1.0">
bash: syntax error near unexpected token `newline'
    <meta name="csrf-token" content="{{ csrf_token() }}">
(low) AirvonMatthias:masterblog_api martinawill$     <meta name="csrf-token" content="{{ csrf_token() }}">
bash: syntax error near unexpected token `newline'
    <title>My Blog</title>
</head>
<body>
    <h1>(low) AirvonMatthias:masterblog_api martinawill$     <title>My Blog</title>
bash: syntax error near unexpected token `newline'
</head>
<body>
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a ne(low) AirvonMatthias:masterblog_api martinawill$ </head>
bash: syntax error near unexpected token `newline'
<body>
    <h1>Welcome to My Blog</h1>

    <!-- Form to add a new post -->
    <form id="add-post-form" method="PO(low) AirvonMatthias:masterblog_api martinawill$ <body>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$     <h1>Welcome to My Blog</h1>
bash: syntax error near unexpected token `newline'

    <!-- Form to add a new post -->
    <form id="add-post-form" method="POST" action="/api/v1/posts">
        <input type="h(low) AirvonMatthias:masterblog_api martinawill$ 
(low) AirvonMatthias:masterblog_api martinawill$     <!-- Form to add a new post -->
bash: !--: event not found
(low) AirvonMatthias:masterblog_api martinawill$     <form id="add-post-form" method="POST" action="/api/v1/posts">
bash: syntax error near unexpected token `newline'
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}(low) AirvonMatthias:masterue="{{ csrf_token() }}">      <input type="hidden" name="csrf_token" val 
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <label for="post-title">Title:</label>
bash: syntax error near unexpected token `newline'
        <input type="text" id="post-title" name="t(low) AirvonMatthias:masterblog_api martinawill$ itle" required>type="text" id="post-title" name="t 
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$         <label for="post-content">Content:</label>
bash: syntax error near unexpected token `newline'
        <textarea id="post-content" name="content" required></textarea>
        <bu(low) AirvonMatthias:masterblog_api martinawill$         <textarea id="post-content" nam required></textarea>
bash: syntax error near unexpected token `<'
(low) AirvonMatthias:masterblog_api martinawill$         <button type="submit">Add Post</button>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$     </form>
bash: syntax error near unexpected token `newline'

    <!-- Container to display posts -->
    <div i(low) AirvonMatthias:masterblog_api martinawill$ 
    <!-- Container to display posts -->
    <div id="post-container"></div>

    <script src="main.js"></script>
</body>
</html>(low) AirvonMatthias:masterblog_api martinawill$     <!-- Container to display posts -->
bash: !--: event not found
(low) AirvonMatthias:masterblog_api martinawill$     <div id="post-container"></div>
bash: syntax error near unexpected token `<'
(low) AirvonMatthias:masterblog_api martinawill$ 
(low) AirvonMatthias:masterblog_api martinawill$     <script src="main.js"></script>
bash: syntax error near unexpected token `<'
(low) AirvonMatthias:masterblog_api martinawill$ </body>
bash: syntax error near unexpected token `newline'
(low) AirvonMatthias:masterblog_api martinawill$ </html>
(low) AirvonMatthias:masterblog_api martinawill$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 9.1.0 Homebrew

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| MasterschoolMovies |
| moviewebapp        |
| myblog             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
7 rows in set (0.01 sec)

mysql> USE myblog;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> DESCRIBE myblog;
ERROR 1146 (42S02): Table 'myblog.myblog' doesn't exist
mysql> USE myblog;
Database changed
mysql> DESCRIBE myblog;
ERROR 1146 (42S02): Table 'myblog.myblog' doesn't exist
mysql> \d myblog;
mysql> \c myblog;
ERROR: 
No query specified

mysql> SHOW TABLES;
    -> \c;
    -> \c
mysql> USE myblog;
ERROR: 
USE must be followed by a database name
mysql> USE myblog;
ERROR: 
USE must be followed by a database name
mysql> SHWO DATABASES;
    -> SHOW DATABASES;
    -> \c
mysql> USE myblog;
ERROR: 
USE must be followed by a database name
mysql> DESCRIBE posts;
    -> SHOW TABLES;
    -> \c
mysql> USE myblog;
ERROR: 
USE must be followed by a database name
mysql> USE moviewebapp
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> USE myblog
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
    -> SHOW TABLES;
    -> \c
mysql> -A SHOW TABLES;
    -> -A SHOW TABLES;
    -> \c
mysql> USE myblog
Database changed
mysql> DESCRIBE posts;
    -> DESCRIBE posts;
    -> 
    -> \c
mysql> \q
Bye
(low) AirvonMatthias:masterblog_api martinawill$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 9.1.0 Homebrew

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES
    -> SHOW DATABASES;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SHOW DATABASES' at line 2
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| MasterschoolMovies |
| moviewebapp        |
| myblog             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
7 rows in set (0.05 sec)

mysql> USE myblog
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+------------------+
| Tables_in_myblog |
+------------------+
| posts            |
| users            |
+------------------+
2 rows in set (0.01 sec)

mysql> DESCRIBE posts;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int          | NO   | PRI | NULL    | auto_increment |
| title   | varchar(255) | NO   |     | NULL    |                |
| content | text         | NO   |     | NULL    |                |
| author  | varchar(255) | NO   |     | NULL    |                |
| date    | date         | NO   |     | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)

mysql> DESCRIBE users;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| username | varchar(255) | NO   | UNI | NULL    |                |
| password | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> SELECT username, password FROM users;
+-------------+--------------------------------------------------------------+
| username    | password                                                     |
+-------------+--------------------------------------------------------------+
| DON CAMILLO | $2b$12$W263zFOvKKeKI7uZr6PvXeMKKTLISSWOSSjMQApytOYKEaV1lDW2G |
+-------------+--------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> SELECT * FROM users;
+----+-------------+--------------------------------------------------------------+
| id | username    | password                                                     |
+----+-------------+--------------------------------------------------------------+
|  1 | DON CAMILLO | $2b$12$W263zFOvKKeKI7uZr6PvXeMKKTLISSWOSSjMQApytOYKEaV1lDW2G |
+----+-------------+--------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> 
'''
