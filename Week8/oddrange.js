

document.getElementById("demo").innerHTML = "Paragraph changed.";
var num1=parseInt(prompt("Enter num1 :"));
var num2=parseInt(prompt("Enter num2 :"));

function oddRange(num1,num2)
{
	
	for(var i=num1;i<=num2;i++)
	{
		if(i%2!=0)
			document.write(i);

			console.log("debug1");
	}
	console.log("debug2");

	

}
oddRange(num1,num2);			
