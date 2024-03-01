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
$squared = 8**2;
echo "squared 8 is $squared";
echo "\n";