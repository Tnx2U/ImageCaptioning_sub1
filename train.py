import config
from data import preprocess 
from utils import utils


# config 저장
utils.save_config()


# 3-1 이미지 경로 및 캡션 불러오기
dataset_path = preprocess.get_path_caption()

# 3-2 전체 데이터셋을 분리해 저장하기
train_dataset_path, val_dataset_path = preprocess.dataset_split_save(dataset_path)


# 3-3 저장된 데이터셋 불러오기
# 3-2 에서 데이터를 가져왔으므로 스킵
# img_paths, caption = preprocess.get_data_file()


# 3-4 데이터 샘플링
sample_rate = 70 # %단위로 입력
dataset_origin = train_dataset_path;
if config.do_sampling:
    dataset_sampled = preprocess.sampling_data(sample_rate, dataset_origin)


# 4-1 이미지와 캡션 시각화 하기
target_idx = 1
utils.visualize_img_caption(dataset_sampled, target_idx)
