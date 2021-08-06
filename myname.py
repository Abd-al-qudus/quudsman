''' this script prints the name,
    gmail,slack username,the biostack of the user'''

First_Name = 'Adegite'
Last_Name = 'Adejuwon'
Gmail_Domain = 'gmail.com' 
Gmail = First_Name.lower() + Last_Name.lower() + '@' + Gmail_Domain
Slack_Username = '@A' + First_Name + ' ' + 'Genomics'
Bio_Slack = '@A_' + First_Name
Full_Name = First_Name + ' ' + Last_Name
print(Full_Name)
print(Gmail)
print(Slack_Username)
print(Bio_Slack)