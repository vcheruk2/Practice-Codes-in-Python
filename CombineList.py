"""a = [1,1,1,2,2,2,3,3,3,3,4,4,5 ]
	b= ["Sun", "is", "bright", "June","and" ,"July", "Sara", "goes", "to", "school", "Ravi","Stackoverflow","Solution"]
	
	output = ['Sun is bright', 'June and July', 'Sara goes to school', 'Ravi Stackoverflow', 'Solution']"""

result = []

def solution():
	first = 1
	ctr = 0
	a = [1,1,1,2,2,2,3,3,3,3,4,4,5 ]
	b= ["Sun", "is", "bright", "June","and" ,"July", "Sara", "goes", "to", "school", "Ravi","Stackoverflow","Solution"]

	length = len(a)
	i = 0
	temp = ""

	while(i < length ):
		
		if i == 0:
			temp = b[i]
		else:
			if i == length -1 and a[i] != a[i-1]:
				result.append(temp)
				result.append(b[i])	
			elif a[i] == a[i-1] and i != length - 1:
				temp = temp+" "+b[i]
			elif i == length - 1:
				temp = temp+" "+b[i]
				result.append(temp)
				temp = b[i]
			else:
				result.append(temp)
				temp = b[i]

		i = i + 1
	return result

print solution()
