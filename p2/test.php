$username = mysql_real_escape_string("victim");
$password = md5("world", true);
echo $password;