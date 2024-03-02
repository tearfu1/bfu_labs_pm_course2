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
echo "\ntask 2\n";

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
echo "\ntask 11\n";

$numLanguages = 4;
$months = 11;

$days = 16 * $months;

$daysPerLanguages = $days / $numLanguages;
echo "Mag spent about $daysPerLanguages days to learn each programming language";
echo "\n";

//task 12
echo "\ntask 12\n";
$squared = 8 ** 2;
echo "squared 8 is $squared";
echo "\n";

//task 13
echo "\ntask 13\n";
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
echo "\ntask 14\n";

#
$a = 10;
$b = 3;
$c = $a % $b;
echo "a % b is $c";
echo "\n";

#
if ($c == 0) {
    echo "a is divisible by b without remainder\n";
} else {
    echo "a is divisible by b with remainder: $c\n";
}

#
$st = pow(2, 10);
echo "2 to the 10th power is $st";
echo "\n";

#
$root1 = sqrt(245);
echo "square root of 245 is $root1";
echo "\n";

#
$array1 = [4, 2, 5, 19, 13, 0, 10];
$sum = 0;
foreach ($array1 as $item) {
    $sum += $item ** 2;
}
$root2 = sqrt($sum);
echo "square root from squared elemts sum is $root2";
echo "\n";

#
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

#
$root4 = sqrt(587);
$root4Top = ceil($root4);
$root4Bot = floor($root4);

$array2 = ["ceil" => $root4Top, "floor" => $root4Bot];
var_dump($array2);

#
$array3 = [4, -2, 5, 19, -130, 0, 10];
$minim = min($array3);
echo "min from array3 is $minim";
echo "\n";

$maxim = max($array3);
echo "max from array3 is $maxim";
echo "\n";

#
$randNum = rand(1, 100);
echo "random num is $randNum";
echo "\n";

#
$array4 = [];

while (sizeof($array4) < 11) array_push($array4, rand(1, 100));
echo "array of random numbers(1-100) is ";
foreach ($array4 as $item) {
    echo "$item ";
}
echo "\n";

#
$a = rand(1, 100);
$b = rand(1, 100);
$abs = abs($a - $b);
echo "a: $a, b: $b module is $abs";
echo "\n";

#
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

#
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

#
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

//task 15
echo "\ntask 15\n";

#
function printStringReturnNumber(): int
{
    $num = rand(1, 100);
    echo "i'm random string from printStringReturnNumber function, also i return random number(1-100), not it's: $num";
    echo "\n";
    return $num;
}

#
$myNum = printStringReturnNumber();

#
echo "myNum is $myNum";
echo "\n";

//task 16
echo "\ntask 16\n";

#
function increaseEnthusiasm(string $str)
{
    return $str . "!";
}

echo increaseEnthusiasm("im fine") . "\n";

#
function repeatThreeTimes(string $str)
{
    return $str . $str . $str;
}

echo repeatThreeTimes("is it echo?") . "\n";

#
echo increaseEnthusiasm(repeatThreeTimes("its absolutely echo")) . "\n";

#
function cut(string $str, int $num = 10): string
{
    return substr($str, 0, $num);
}

$newStr = "hello im here to talk about something";
echo "cut function: " . cut($newStr, 20) . "\n";

#
function arrayOutput(array $arr)
{
    if (sizeof($arr) == 0) {
        echo "\n";
        return 0;
    }
    echo $arr[0] . " ";
    array_splice($arr, 0, 1);
    return arrayOutput($arr);
}

echo "recursive output: ";
arrayOutput([1, 2, 3]);

$newNum = rand(100, 1000);

#
function numSumDecreaser(int $num)
{
    $sum = 0;
    while ($num > 0) {
        $sum += $num % 10;
        $num = floor($num / 10);
    }
    if ($sum > 9) {
        return numSumDecreaser($sum);
    }
    return $sum;
}

echo "New num is $newNum, if we put it in our function: " . numSumDecreaser($newNum);
echo "\n";

//task 17
echo "\ntask 17\n";

#1
$array9 = [];

for ($i = 1; $i < 10; ++$i) {
    $tempStr = "";
    for ($j = 0; $j < $i; ++$j) {
        $tempStr .= "x";
    }
    array_push($array9, $tempStr);
}
echo "'x' array: ";
foreach ($array9 as $item) {
    echo "$item ";
}
echo "\n";

#2
function arrayFill(string $elem, int $num): array
{
    $newArray = [];
    while (sizeof($newArray) < $num) {
        array_push($newArray, $elem);
    }
    return $newArray;
}

