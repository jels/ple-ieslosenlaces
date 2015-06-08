# MySQL #
  * http://www.connectionstrings.com/mysql
  * http://www.mysql.com/downloads/connector/net/
  * http://www.elguille.info/colabora/puntoNET/versae_MySQLNET.htm
  * http://sourceforge.net/projects/mysqldrivercs/

  * http://dev.mysql.com/tech-resources/articles/Beginning_MYSQL_5_with_Visual_Studio.NET_2005.pdf
  * http://windows-programming.suite101.com/article.cfm/how_to_access_mysql_with_c

```
using MySql.Data.MySqlClient;
MySqlConnection myConnection = new MySqlConnection();
myConnection.ConnectionString = myConnectionString;
myConnection.Open();
//execute queries, etc
myConnection.Close();
```
## Ejemplo ##
  * Ej. C#: http://www.csharphelp.com/2006/08/opening-mysql-database-with-c/
  * Ej. C#: http://softmetal.wordpress.com/2009/03/07/conectar-mysql-con-net-tutorial-c/
  * Ej. ironpython: http://d.hatena.ne.jp/akiramei/20060129/p1