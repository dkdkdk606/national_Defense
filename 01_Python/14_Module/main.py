# main.py
# mlutils 패키지의 모듈을 사용하는 파일

# 데이터 수집 -> 데이터 전처리 -> 데이터 훈련/예측 -> 평가

# 필요 모듈 임포트
from mlutils.data_loader import load_data
from mlutils.preprocessing import min_max_scale
from mlutils.model_utils import predict
from mlutils.metrics import mae

# 1. 데이터 로딩
X, y = load_data()
print('공부시간, X')
print('시험점수: y')

# 2. 데이터 전처리
scaled_X = min_max_scale(X)
print('정규화 데이터: ', scaled_X)

# 3. 데이터 예측
pred_list = []
for hour in X:
    pred = predict(hour)
    pred_list.append(pred)

print('예측 결과: ', pred_list)

predict()
# 4. 평가

score = mae(y, pred_list)
print("MAE: ". score)