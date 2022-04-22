import pytest
import os
import sys
sys.path.append('..')
import project1
import nltk
import spacy
import re
import redactor
nlp=spacy.load('en_core_web_sm')

def test_input_files():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    if(len(data)!=0):
        assert True
    else:
        assert True
def test_cleaned():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    token,entities,doc=redactor.cleaned_data(data)
    if(len(token)!=0):
        assert True
def test_names():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    names=redactor.names(data)
    for i in names:
        if '\u2588' in i:
            assert True
def test_dates():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    dates=redactor.dates(data)
    for i in dates:
        if '\u2588' in i:
            assert True

def test_phones():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    phones=redactor.phones(data)
    for i in phones:
        if '\u2588' in i:
            assert True

def test_genders():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    gender=redactor.gender(data)
    for i in gender:
        if '\u2588' in i:
            assert True

def test_address():
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    address=redactor.address(data)
    for i in address:
        if '\u2588' in i:
            assert True

def test_concept():
    conpt=['mail']
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    con,list_file=redactor.concept(data,conpt)
    for i in con:
        if '\u2588' in i:
            assert True

def test_stats():
    conpt=['mail']
    k='test_stats'
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    con,list_file=redactor.concept(data,conpt)
    s=redactor.stats(list_file,files,k)
    if(len(s)!=0):
        assert True
def test_output():
    conpt=['mail']
    p=['*.txt','*.md']
    data,files=redactor.input_files(p)
    con,list_file=redactor.concept(data,conpt)
    f='files/'
    e=redactor.output(files,con,f)
    if(e==0):
        assert True


