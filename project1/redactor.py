import nltk
import spacy
import re
import os
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk import ne_chunk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import glob


count_list = []
nlp = spacy.load('en_core_web_sm')

def input_files(txt_format):
    files=[]
    txt_format=nltk.flatten(txt_format)
    for i in txt_format:
        t=glob.glob(i)
        files.append(t)
    glob_data=[]
    myfiles=nltk.flatten(files)
    for i in myfiles:
        data = open(i,"r").read()
        data=data.replace('\n',' ')
        data=data.replace('\t',' ')
        glob_data.append(data)
    
    print(myfiles)
    return glob_data,myfiles

def cleaned_data(glob_data):
    if(len(glob_data)==0):
        raise exception
    else:
        data=glob_data
        st=str(data)
        doc = nlp(st)
        words = nltk.word_tokenize(str(doc))
        tags = nltk.pos_tag(words)
        entities = nltk.ne_chunk(tags)
        return words,entities,doc

def names(glob_data):
    if(len(glob_data)==0):
        raise error
    else:

        C_names_redacted=[]
        labels=["PERSON","ORG"]
        for list_data  in glob_data:
            names_data=[]
            token,entities,doc=cleaned_data(list_data)
            for entity in entities.subtrees():
                if (entity.label()==(labels[0]or labels[1])):
                    for leaf in entity.leaves():
                        names_data.append(leaf[0])
            if(len(names_data)==0):
                temp="The Masked Count of Names :"+ str(len(names_data))
                count_list.append(temp)
                C_names_redacted.append(list_data)
            else:
                for name in names_data:
                    redact = u"\u2588" * len(name)
                    list_data =list_data.replace(name,redact)
        
                temp="The Masked Count of Names :"+ str(len(names_data))
                count_list.append(temp)
                C_names_redacted.append(list_data)
        return C_names_redacted
         


def dates(glob_data):
    if(len(glob_data)==0):
            raise error
    
    else:
        C_dates_redacted=[]
        for list_data in glob_data:
            dates_data=[]
            token,entities,doc=cleaned_data(list_data)
            match=re.findall(r'[0-9]{2}[-|\/]{1}[0-9]{2}[-|\/]{1}[0-9]{4}',list_data)
            match1=re.findall(r'\d{1,2}[- , . / \  ' '](January?|Jan?|February?|Feb?|March?|Mar?|April?|Apr?|May?|June?|Jun?|July?|Jul?|August?|Aug?|September?|Sept?|October?|Oct?|November?|Nov?|December?|Dec?)[- , . / \ ' ']\d{4}',list_data)
            match2=re.findall(r'(January?|Jan?|February?|Feb?|March?|Mar?|April?|Apr?|May|June?|Jun?|July?|Jul?|August?|Aug?|September?|Sept?|October?|Oct?|November?|Nov?|December?|Dec?)[- , . / \ ' ']+\d{1,2}[- , . / \ ' ']+\d{4}',list_data)
                
            dates_data=match+match1+match2
            for entity in entities.subtrees():
                if entity.label()==['DATE']:
                    for k in entity.leaves():
                        dates_data.append(k[0])
            if(len(dates_data)==0):
                temp="The Masked Count of Dates :"+ str(len(dates_data))
                count_list.append(temp)
                C_dates_redacted.append(list_data)
            else:
                for number in dates_data:
                    redact = u"\u2588" * len(number)
                    list_data= list_data.replace(str(number),redact)
                temp="The Masked Count of Dates :"+ str(len(dates_data))
                count_list.append(temp)
                C_dates_redacted.append(list_data)
        return  C_dates_redacted

def phones(glob_data):
    if(len(glob_data)==0):
        raise error
    else:
        C_phones_redacted=[]
        for list_data in glob_data:
            phone_data=[]
            token,entities,doc=cleaned_data(list_data)
            match = re.findall(r'^\(?([0-9]{3})\)?[- . ● _]?([0-9]{3})[- . ● _]?([0-9]{4})$',str(doc))
            
            match1=re.findall(r'^(\+\d{1,2})?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',str(doc))
            match2=re.findall(r'((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))',str(doc))
            phne_data=match+match1+match2
            for i in phne_data:
                if(len(i)==10 or len(i)==12):
                    phone_data.append(i)
            
            if(len(phone_data)==0):
                temp="The Masked Count of Phones :"+ str(len(phone_data))
                count_list.append(temp)
                C_phones_redacted.append(list_data)
            else:
                for number in phone_data:
                    redact = u"\u2588" * len(number)
                    list_data = list_data.replace(str(number),redact)
                temp="The Masked Count of Phones :"+ str(len(phone_data))
                count_list.append(temp)
                C_phones_redacted.append(list_data)
        return C_phones_redacted

