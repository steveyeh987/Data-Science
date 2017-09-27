
The script is for text data parsing and data visualization with python
There are three functions in hw1.py: Parse_File, Data_Class, and Chart.

Parse_File:
	Preprocess the input link into the following format:
	
	[
		class name
		[class type]
		[male smoke percentage]
		[female smoke percentage]
		[total smoke percentage]
		[non-smoking population percentage]
	]
	
	Example for the Education class:
	
	[
		'Eduction Level'
		['elementary school and below', 'junior high', 'senior high', 'university', 'graduate school and above']
		[25.3, 49.6, 28.7, 11.7, 4.6]
		[1.7, 10.6, 6.5, 1.0, 0.0]
		[10.3, 28.4, 16.6, 6.0, 2.7]
		[0.2, 0.1, 0.3, 0.3, 0.1]
	]

Data_Class:
	Determine the data class for the first argument.
	E: stands for Education level
	A: stands for Average monthly income
	W: stands for Work environment

Chart:
	Determine the plotting method for the second argument
	l: stands for line chart
	b: stands for bar chart
	p: stands for pie chart


A simply use of the file:
	python hw1.py -(class of data)(type of chart)
	
	For example,
		python hw1.py -Ab -Wp
	First shows the bar chart of the data "Average monthly income". 
	After the user close the bar chart, it shows the pie chart of the data "Work environment".
