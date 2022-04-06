# cs5293sp22-project1
## Project1: Text Redaction of Sensitive data
**Author: PAVAN VASANTH KOMMMINENI**  
**Project Summary:** Whenever sensitive information is shared with the public, the data must go through a redaction process. Our Assignment in the project is to build to convert the text file data to redacted data in redacted file.
The txt file are accessed from the link attached in project description.("https://www.cs.cmu.edu/~enron/")

To run the project change the dirctory to project1 and execute the command -  
```pipenv run python main.py --input '*.txt' --names --dates --address  --phones --genders   --concept 'kid' --output 'files' --stats stdout```

**redactor.py:** In this file all the functions and modules are defined.  
**main.py:** In this file all the redactor functions are called.

Python Functions:  
1.Input files function  
2.Cleaned data function  
3.Names (Redaction) function  
4.Dates (Redaction) function  
5.Phone number (Redaction) function  
6.Gender (Redaction) function  
7.Address (Redaction) function  
8.Concept (Redaction) function  
9.Output Function  
10.Statistics Function  

The cd is cs5293sp22-Project1; I'm listing project1 for the rootpath.

Required Python Packages  

1.nltk: For the text cleaning and labels  
	word_tokenize,sent_tokenize: For the sentence tokenization, word tokenization of text  
	ne_chunk: for creation of trees  
	stopwords: It is generally used for the remove of English words which does not add much meaning to a sentence.But not used in our case  
	wordnet: For the concept, I'm using the wordnet to get the synonyms of word given  
2.spacy: For the data cleaning and redacting    
3.re: For identifying the required pattern in the text  
4.os: For the file path and folder path  
5.glob: Return all file paths that match a specific pattern(In this case .txt file)
6.argparse: take argument
  
Redactor.py Functions:  
Input_File Function:Input_function()  
1.This function extracts all required format files in the folder
2.Input is the required format.  
2.Each file data is appended to a list  
3.I'm appending the file name to another list  	
4.Returning the data list and text file name list.  
5.This method is passed when –-input is passed in command line   

Cleaned data Function:(cleaned_data(data))    
1.In this function I'm converting into doc file  
2.Word tokenizing the doc file  
3.I'm creating trees and returning the doc file,tokens and entities  
4.Instead of intializing token entities and doc every time; I'm calling this function  

Names Function:  
1.This function takes data which is returned from input_file function as input  
2.Spacy & nltk libraries have been used to identify entities "PERSON" and "ORG"  
3.There are limitations in spacy and nltk. These are not identifying non-english names.  
4.It return the data with masking names  with Unicode character ██ .  
5.This method is passed when –-names is passed in command line.  
6.I'm appending the masked names count to a global list  

Dates Function:  
1.This function takes data which is returned from names function as input  
2.Spacy & nltk libraries have been used to identify entities "DATES"  
3.There are limitations in spacy and nltk. This 'dates' is not working all the time  
4.I'm using regualar expression (re.findall). Identify the pattern in the text.  
5.It return the data with masking dates  with Unicode character ██ .  
6.This method is passed when –-dates is passed in command line.  
7.I'm appending the masked dates count to a global list  

Phones Function:  
1.This function takes data which is returned from dates function as input  
2.I'm using regualar expression. Identify the pattern in the text.  
3.There are limitations; This expreesion is not working when there are countrycode attached to the phone number(+1).   
4.It return the data with masking phone number  with Unicode character ██ .  
5.This method is passed when –-phones is passed in command line.  
6.I'm appending the masked phones count to a global list  

Gender Function:  
1.This function takes data which is returned from phones function as input  
2.I'm intializing gender related words to a list and searching the gender words in the data text.   
3.There is a limitation, gender words are vast i'm initializing very small amount when gender related word is not in the list it doesn't mask.  
4.It return the data with masking gender with Unicode character ██ .  
5.This method is passed when –-gender is passed in command line.  
6.I'm appending the masked gender count to a global list  

Address Function:  
1.This function takes data which is returned from dates function as input  
2.Spacy & nltk libraries have been used to identify entities "GPE"  
3.There are limitations in spacy and nltk. This 'GPE" is just taking the Noun not considering the numbers in the address(1123 Lindsey St; masking only lindsey)  
4.To overcome the above issue I've used regular expression. Identify the some address pattern in the text.  
5.It return the data with masking address  with Unicode character ██ .  
6.This method is passed when –-address is passed in command line.  
7.I'm appending the masked address count to a global list  

