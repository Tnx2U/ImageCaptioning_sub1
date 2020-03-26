from datetime import datetime
import pickle
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import tensorflow as tf
import config


# Req. 2-2	세팅 값 저장

def save_config():
	#입력받은 매개변수를 저장하는 config 객체를 현재 시간을 이름으로 가지는 파일에 저장하기
	current_time = datetime.now().strftime('%Y-%m-%d-%H-%M')
	config_file = {'caption_file_path' : config.args.caption_file_path, 'images_path' : config.args.images_path}

	with open(current_time+'.p','wb') as file:
		pickle.dump(config_file, file)


# Req. 4-1	이미지와 캡션 시각화
def visualize_img_caption(dataset_sampled, target_idx):
	img_path = '.\\images\\'+dataset_sampled[target_idx][0]
	comments = dataset_sampled[target_idx][1]

	title = ""
	for comment in comments:
		title += "\n" + comment

	image = img.imread(img_path)

	plt.imshow(image)
	plt.title(title)
	plt.show()

