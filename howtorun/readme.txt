PostgreSQL or Postgre as it is known is an open source relational database management system(RDBMS). Currently Postgre does not support stream processing queries. Streaming data refers to data that arrives in  continuous fashion. There are many applications that has streaming data like stock market, e-commerce site, sensor readings etc. Queries on these streams can be very useful for monitoring, alerts and automated triggering of actions.


This project aims to introduce the stream processing in PostgreSQL. We have used approach similar to windowing, in which streams is broken up into windows and queries run on windows. The system will create an UNLOGGED table named \verb!tmp_table! whenever the server is started. It will serve as a temporary table for storing metadata from insert queries. Whenever the user executes an insert query, the system will automatically push the values in it into the \verb!tmp_table!
as per the format \verb!(relation_name,attribute_name, attribute_values)!. Whenever the user executes a stream aggregate query, the system will automatically calculate the aggregate from the \verb!tmp_table! and display the output. 

In the earlier system for each insert, aggregate results are calculated as it arrives. Five aggregates are calculated i.e. sum, min, max, avg and count. 
The results are stored in a temporary relation that resides in-memory. 
The problem here is that this currently works on only a table named “student” with column “marks” and “id”

Members
Nadesh Seen     - 21q050003
Pritam Sil         - 21q05r001
Saurish Darodkar     - 213050046

File Paths-
git/postgresql/src/backend/access/heap/heapam_handler.c
/git/postgresql/src/backend/tcop/postgres.c

After copying these files in their respective folders. Use make && make install to compile.

Use the following link for installation guidelines - https://www.cse.iitb.ac.in/infolab/Data/Courses/CS631/PostgreSQL-Resources/
