<?hh
<<__EntryPoint>> function main(): void {
require_once('connect.inc');
list($host, $user, $passwd, $db) = connection_settings();
$conn = mysql_pconnect($host, $user, $passwd);
var_dump((bool)$conn);
}
