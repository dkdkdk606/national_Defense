# 데이터 전처리 모듈
# mlutils/preprocessing.py

# 입력데이터를 0~1로 변환하는 함수

def min_max_scale(data):
    min_v = min(data)
    max_v = max(data)
    scaled_data = []
    for value in data:
        scaled_value = (value - min_v) / (max_v - min_v)
        scaled_data.append(scaled_value)
    return scaled_data