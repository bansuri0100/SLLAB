function AgeConvert(str)
{
		var arr=str.split('-');
		var d=Number(arr[0]);
		var m=Number(arr[1]);
		var y=Number(arr[2]);

		var d=new Date();

		var cd=d.getDate();
		var cm=d.getMonth();
		var cy=d.getFullYear();

		var age=cy-y;

		if(Math.abs(cm-m<=6))
			age--;

		return age;	
}
console.log(AgeConvert(prompt("Enter dob in dd-mm-yy format")))