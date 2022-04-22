CS5293 sp22  
Project1  
Pavan Vasanth Kommineni   

I have changed the redactor.py location earlier it was in project1 sub directory along with main.py consists of main function.   

Now i have attached the main function(the main.py code)  in redactor.py and changed the location to main directory.   

Earlier for the test cases even though there is  no redacted text i'm asserting true. I removed that condition.(For the text everytime it doesn't have names,dates,genders,concept,addressphones;so i assumed in that case we should call assert true if there is no redacted text,(in the last submission))  

My python version is 3.9 in the last submission and i have updated the python version to 3.10 and updated the pipfile and pipfile.lock.  

spacy verion is changed from sm to md by listing the line in the pipfile.  
en_core_web_md = {file = "https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.2.0/en_core_web_md-3.2.0-py3-none-any.whl"}  

I have added few extra regex patterns for the dates and address.  

For the output earlier i assumed .redacted to be created in files directory.  
In the updated code; I'm checking whether directory is available or not. If not new directory will be created and the output redacted file will be created in that directory.  



