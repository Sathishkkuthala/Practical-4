fh = open("prac 4.txt",'w')
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers) 
fh.write("Average:"+  str(average))
fh.close()
