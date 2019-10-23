var num1=prompt("Enter num1 :");
var num2=prompt("Enter num2 :");
function oddRange(num1,num2)
{
	for(var i=num1;i<=num2;i++)
	{
		if(i%2!=0)
			console.log(i);
			console.log("debug1");
	}
	console.log("debug2");
}
oddRange(num1,num2);			