def gender(glob_data):    
    if(len(glob_data)==0):
        raise error
    else:
        C_gender_redacted=[]
        gender_label=['male','female','girl','boy',' he','his','she','him','her','man','woman','mother','father','brother','sister','aunt','uncle','sister','brother']

        for list_data in glob_data: 
            gender_data=[]
            token,entities,doc=cleaned_data(list_data)

            for i in token:
                if str(i.lower()) in gender_label:
                    gender_data.append(i)

            if(len(gender_data)==0):
                temp="The Masked Count of gender:"+str(len(gender_data))
                count_list.append(temp)
                C_gender_redacted.append(list_data)
            else:
                for gender in gender_data:
                    redact = u"\u2588" * len(gender)
                    list_data = list_data.replace(str(gender),redact)
                temp="The Masked Count of Gender :"+ str(len(gender_data))
                count_list.append(temp)
                C_gender_redacted.append(list_data)
        return C_gender_redacted

def address(glob_data):
     if(len(glob_data)==0):
        raise error

     else:
         C_address_redacted=[]
         labels=["GPE"]
         for list_data in glob_data:
             address_data=[]
             token,entities,doc=cleaned_data(list_data)
             for entity in entities.subtrees():
                if (entity.label()==(labels[0] )):
                    for k in entity.leaves():
                        address_data.append(k[0])

             match=re.findall('/^[0-9]* (.*), (.*) [a-zA-Z]{2} [0-9]{5}(-[0-9]{4})?$/',list_data)
             match3=re.findall('r\d{1,7}( \w+){1,6} (st|street|ave|avenue|ln|lane) (apt|unit|apartment)[\., ]+.*[\. ,]+(?:[A-Z][a-z.-]+[ ]?)+(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New[ ]Hampshire|New[ ]Jersey|New[ ]Mexico|New[ ]York|North[ ]Carolina|North[ ]Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode[ ]Island|South[ ]Carolina|South[ ]Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West[ ]Virginia|Wisconsin|WyomingZ|AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)[\. ,]\d{5}',list_data)
             match1=re.findall('^(\d{1,10}( \w+){1,10}( ( \w+){1,10})?( \w+){1,10}[,.](( \w+){1,10}(,)? [A-Z]{2}( [0-9]{5})?)?) $',list_data)
             match2=re.findall('^\d{1,4}( \w+){1,3},( \w+){1,3} [A-Z]{2}$',list_data)
             address_data=address_data+match+match1+match2  
             if(len(address_data)==0):
                temp="The Masked Count of Address :"+ str(len(address_data))
                count_list.append(temp)
                C_address_redacted.append(list_data)
             else:
                 for address in address_data:
                     redact = u"\u2588" * len(address)
                     list_data =str(list_data).replace(address,redact)
                 temp="The Masked Count of Address :"+ str(len(address_data))
                 count_list.append(temp)
                 C_address_redacted.append(list_data)
         return C_address_redacted


def concept(glob_data,words):
    if(len(glob_data)!=0 and len(words)!=0):
        C_concept_redacted=[]
        synonyms = []
        q=0
        for word in words:
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())

        for list_data in glob_data:
            concept_data=[]
            concept_redacted_data=[]
            token,entities,doc=cleaned_data(list_data)
            sent_token=sent_tokenize(list_data)
            for i in token:
                if str(i.lower()) in synonyms:
                    concept_data.append(i)

            if(len(concept_data)==0):
                temp="The Masked Count of Concept :"+ str(len(concept_data))
                count_list.append(temp)
                for sent in sent_token:
                    concept_redacted_data.append(sent)
                    concept_redacted_data.append(" \n ")
                reda_data=" ".join(concept_redacted_data)
                C_concept_redacted.append(reda_data)

            else:
                for sent in sent_token:
                    for con in concept_data:
                        if con in sent:
                            redact = u"\u2588" * len(sent)
                            sent=sent.replace(str(sent),redact)
                            q=q+1
                    concept_redacted_data.append(sent)
                    concept_redacted_data.append(" \n ")
                reda_data=" ".join(concept_redacted_data)
                temp="The Masked Count of Concept :"+ str(q)
                count_list.append(temp)

                C_concept_redacted.append(reda_data)
        return C_concept_redacted,count_list
    else:
        raise error

def stats(stderr_list,mylist,st):
    if(len(stderr_list)==0):
        raise error
    
    else:
        if (str(st)=='stderr') or (str(st)=='stdout'):
            for i in mylist:
                c="For The "+str(i)+" File"
                print(c)
                for k in range(0,len(stderr_list),len(mylist)):
                    print(stderr_list[k])
        else:
            path=(os.getcwd())
            c_list=[]
            for i in range(len(mylist)):
                c_list.append("For The "+mylist[i]+" File")
                for k in range(0,len(stderr_list),len(mylist)):
                    c_list.append(stderr_list[k])
            file_path =os.path.join(path,str(st))
            file = open(file_path, "w", encoding="utf-8")
            for i in range(len(c_list)):
                file.write(c_list[i])
                file.write("\n")
            file.close()
        
        return stderr_list
def output(input_files, data, output):
    path=(os.getcwd())
    list_files=[]
    for j in range(len(input_files)):
        input_files[j] = str(input_files[j])+".redacted"
    for i in range(len(input_files)):
            k=(output +'/'+ str(input_files[i]))
            filepath=os.path.join(path ,k)
            output_file = open(filepath, "w" ,encoding="utf-8")
            output_file.write(str(data[i]))
            output_file.close()

    return 0



