# 모델 성능 평가 지표 모듈
# mlutils/metrics.py
'''
MAE 지표 : e = y_true - y_pred
    mae = sum(|e|)
'''

def mae(y_true, y_pred):
    total_error = 0
    for true, pred in zip(y_true, y_pred):
        error = abs(true-pred)
        total_error += error
    return total_error/len(y_true)