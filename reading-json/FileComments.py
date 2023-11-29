"""
for i in range(0,len(df["message"])):
	
	if str(df["message"][i]).find("#Software_design_and_Development")!=-1:
		table.insertIntoTable(i,df["message"][i],df["date"][i])
	elif table.checkAllWith(list_of_stack,df["message"][i])==True:
		table.insertIntoTable(i,df["message"][i],df["date"][i])
	elif table.checkAllWith(list_of_job,df["message"][i])==True:
		table.insertIntoTable(i,df["message"][i],df["date"][i])
		
	if count==100:
		count=0
		print(f"Insert up to {i}")
		sleep(3)
	else:
		count+=1

"""