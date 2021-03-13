import os

directory1 = r'./training/labels_id'
directory2 = r'./testing/labels_id'


file1 = open('train.txt', "w")


for filename in os.listdir(directory1):
	
	if os.path.isfile("./training/images/"+filename):	
		file1.write("training/images/" + filename + ",training/labels_id/" + filename + "\n")

file1.close()

file2 = open('val.txt', "w")
for filename in os.listdir(directory2):
	if os.path.isfile("./testing/images/"+filename):
		file2.write("testing/images/" + filename + ",testing/labels_id/" + filename + "\n")

file2.close()
