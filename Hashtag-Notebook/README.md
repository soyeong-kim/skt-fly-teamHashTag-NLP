# 해시태그 추출 알고리즘(Hashtag Extraction Algorithm)
### 파일 구조
```
wanso/
├── pickle_data/
│   ├── common_tag.pickle
│   ├── dic.pickle
│   ├── hash_table.pickle
│   └── img_table.pickle
├── weights/
│   └── classification_model.pt
├── adot_clf_model.py
├── adot_tag_generate.py
├── adot_tag_run.py
└── ko.bin
```
### 설치 파일
1. 필요한 라이브러리 설치: requirements.txt</br>
    ✅ **Python 3.8.8 버전**에서 파일을 실행함
    ```
    !pip install -r requirements.txt
    ```
2. 사전 훈련된 한국어 Word2Vec 임베딩 설치</br>
    2-1. [사전 훈련된 한국어 Word2Vec 임베딩 다운로드 경로](https://drive.google.com/file/d/0B0ZXk88koS2KbDhXdWg1Q2RydlU/view?resourcekey=0-Dq9yyzwZxAqT3J02qvnFwg)<br>
    2-2. 압축 해제 후 ko.bin 파일 사용
    ```
    !unzip ko.zip
    ```
3. Topic Classification Model의 weights 파일(.pt) 다운로드</br>
    ✅ [Classification-Notebook](https://github.com/soyeong-kim/skt-fly-teamHashTag-NLP/tree/main/Classification-Notebook)에서 Fine-tuning한 Multilingual BERT 모델의 가중치(classification_model.pt)를 사용함</br>
    ✅ **경로**: weights/classification_model.pt
### 파일 실행
```
python3 adot_tag_run.py
```
