import argparse

# Req. 2-1	Config.py 파일 생성
parser = argparse.ArgumentParser()

# 캡션 데이터가 저장된 csv파일 경로
parser.add_argument('--caption_file_path', type=str, default='.\\datasets\\captions.csv')

# 실제 이미지 파일들이 저장된 경로
parser.add_argument('--images_path', type=str, default='.\\images')

