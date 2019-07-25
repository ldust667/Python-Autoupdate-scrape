<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
  <meta name="description" content="Test database">
  <meta name="keywords" content="HTML,CSS,XML,JavaScript">
  <meta name="author" content="Dustin Leach">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PHP test</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>


<body>

<h1> This project is currently undergoing updates- as of 7/18/19 these prices are no longer accurate. </h1>

<?php
$user = 'waagh';
$pass = 'Norest2019';
//function to test input
function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
try{
//connecting to the database
$conn = new PDO('mysql:host=localhost;dbname=prices', $user, $pass);
//$sqlst = $conn->prepare("select count(*) from metals");
//$sqlst->execute();
//print $sqlst;
//select query for output
$sqlst = $conn->prepare("select * from models");
$sqlst->execute();
//$result = $sqlst->fetchAll();
//print($result[0][0]);
$data = $sqlst->fetchall();
//iterate 
?>
<div class="table-responsive container">
<table class="table" style="width:1%">
<thead>
<tr>
<?php foreach($data as $row):
     print "<th>" . $row['names'] . "</th>";
 endforeach ?>
</thead>
<tbody>
<tr>
<?php foreach($data as $row):
     print "<th>" . $row['price_usd'] . "</th>";
 endforeach ?>
</tr>
</tbody>
</table>

//change to block
<div id="removeSearch" style="display:none">
<input type="text" id="myInput" onkeyup="myEnterFunct()" placeholder="Search for records.." title="Type in a record">

<ul id="listRemove">
<?php foreach($data as $row):
     print "<li><a href='#'>" . $row['names'] . "</a></li>";
 endforeach ?>
</ul>
</div>

</div>

<div class="container form-group">
  <form action="" onsubmit="mySubmit()">
 <div id="addSearch">
  <label for="name">Name of metal:</label>
  <input type="text" name="name"><br>
  <label for="pricelb">Price of metal per pound:</label>
  <input type="text" name="pricelb">
 </div>
<div class="radio">
  <label><input type="radio" name="optradio" value="1" onclick="addSelected();" checked>Add a record</label>
</div>
<div class="radio">
  <label><input type="radio" name="optradio" value="2" onclick="removeSelected();">Remove a record</label>
</div>

<input type="submit" value="Submit">
</form>

</div>

<?php
//need action for form take for method
}
catch (PDOException $e) {
	//display an error message if connection fails
    print "Error!: " . $e->getMessage() . "<br/>";
    die();
}
?>



<script>
function mySubmit() {
alert("Form submitted");
//name, pricelb,add,remove
//if(document.getElementById("add").checked){
//alert("You have selected to add a record");
//}
}
function addSelected(){
alert("Your add button has been selected");
}
function removeSelected(){
alert("Your remove button has been selected");
}
function myEnterFunct() {
	//init variables
    var input, filter, ul, li, a, i, txtValue;
	//set variable for input searched in bar
    input = document.getElementById("myInput");
	//changes input to uppercase
    filter = input.value.toUpperCase();
	//set variable for list
    ul = document.getElementById("listRemove");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
</script>


</body>

</html>

