# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#Q1, 리스트 홀수만 출력
#주어진 리스트
num_list = [1,5,7,15,16,22,28,29]

#for문 활용
def get_odd_num_f(num_list):
    odd_list=[] #홀수 값을 저장할 리스트 선언
    for i in num_list: #주어진 리스트에 대해서
        if(i%2==1): #해당 값이 홀수인 경우
            odd_list.append(i) #그 값을 선언한 리스트에 저장
    return odd_list #홀수 값이 저장된 리스트 리턴


# while문 활용
def get_odd_num_w(num_list):
    k=len(num_list) #해당 리스트의 크기 저장
    i=0 # while문을 위한 변수 저장(for문의 i와 비슷한 역할)
    while(i != k): #i값이 k값과 같아지기 전까지 계속 증가함
        if(num_list[i] % 2 == 0): #리스트의 값이 짝수인 경우
            num_list.pop(i) #해당 값을 리스트에서 제거
            i-=1 #진행되는 i값을 제거(해당 값이 없어지므로 그 뒤에 있는 변수들의 인덱스가 1씩 당겨짐)
            k-=1 #인덱스가 하나 감소했기 때문에 전체 리스트의 크기도 1 감소
        else:
            i+=1 #홀수인 경우 i값을 증가시켜, while문이 끝날 수 있도록 조정(해당 리스트를 끝까지 비교할 수 있도록 1씩 증가)
            
    return num_list #수정된 리스트 리턴

print(get_odd_num_f(num_list))
print(get_odd_num_w(num_list))

# +
#Q2, 문자열 뒤집기(단어 단위)
#주어딘 문자열
sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    word = sentence.split() #문자열을 단어 단위로 끊어서 저장
    new_sentence="" #새로 출력할 문자열 선언
    for i in word[::-1]: #저장한 단어들을 역순으로 불러옴
        new_sentence+=i+" " #역순으로 불러온 단어들을 새로 선언한 문자열에 연장
    return new_sentence #새로 만든 문자열 리턴

print(reverse_sentence(sentence))

# +
#Q3, 평균 출력
# 주어진 데이터
score = [(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    for i in range(len(score)): #해당 리스트의 크기만큼 반복(튜플의 개수만큼)
        print((i+1), " 번, 평균 : ", (score[i][0]+score[i][1])/2) # 리스트 안의 튜플 값을 이중으로 불러올 수 있음
        
get_avg(score)

# +
#Q4, 딕셔너리 합치기
from collections import Counter #Counter모듈
import copy #딕셔너리 복사를 위한 모듈

#주어진 데이터
dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict_f(dict_first, dict_second): #for문을 활용한 방법
    new_dic = dict_first.copy() #copy모듈을 활용해서 첫번째 딕셔너리 복사한 새로운 딕셔너리 지정
    for i in dict_second: #두번째 딕셔너리에서
        if i not in new_dic: #해당 키가 새로 지정한 딕셔너리에 없는 경우
            new_dic[i] = dict_second[i] #해당 키값과 값을 새로 지정한 딕셔너리에 넣음
        else: #해당 키가 이미 있는 경우
            new_dic[i] += dict_second[i] #해당 키에 있는 값에서 두번째 딕셔너리의 값을 더해서 저장
            
    return new_dic

def merge_dict_C(dict_first, dict_second): #Counter 모듈 활용한 방법
    new_dic = Counter(dict_first) + Counter(dict_second) #첫번째 딕셔너리와 두번째 딕셔너리를 합친 새로운 딕셔너리 지정(같은 키를 갖은 경우 값을 더해서 저장)
    return dict(new_dic)

print(merge_dict_f(dict_first, dict_second))
print(merge_dict_C(dict_first, dict_second))

# +
#Q5, 문자열 숫자 제거
#주어진 데이터
inputs = "cat32dog16cow5"

def find_string(inputs):
    new_string = [] #단어들을 저장할 리스트 선언
    k = 0 #숫자가 있는 경우, 해당 단어의 첫 번째 글자의 인덱스 순서 저장
    if(inputs[0].isdigit()): flag = False #for문에서 단어가 시작한 경우 True로, 아닌 경우(숫자일 경우) False로 지정
    else: flag = True
    for i in range(len(inputs)): #inputs의 크기만큼 반복문 실행
        if(inputs[i].isdigit()): #해당 글자가 숫자인 경우
            if(flag == True): #앞에 글자까지 문자였을 경우(단어였을 경우) 
                new_string.append(str(inputs[k:i])) #k번째부터 해당 숫자의 이전까지의 단어를 선언한 리스트에 저장
                flag = False #숫자이므로, flag를 False로 변경
            k = i+1 #i 숫자이므로, 다음번째 순서로 k값 변경
        else: #문자인 경우(단어가 아직 다 안 끝나거나, 새로 시작하는 단어인 경우)
            flag = True # flag값을 True 값으로 유지하거나, False에서 True값으로 변경
            
    return new_string #선언한 리스트 리턴

print(find_string(inputs))
# -