echo "arrayFill func result: ";
$array10 = arrayFill('x', 5);
foreach ($array10 as $item) {
    echo "$item ";
}
echo "\n";

#3
$array11 = [[1, 2, 3], [4, 5], [6]];
echo "2-D array is ";
foreach ($array11 as $item) {
    foreach ($item as $value) {
        echo "$value ";
    }
}
echo "\n";
$newSum = 0;
foreach ($array11 as $item1) {
    foreach ($item1 as $item2) {
        $newSum += $item2;
    }
}
echo "Sum of 2-dimensional array is : " . $newSum . "\n";

#4
echo "2-D array creation: ";
$array12 = [];
$firstDim = 3;
$secondDim = 3;
$cnt = 1;
for ($i = 0; $i < $firstDim; ++$i) {
    $tempArray = [];
    array_push($array12, $tempArray);
    for ($j = 0; $j < $secondDim; ++$j) {
        array_push($array12[$i], $cnt);
        $cnt++;
    }
}
foreach ($array12 as $item) {
    foreach ($item as $value) {
        echo "$value ";
    }
}
echo "\n";

#5
$array13 = [2, 5, 3, 9];
$result = $array13[0] * $array13[1] + $array13[2] * $array13[3];
echo "result is $result" . "\n";

#6
$user = ['name' => "Maxim", 'surname' => "Vayda", 'patronymic' => "Valentinovich"];
echo "surname is: " . $user['surname'] . ", name is: " . $user['name'] . ", patronymic is: " . $user['patronymic'] . "\n";

#7
$date = ['year' => "2024", 'month' => "march", 'day' => "1"];
echo $date['year'] . "-" . $date['month'] . "-" . $date['day'] . "\n";

#8
$arr = ['a', 'b', 'c', 'd', 'e'];
$size = sizeof($arr);
echo "size of arr: $size" . "\n";
$lastElemIndex = $size - 1;
$predLastElemIndex = $size - 2;
echo "last elem: $arr[$lastElemIndex]" . "\n";
echo "pred last elem: $arr[$predLastElemIndex]" . "\n";

//task 18
echo "\ntask18\n";

#
function greaterThanTen(int $a, int $b): bool
{
    return ($a + $b) > 10;
}

echo "greaterThanTen function result: ";
if (greaterThanTen(10, 10)) {
    echo "true" . "\n";
} else {
    echo "false" . "\n";
}

#
function isEqual(float $a, float $b): bool
{
    return $a == $b;
}

echo "isEqual function result: ";
if (isEqual(10, 10)) {
    echo "true" . "\n";
} else {
    echo "false" . "\n";
}

#
$test = 0;
if (!$test) echo "верно" . "\n";

#
$age = rand(1, 200);
echo "age is $age" . "\n";
if ($age < 10 || $age > 99) {
    echo "age is less than ten, or greater than 99: $age" . "\n";
} else {
    echo "age is between 10 and 99" . "\n";
    $sum = 0;
    while ($age > 0) {
        $sum += $age % 10;
        $age = floor($age / 10);
    }
    if ($sum <= 9) {
        echo "sum of digits of this age is unambiguous: $sum" . "\n";
    } else {
        echo "the sum of the digits of this number is two digits: $sum" . "\n";
    }
}

#
$arr = [1, 2, 3];
if (sizeof($arr) == 3) {
    $sum = 0;
    foreach ($arr as $value) $sum += $value;
    echo "size of array is 3 and sum of its numbers is: $sum" . "\n";
}

//task 19
echo "\ntask19 \n";
for ($i = 1; $i <= 20; ++$i) {
    for ($j = 0; $j < $i; ++$j) {
        echo "x";
    }
    echo "\n";
}

//task 20
echo "\ntask20 \n";

#
$array14 = [1, 10, 15, 11, 63, 16, 45, 35];
$mean = array_sum($array14) / sizeof($array14);
echo "mean of array is $mean" . "\n";

#
$sumThousand = array_sum(range(1, 100));
echo "sum 1 to 100 is $sumThousand" . "\n";

#
$array15 = [16, 144, 400];
$array16 = array_map('sqrt', $array15);

echo "origin array is: ";
foreach ($array15 as $value) echo "$value ";
echo "\n";
echo "square rooted array is: ";
foreach ($array16 as $value) echo "$value ";
echo "\n";

#
$array17 = array_combine(range('a', 'z'), range(1, 26));
echo "a-z and 1-26 array: ";
var_dump($array17);

#
$str = "1234567890";
$array18 = str_split($str, 2);
$sum = array_sum($array18);
echo "sum by pairs: $sum" . "\n";