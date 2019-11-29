function changeString(wrd)
{
		var nwrd='';
		for (var i =0;i<wrd.length;i++)
		{
			if(wrd.charAt(i)>='a' &&wrd.charAt(i)<='z')
			{
				if(wrd.charAt(i)!='z')
					nwrd=nwrd+String.fromCharCode(wrd.charCodeAt(i)+1);
			
				else
					nwrd+='a';
			}
			else
				nwrd+=wrd.charAt(i);
		}
		nwrd2=''
		for(var i=0;i<nwrd.length;i++)
		{
			var c=nwrd.charAt(i);
			if(c=='a' ||c=='e'||c=='i'||c=='o'||c=='u')
				nwrd2+=c.toUpperCase();
			else
				nwrd2+=c;

		} 
		return nwrd2;
}
console.log(changeString(prompt("Enter the string")));
document.write(changeString("hello*3"));