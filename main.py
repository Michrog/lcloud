import boto3
import re

#never had experience with aws so its a bit clunky, but it did do its job on my end

#I used aws configure to set the env variables, I dont configure anything here so everything should be good

#When it comes to deleting/adding files, the prints dont 'update' for some reason.
#Meaning after you add or delete a file you have to run this script a second time and then you should see the results.

#there are 4 txt files named test, test1, test2 and test3
#you can use reges 't' or 'test' to do things for them
#I used the re library and its search() function for that

#bucket name
bucket = 'developer-task'
#bucket prefix
prefix = 'a-wing/'
#regex filter
re_filter = 't'
#add file
file_add = False
file_add_name = 'test.txt'
#delete files
file_del = False
file_del_re = 'test'


client = boto3.client('s3')
objects = client.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter='/')

#delete
if file_del:
    for file in objects['Contents']:
        if re.search(file_del_re, file['Key']):
            client.delete_object(Bucket=bucket, Key=file['Key'])

#add
if file_add:
    client.upload_file('./'+file_add_name, bucket, prefix+file_add_name)

#print filtered
print('Filtered:\n')
for file in objects['Contents']:
    if re.search(re_filter, file['Key']):
        print(file['Key'])
print('\n')

#print all
print('All:\n')
for file in objects['Contents']:
    print(file)
print('\n')