import os
import csv
import numpy as np
import config
import pandas as pd

# Req. 3-1	이미지 경로 및 캡션 불러오기
def get_path_caption():
    # img_path 가져올 리스트
    img_paths = []
    # comments 가져올 리스트
    captions = []

    csv_data = csv.reader(open(config.args.caption_file_path), delimiter="|")
    header = next(csv_data)

    idx = 0;
    prev_path = csv_data
    temp = []

    for row in csv_data:
        if len(img_paths) == 0:
            img_paths.append(row[0])
            prev_path = row[0]
            temp.append(row[2])
            #captions[0].append(row[2])
        else:
            if row[0] == prev_path:
                temp.append(row[2])
                # captions[idx].append(row[2])
            else:
                captions.append(temp)
                temp = []
                # idx += 1
                img_paths.append(row[0])
                temp.append(row[2])
                # captions[idx].append(row[2])


    for i in range(0, 100):
        print("i : ",i,"img_path :", img_paths[i],"captions : ", captions[i])
    pass


# Req. 3-2	전체 데이터셋을 분리해 저장하기
def dataset_split_save():
    pass


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file():
    pass


# Req. 3-4	데이터 샘플링
def sampling_data():
    pass