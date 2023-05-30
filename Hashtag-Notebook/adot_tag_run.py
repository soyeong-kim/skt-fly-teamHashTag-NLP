from adot_clf_model import PredictModel
from adot_tag_generate import GetKeyword,GetHashtag,get_section_score
import numpy as np

if __name__ == '__main__':
    """
    user_cat: 카테고리 리스트 []
    total_stt: 구간별 리스트 [[],[],[], ...]
    ws_obj_lst: 구간별 이미지 리스트 [{}, {}, {}, ...]
    user_cat, total_stt, ws_obj_lst 만 바꾸면 된다.
    """
    user_cat = [1]
    
    total_stt = [['프린트 숙제가 너무 많아서 아침 6시 40분에 일어났어요', 
                  '너무 졸렸지만 어쩔 수 없지', 
                  '요즘은 학원 다니면서 공부하고 있어요', 
                  '이렇게 하루종일 공부만 많이 하는 방학은 오랜만', 
                  '예비고1 정말 중요한데 힘들다'], 
                  ['학원 갈 준비하고 있어요', 
                  '거의 댄스 연습실 가야할 듯','털 슬리퍼랑 잘 어울리는 느낌', 
                  '대충 선크림 발라주고 학원 가겠습니다', 
                  '맨날 후드티만 입고 다니는데 오늘은 약간 신경써봄', 
                  '요즘 새벽 공부를 너무 많이해요']]
    
    ws_obj_lst = [{'5': 2, '50': 3}, {'2': 2, '5': 5}]

    pred = PredictModel('cpu') # 'cpu' or 'cuda'
    get_key = GetKeyword()
    get_tag = GetHashtag()
    ws_score = get_section_score(user_cat, total_stt, pred)
    print(ws_score) # 스코어
    max_idx = np.argmax(ws_score)
    temp = get_key(total_stt, max_idx)
    print(temp)
    hashtag = get_tag(user_cat, ws_obj_lst, max_idx, temp)
    print(hashtag) # 태그