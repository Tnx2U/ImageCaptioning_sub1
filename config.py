import argparse

# Req. 2-1	Config.py 파일 생성
parser = argparse.ArgumentParser()


# 캡션 데이터가 저장된 csv파일 경로
parser.add_argument('--caption_file_path', type=str, default='.\\datasets\\captions.csv')

# 실제 이미지 파일들이 저장된 경로
parser.add_argument('--images_path', type=str, default='.\\images')

# 설정된 변수들 객체에 저장
args = parser.parse_args()

def do_sampling():
    if args.caption_file_path:
        return true
    else:
        return false


# 참고 사이트 : https://docs.python.org/ko/3/howto/argparse.html