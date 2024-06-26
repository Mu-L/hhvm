<?hh
/* Prototype  : mixed array_rand(array $input [, int $num_req])
 * Description: Return key/keys for random entry/entries in the array
 * Source code: ext/standard/array.c
*/

/*
* Test behaviour of array_rand() when keys of the 'input' array is heredoc string
*/
<<__EntryPoint>> function main(): void {
echo "*** Testing array_rand() : with keys of input array as heredoc strings ***\n";

// defining different heredoc strings
$empty_heredoc = <<<EOT
EOT;

$heredoc_with_newline = <<<EOT
\n
EOT;

$heredoc_with_characters = <<<EOT
first line of heredoc string
second line of heredoc string
third line of heredocstring
EOT;

$heredoc_with_newline_and_tabs = <<<EOT
hello\tworld\nhello\nworld\n
EOT;

$heredoc_with_alphanumerics = <<<EOT
hello123world456
1234hello\t1234
EOT;

$heredoc_with_embedded_nulls = <<<EOT
hello\0world\0hello
\0hello\0
EOT;

$input = dict[
  $empty_heredoc => "heredoc1",
  $heredoc_with_newline => "heredoc2",
  $heredoc_with_characters => "heredoc3",
  $heredoc_with_newline_and_tabs => "heredoc3",
  $heredoc_with_alphanumerics => "heredoc4",
  $heredoc_with_embedded_nulls => "heredoc5"
];

// Test array_rand() function with different valid 'req_num' values
echo "\n-- with default parameters --\n";
var_dump( array_rand($input) );

echo "\n-- with num_req = 1 --\n";
var_dump( array_rand($input, 1) );

echo "\n-- with num_req = 3 --\n";
var_dump( array_rand($input, 3) );

echo "\n-- with num_req = 6 --\n";
var_dump( array_rand($input, 6) );


echo "Done";
}
