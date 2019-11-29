function letterSurround(wrd)
{
		var equal=0;var plus=0;flag=true;
			
		for (var i=0;i<wrd.length;i++)
		{
				var c=wrd.charAt(i);
				if(wrd.charAt(0)>='a'&&wrd.charAt(0)<='z')
				{
					return false;
				}	
				else if(c=='=')
				{
						equal++;
						continue;
				}
				else if(c=='+')
				{
						plus++;
						continue;
				}
				else if(c>='a'&& c<='z')
				{
						if(c.charAt(i-1)=='+' &&c.charAt(i+1)=='+')
							continue;
						else
						{
							return false;
						}
				}	
		}
		return(flag)
}
console.log(letterSurround(prompt("Enter the string:")))