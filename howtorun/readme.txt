PostgreSQL or Postgre as it is known is an open source relational database management system(RDBMS). Currently Postgre does not support stream processing queries. Streaming data refers to data that arrives in  continuous fashion. There are many applications that has streaming data like stock market, e-commerce site, sensor readings etc. Queries on these streams can be very useful for monitoring, alerts and automated triggering of actions.


This project aims to introduce the stream processing in PostgreSQL. We have used approach similar to windowing, in which streams is broken up into windows and queries run on windows. The system will create an UNLOGGED table named \verb!tmp_table! whenever the server is started. It will serve as a temporary table for storing metadata from insert queries. Whenever the user executes an insert query, the system will automatically push the values in it into the \verb!tmp_table!
as per the format \verb!(relation_name,attribute_name, attribute_values)!. Whenever the user executes a stream aggregate query, the system will automatically calculate the aggregate from the \verb!tmp_table! and display the output. 

In the earlier system for each insert, aggregate results are calculated as it arrives. Five aggregates are calculated i.e. sum, min, max, avg and count. 
The results are stored in a temporary relation that resides in-memory. The problem earlier was that it worked on only a table named “student” with column “marks” and “id”.
We propose the following solution to this problem.

Implement stream inserts at the execution level and make the current system more generic. For any insert query, postgres will automatically update the temp table and reduce the time taken to calculate aggregation queries. 
Modify existing stream queries at the parsing level to support the above changes.

We have also documented how to modify the existing insert query at execution level.

We have modified postgres.c, heapam_handler.c files and have used functions from heaptuple.c
and printtup.c. The parsing level code is in postgres.c and the execution level changes are done
in heapam_tuple_insert() function in heapam_handler.c. We have studied the following data
structures TupleTableSlot and HeapTupleHeader. These are some of the important data structures
that we needed to study to in order to implement stream inserts at execution level. debugtup(),
RelationIdGetRelation(), CreateTupleDesc() and heap_form_tuple() are some of the important
functions that are used in our system.

Members
Nadesh Seen     - 21q050003
Pritam Sil         - 21q05r001
Saurish Darodkar     - 213050046

File Paths-
git/postgresql/src/backend/access/heap/heapam_handler.c
/git/postgresql/src/backend/tcop/postgres.c

After copying these files in their respective folders. Use make && make install to compile.

Use the following link for installation guidelines - https://www.cse.iitb.ac.in/infolab/Data/Courses/CS631/PostgreSQL-Resources/
