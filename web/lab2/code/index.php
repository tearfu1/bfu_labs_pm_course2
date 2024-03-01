<?php
//task 1
echo "task 1";
//здесь я не стал менять snake case, так как у нас очень_плохое_грязное_имя именно так и должно выглядеть
$very_bad_unclear_name = "15 chicken wings";
$order = &$very_bad_unclear_name;
$order .= " and cola";
echo "\nYour order is: $very_bad_unclear_name.";
echo "\n";

//task 2
echo "task 2\n";

$newInt = 52;
echo $newInt;
echo "\n";

$newFloat = 3.14;
echo $newFloat;
echo "\n";

echo 15 - 3;
echo "\n";

$lastMonth = 1187.23;
$thisMonth = 1089.98;
echo $lastMonth - $thisMonth;
echo "\n";

//task 11
echo "task 11\n";

$numLanguages = 4;
$months = 11;

$days = 16 * $months;

$daysPerLanguages = $days / $numLanguages;
echo "Mag spent about $daysPerLanguages days to learn each programming language";
echo "\n";

//task 12
echo "task 12\n";
$squared = 8 ** 2;
echo "squared 8 is $squared";
echo "\n";

//task 13
echo "task 13\n";
$myNum = 49;
$answer = $myNum;
$answer += 2;
$answer *= 2;
$answer -= 2;
$answer /= 2;
$answer -= $myNum;
echo "finally answer is $answer";
echo "\n";

//task 14
echo "task 14\n";
$a = 10;
$b = 3;
$c = $a % $b;
echo "a % b is $c";
echo "\n";

if ($c == 0) {
    echo "a is divisible by b without remainder\n";
} else {
    echo "a is divisible by b with remainder: $c\n";
}

$st = pow(2, 10);
echo "2 to the 10th power is $st";
echo "\n";

$root1 = sqrt(245);
echo "square root of 245 is $root1";
echo "\n";

$array1 = [4, 2, 5, 19, 13, 0, 10];
$sum = 0;
foreach ($array1 as $item) {
    $sum += $item ** 2;
}
$root2 = sqrt($sum);
echo "square root from squared elemts sum is $root2";
echo "\n";

$root3 = sqrt(379);
$root3Num = round($root3);
$root3Ten = round($root3, 1);
$root3Thousand = round($root3, 2);
echo "to numbers $root3Num";
echo "\n";
echo "to tens $root3Ten";
echo "\n";
echo "to thousands $root3Thousand";
echo "\n";

$root4 = sqrt(587);
$root4Top = ceil($root4);
$root4Bot = floor($root4);

$array2 = ["ceil" => $root4Top, "floor" => $root4Bot];
var_dump($array2);

$array3 = [4, -2, 5, 19, -130, 0, 10];
$minim = min($array3);
echo "min from array3 is $minim";
echo "\n";

$maxim = max($array3);
echo "max from array3 is $maxim";
echo "\n";

$randNum = rand(1, 100);
echo "random num is $randNum";
echo "\n";

$array4 = [];

while (sizeof($array4) < 11) array_push($array4, rand(1, 100));
echo "array of random numbers(1-100) is ";
foreach ($array4 as $item) {
    echo "$item ";
}
echo "\n";

$a = rand(1, 100);
$b = rand(1, 100);
$abs = abs($a - $b);
echo "a: $a, b: $b module is $abs";
echo "\n";

$array5 = [1, 2, -1, -2, 3, -3];
$array6 = [];
foreach ($array5 as $item) {
    array_push($array6, abs($item));
}
echo "origin array is ";
foreach ($array5 as $item) {
    echo "$item ";
}
echo "\n";
echo "array with only positive is ";
foreach ($array6 as $item) {
    echo "$item ";
}
echo "\n";

$num = rand(1, 100);
echo "new num is $num";
echo "\n";

$array7 = [];
for ($i = 1; $i <= sqrt($num) + 1; ++$i) {
    if ($num % $i == 0) {
        array_push($array7, $i);
    }
}
for ($i = sizeof($array7) - 1; $i >= 0; --$i) {
    $temp = $num / $array7[$i];
    if (!in_array($temp, $array7)) {
        array_push($array7, $temp);
    }
}
echo "its divisors is : ";
foreach ($array7 as $item) {
    echo "$item ";
}
echo "\n";

$array8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$cnt = 0;
$temp_sum = 0;
foreach ($array8 as $item) {
    $temp_sum += $item;
    $cnt++;
    if ($temp_sum > 10) break;
}
echo "we should summarize first $cnt elements to receive sum greater than 10";
echo "\n";