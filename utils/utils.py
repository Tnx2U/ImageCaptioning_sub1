from datetime import datetime
import pickle
import os
import matplotlib.pyplot as plt
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


	pass



# Req. 4-1	이미지와 캡션 시각화
def visualize_img_caption():
	pass