import csv
import json	

class Parser:

	def main(self):
		
		csv.field_size_limit(100000000)
		f = open( 'C:\Users\asus\Desktop\POO\output.csv', 'r', encoding='utf-8' )
		reader = csv.DictReader(f)
		# Parse the CSV into JSON  
		out = json.dumps( [ row for row in reader ],ensure_ascii=False)  
		print ("JSON parsed!")
		# Save the JSON  
		f = open( 'C:\Users\asus\Desktop\POO\parsed.json', 'w')  
		f.write(out)  
		print ("JSON saved!")  

#BALTHAZARWRONG VIBRATION