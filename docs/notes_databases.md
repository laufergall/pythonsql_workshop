# This file

These are just some basics around different ways to persist data on databases. These notes do not pretend to be exhaustive and are limited to the workshops' contents.

## A database

A database is a set of data stored in a computer.

## SQL (Structured Query Language)

A programming language used to communicate with data stored in a relational database management system.

* DML (Data Manipulation Language): `INSERT`, `SELECT`, `UPDATE`, `DELETE`.

* DDL (Data Definition Language): describe, modify, or remove. `CREATE`, `ALTER TABLE`, `DROP`, `TRUNCATE`.

* DCL (Data Control Language): `GRANT`, `REVOKE`.

* TCL (Transaction Control Language): `COMMIT`, `ROLLBACK`, `SAVEPOINT`, `SET TRANSACTION`.

## SQL vs. NoSQL Databases

* SQL: row-based table structure. Columns have a specific data type, e.g. integer.

* NoSQL: 
    * MongoDB
	* Redis
	* Cassandra
	* Apache HBase
	* [Neo4j](https://neo4j.com/). A graph database.
	
* Distributed databases: Partitioned or replicated across clusters of computers. 
    * [Hadoop](http://hadoop.apache.org/)
    * [Apache Ignite](http://ignite.apache.org/)

* Cloud Storage: 
    * [Amazon Redshift](https://aws.amazon.com/redshift/)
    * [Snowflake](https://www.snowflake.com)
	* Amazon S3
	* Azure Blob Storage
	* Google Cloud Storage

* Querying distributed datasets: 
    * [Apache Drill](http://drill.apache.org/) Querying non-relational datastores.
    * [Apache Hive](https://hive.apache.org/): Hive gives a SQL-like interface to query data stored in various databases and file systems that integrate with Hadoop.
	* [PrestoDB](https://prestosql.io/)


## RDBMS (relational database management system)

The software that allows to create, update, and administer a **relational** database. The SQL language (and its variants) are primarily used to interact with the database.

Open-source:
* [MySQL](https://www.mysql.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLite](https://www.sqlite.org/)
* [MariaDB](https://mariadb.org)

Others: 
* [Oracle DB](https://www.oracle.com/database/)
* [Microsoft SQL Server](https://www.microsoft.com/sql-server/)
* [IBM DB2](https://www.ibm.com/analytics/db2)
* [Exasol](https://www.exasol.com)
* [Vertica](https://www.vertica.com/)
* [Teradata](https://www.teradata.com/)


## SQL Clients

IDE for Databases.

Free: 
* [DBeaver](https://dbeaver.io/)
* [QueryPie](https://www.querypie.com/)
* [HeidiSQL](https://www.heidisql.com/)
* [SQLGate](https://www.sqlgate.com/)
* [SQuirreL SQL](http://squirrel-sql.sourceforge.net/)

Paid:
* [DataGrip](https://www.jetbrains.com/datagrip/)


## Database connectivity

Standard APIs which defines how a client may access a database. Establish connection, handle SQL requests and convert it into a request the DBMS can interpret.

* [ODBC]() Open Database Connectivity.
* [JDBC]() Java Database Connectivity, for connecting programs written in Java to the data in relational databases. A JDBC-to-ODBC bridge enables connections to any ODBC-accessible data source.
* [ADO.NET]()


## Data-Warehousing

* Cloud data warehouse
* OLTP vs OLAP


## References

* Christof Strauch, "NoSQL Databases", 2011. 
* https://www.codecademy.com/articles/what-is-rdbms-sql
* https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/

