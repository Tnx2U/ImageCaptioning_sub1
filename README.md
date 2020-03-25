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
# model = Model(inputs=a, outputs=b) 로 생성시 a입력하면 b가 나오는 함수를 만들어준다.
```
* LinearModel 클래스의 인스턴스를 만든다. (../models/linear_model.py)
#


```python
# 최적화 함수, 손실함수와 모델 바인딩
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
			  loss=tf.keras.losses.MSE,
			  metrics=[tf.keras.metrics.MeanSquaredError()])
```
* model을 컴파일하는 과정이다. 필수적으로 optimizer와 loss라는 두 개의 매개변수를 가진다.
* optimizer(최적화 함수)는 SGD(확률적 경사 하강법)을 사용하였다.
* loss는 손실함수로써, 여기선 tf 라이브러리의 MSE(mean_squared_logarithmic_error예상)를 사용하였다.
* metrics는 학습된 모델에 의해 평가될 metrics를 지정한다.
#

```python
# 모델 학습
model.fit(x=x_data, y=y_data, epochs=10, batch_size=32)
```
* fit()함수는 epochs 회수만큼 모델을 학습시키는 함수이다.
* x = 인풋값, y = 타겟 데이터, epochs = 모델학습을 반복할 횟수, batch_size = 한번의 batch마다 주는 데이터의 크기
#

```python
# 모델 테스트
prediction = model.predict(x=test_x,batch_size=None)
```
* 입력 결과에 대한 결과값을 예측하는 함수이다.
* x = 입력값, batch_size = 경사 업데이트당 샘플 개수로 기본은 32이다.
#

```python
# 결과 시각화
plt.scatter(x_data,y_data,s=5,label="train data")
plt.scatter(test_x,prediction,s=5,label="prediction data")
plt.legend()
plt.show()
```
* scatter() : 산포그래프를 작성하는 함수 , s = 마커의 크기를 입력 label = 라벨지정
* legend() : 범례를 추가하는 함수인데 여기서 아무것도 안했다.
* show() : 작성된 그래프를 출력하는 함수
#

```python
# 모델 정리
model.summary()
```
* 다중 레이어에 대해 작성한 모델에 대한 요약을 출력한다.
