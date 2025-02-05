<?hh
/* Prototype  : bool sort ( array &$array [, int $sort_flags] )
 * Description: This function sorts an array.
                Elements will be arranged from lowest to highest when this function has completed.
 * Source code: ext/standard/array.c
*/

/*
 * testing sort() by providing different string arrays for $array argument with following flag values
 *  flag  value as defualt
 *  SORT_REGULAR - compare items normally
 *  SORT_STRING  - compare items as strings
*/
<<__EntryPoint>> function main(): void {
echo "*** Testing sort() : usage variations ***\n";

$various_arrays = vec[
  // group of escape sequences
  vec["\a", "\cx", "\e", "\f", "\n", "\r", "\t", "\xhh", "\ddd", "\v"],

  // array contains combination of capital/small letters
  vec["lemoN", "Orange", "banana", "apple", "Test", "TTTT", "ttt", "ww", "x", "X", "oraNGe", "BANANA"]
];

$flags = dict["SORT_REGULAR" => SORT_REGULAR, "SORT_STRING" => SORT_STRING];

$count = 1;
echo "\n-- Testing sort() by supplying various string arrays --\n";

// loop through to test sort() with different arrays
foreach ($various_arrays as $array) {
  echo "\n-- Iteration $count --\n";

  echo "- With Default sort flag -\n";
  $temp_array = $array;
  var_dump(usort(inout $temp_array,  HH\Lib\Legacy_FIXME\cmp<>) ); // expecting : bool(true)
  var_dump($temp_array);

  // loop through $flags array and setting all possible flag values
  foreach($flags as $key => $flag){
    echo "- Sort flag = $key -\n";
    $temp_array = $array;
    var_dump(sort(inout $temp_array, $flag) ); // expecting : bool(true)
    var_dump($temp_array);
  }
  $count++;
}

echo "Done\n";
}
