<!DOCTYPE html>
<html>
<body>

<h1>The onclick Event</h1>

<button onclick="myFunction()">Click me</button>



<p id="demo"></p>

<script>
function myFunction() {
  	$.ajax({
		type: "GET",
		url: "python.py",
		success: function(msg){
		alert("success");
		}
		});
	new = "rohith";
	document.getElementById("demo").innerHTML = "ues";
}
</script>

</body>
</html>