Concept Function:  
1.This function takes data which is returned from address function as input and concept word.  
2.For this concept, nltk wordnet synsets has been used to find synonyms and related words to the concept.  
3.There is a limitation with wordnet, it couldn't find the synonyms to complete extent.  
4.I'm appending the masked concept count to a global list.  
5.It return the data with masking concept sentence with Unicode character ██ and the global list.  
6.This method is passed when –-concept is passed in command line.  

Stats function:  
1.This function takes count data list and file name list.  
2.This function is used to write the redaction type and number of words redacted in each text file.  
3.This method is passed when –-stats stderr/stdout/* is passed in command line. 
4.If the input is stderr/stdout it will printout the stats and everything else will create * documnet including statistics.

Output function:  
1.This function takes data which is returned from concept function, files names list and output path.  
2.The files names are appended with .redacted.  
3.This function is used to write the output data after all the redaction steps into a corresponding .redacted file wrto .txt file in the output path.  
3.This method is passed when –-output is passed in command line.  

Main.py  
1.The execution of project starts.  
2.All input arguments are parsed in this file.The arguments below are parsed  
--input, --names, --gender, --date, --concept, --output, --stats  

Test Cases:  
To run the test-cases change the directory to tests folder and execute the command:  
pytest  

In the main_test.py i have written all the test cases:  
test_input_files:  
This method is used to test input_files functionality.It asserts true when the ken(data)!=0.If there are no files in text  

test_cleaned_data:  
This method is used to test cleaned data functionality.It asserts true when len of token!=0  

test_names:  
This method is used to test names functionality. It asserts true when there is redacted data in the text data. If there are no names in the text data; it will check len(data) if it's not equal to zero it will assert true.  

test_dates:  
This method is used to test dates functionality. It asserts true when  there is redacted data in the text data. If there are no dates in the text data; it will check len(data) if it's not equal to zero it will assert true.  

test_phones:  
This method is used to test phones functionality. It asserts true when the there is redacted data in the text data. If there are no phone-numbers in the text data; it will check len(data) if it's not equal to zero it will assert true.  

test_gender:  
This method is used to test gender functionality. It asserts true when there is redacted data in the text data. If there are no gender relavant words in the text data; it will check len(data) if it's not equal to zero it will assert true.  

test_address:  
This method is used to test address functionality. It asserts true when there is redacted data in the text data. If there are no address words in the text data; it will check len(data) if it's not equal to zero it will assert true.  

test_concept:  
This method is used to test concept functionality. It asserts true when there is redacted data in the text data. If there are no concept relavant words in the text data; it will check len(data) if it's not equal to zero it will assert true.  

test_stats:
This method is used to test stats functionality. It asserts true when the stats output len(stats) is not equal.  

tests_output:
This method is used to test output functionality. I'm returning 0 in returning function. It will assert true when the returned output is 0.  

Tree Structure:  
.
├── COLLABORATORS  
├── LICENSE  
├── Pipfile  
├── README.md  
├── project1  
│   ├── __init__.py  
│   ├── __pycache__  
│   │   ├── __init__.cpython-39.pyc  
│   │   └── redactor.cpython-39.pyc  
│   ├── files  
│   │   ├── sample.md.redacted  
│   │   ├── sample.txt.redacted   
│   │   ├── sample1.md.redacted  
│   │   └── sample1.txt.redacted  
│   ├── main.py  
│   ├── redactor.py   
│   ├── sample.md  
│   ├── sample.txt  
│   ├── sample1.md  
│   ├── sample1.txt  
│   ├── t  
│   └── tt  
├── setup.cfg  
├── setup.py  
└── tests  
    ├── __pycache__  
    │   └── main_test.cpython-39-pytest-7.0.1.pyc  
    ├── files  
    │   └── sample.txt.redacted  
    ├── main_test.py  
    ├── sample.txt  
    └── test_stats  

6 directories, 26 files  

References:  
https://www.holisticseo.digital/python-seo/nltk/wordnet  
https://stackoverflow.com/questions/11456670/regular-expression-for-address-field-validation  
https://towardsdatascience.com/custom-named-entity-recognition-using-spacy-7140ebbb3718  

Bugs:  
1.In gender, I'm facing an issue; Due to 'he' word; he in The is redacting.  
2.Address should be in specified pattern,(1123 Lindey Ave Norman OK), if not it's not redacting.  
3.There are limitations in spacy; Due to limitation some words are not redacting.   
4.The final redacted data isn't meeting the input-data format.  
5.Some times single capital letter is redacting in the word.  

