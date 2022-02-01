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
#Q1. 시험 점수 저장 클래스 구현, 데코레이트 사용
class Score():
    # mid, final 변수 private로 지정
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final
    
    # 데코레이터를 사용하여 private 변수(mid, final) 접근
    @property
    def mid(self):
        return self.__mid
    @property
    def final(self):
        return self.__final
    
score = Score(50, 75)
print((score.mid + score.final) / 2)


# +
#Q2. 기존 클래스 상속, 새로운 클래스 구현
#기존 클래스
class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels
#새로운 클래스        
class Bike(Car):
    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels) #기존 클래스에서 fuel, wheels 변수 사용
        self.size = size #새로 추가된 변수(size) 선언

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)


# +
#Q3. CSV 파일 저장
class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path # file_path 변수 지정
        self.data_list = [] # 데이터 저장을 위한 리스트 지정

    def read_file(self):
        with open(self.file_path) as data: # 해당 파일명을 data라는 이름의 변수로 불러옴
            while(True):
                line = data.readline() # data의 한 줄을 읽어서 line으로 지정
                if not line: break # 해당 line이 비어있는 경우(더 이상 불러올 정보가 없는 경우) while문을 멈춤
                self.data_list.append(line.strip().split(',')) # 해당 line의 공백 제거 후(마지막의 줄 바꿈 제거), ","을 기준으로 split하여 리스트에 저장
        return self.data_list # 데이터들이 저장된 리스트 리턴
            
read_csv = ReadCSV("data-01-test-score.csv")
print(read_csv.read_file())


# +
#Q4. CSV 파일 읽는 함수 클래스 구현, 합계 구현 
class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path # file_path 변수 지정
        self.data_list = [] # 데이터 저장을 위한 리스트 지정
        self.merge_data_list = [] # 합쳐진 데이터 저장을 위한 리스트 지정
    #CSV파일 저장(with)
    def read_file(self):
        with open(self.file_path) as data: # 해당 파일명을 data라는 이름의 변수로 불러옴
            while(True):
                line = data.readline() # data의 한 줄을 읽어서 line으로 지정
                if not line: break # 해당 line이 비어있는 경우(더 이상 불러올 정보가 없는 경우) while문을 멈춤
                self.data_list.append(line.strip().split(',')) # 해당 line의 공백 제거 후(마지막의 줄 바꿈 제거), ","을 기준으로 split하여 리스트에 저장
        return self.data_list # 데이터들이 저장된 리스트 리턴
    
    def merge_list(self):
        for i in range(len(self.data_list)): # 클래스에서 지정한 데이터들의 저장된 리스트의 크기만큼 for문 실행
            sum_value = 0 # 각 데이터들에 대해서, 데이터의 합을 저장할 변수 지정
            for j in range(len(self.data_list[i])): # SCV 파일에 저장된 데이터들의 한 줄 크기 만큼 for문 실행
                sum_value += int(self.data_list[i][j]) #해당 데이터 값을 sum_value 값에 더함
            self.merge_data_list.append(sum_value) # 더한 값을 리스트에 저장
        return self.merge_data_list # 데이터의 합이 저장된 리스트 리턴
    
read_csv = ReadCSV("data-01-test-score.csv")
print(read_csv.read_file())
print(read_csv.merge_list())


# +
#Q5. CSV파일의 데이터 평균 구하는 함수
class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path # file_path 변수 지정
        self.data_list = [] # 데이터 저장을 위한 리스트 지정
        self.merge_data_list = [] # 합쳐진 데이터 저장을 위한 리스트 지정
    #CSV파일 저장(with)
    def read_file(self):
        with open(self.file_path) as data: # 해당 파일명을 data라는 이름의 변수로 불러옴
            while(True):
                line = data.readline() # data의 한 줄을 읽어서 line으로 지정
                if not line: break # 해당 line이 비어있는 경우(더 이상 불러올 정보가 없는 경우) while문을 멈춤
                self.data_list.append(line.strip().split(',')) # 해당 line의 공백 제거 후(마지막의 줄 바꿈 제거), ","을 기준으로 split하여 리스트에 저장
        return self.data_list # 데이터들이 저장된 리스트 리턴
    
    def merge_list(self):
        for i in range(len(self.data_list)): # 클래스에서 지정한 데이터들의 저장된 리스트의 크기만큼 for문 실행
            sum_value = 0 # 각 데이터들에 대해서, 데이터의 합을 저장할 변수 지정
            for j in range(len(self.data_list[i])): # SCV 파일에 저장된 데이터들의 한 줄 크기 만큼 for문 실행
                sum_value += int(self.data_list[i][j]) #해당 데이터 값을 sum_value 값에 더함
            self.merge_data_list.append(sum_value/len(self.data_list[i])) # 평균 값을 리스트에 저장
        self.merge_data_list.sort() # 리스트 오름차순으로 정렬
        return self.merge_data_list # 데이터의 평균이 저장된 리스트 리턴
    
read_csv = ReadCSV("data-01-test-score.csv")
read_csv.read_file()
print(read_csv.merge_list())
# -


