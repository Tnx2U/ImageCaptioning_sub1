# 인공지능 프로젝트

### 환경설정

### 기존 코드(linear_regression.py) 분석
```python
# 데이터 불러오기
train_data = np.load(".\\datasets\\linear_train.npy")
test_x = np.load(".\\datasets\\linear_test_x.npy")
```
* numpy를 사용해서 데이터셋 가져오기.
#

```python
# 데이터 불러오기
# tf 형식에 맞게 변환
x_data = np.expand_dims(train_data[:,0], axis=1)
y_data = train_data[:,1]
```
* train_data의 인덱스 0의 열의 값들을 가져와서 인덱스1의 위치에 차원을 추가해 x_data를 만든다.
* train_data의 인덱스 1의 열의 값들을 가져와서 y_data를 만든다.
#

```python
# 모델 생성
model = LinearModel(num_units=1)
```
* LinearModel 클래스의 인스턴스를 만든다. (../models/linear_model.py)
#


```python
# 최적화 함수, 손실함수와 모델 바인딩
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
			  loss=tf.keras.losses.MSE,
			  metrics=[tf.keras.metrics.MeanSquaredError()])
```
* 