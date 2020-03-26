import os
import csv
import numpy as np
import config
import pandas as pd
from sklearn.model_selection import train_test_split

# Req. 3-1	이미지 경로 및 캡션 불러오기
def get_path_caption():
    # img_path 가져올 리스트
    img_paths = []
    # comments 가져올 리스트
    captions = []
    #결과를 합칠 최종 리스트
    result = []

    csv_data = csv.reader(open(config.args.caption_file_path), delimiter="|")
    header = next(csv_data)

    prev_path = csv_data
    temp = []

    for row in csv_data:
        if len(img_paths) == 0:
            img_paths.append(row[0])
            prev_path = row[0]
            temp.append(row[2])
        else:
            if row[0] == prev_path:
                temp.append(row[2])
            else:
                prev_path = row[0]
                captions.append(temp)
                temp = []
                img_paths.append(row[0])
                temp.append(row[2])


    for i in range(0 , len(img_paths)-1):
        temp = []
        temp.append(img_paths[i])
        temp.append(captions[i])
        result.append(temp)
    return result


# Req. 3-2	전체 데이터셋을 분리해 저장하기
def dataset_split_save(dataset_path):
    train_dataset_path, val_dataset_path = train_test_split(dataset_path, test_size=0.25, random_state=None)
    return train_dataset_path, val_dataset_path


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file():
    #3-2에서 이미 구현하였으므로 패스
    pass


# Req. 3-4	데이터 샘플링
def sampling_data(sample_rate, dataset_origin):
    sample_size = (100-sample_rate)/100
    dataset_sampled, dummy = train_test_split(dataset_origin, test_size=sample_size, random_state=None)

    return dataset_sampled