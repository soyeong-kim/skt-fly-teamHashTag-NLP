# BERT모델 기반 문서의 토픽 분류 모델</br>(BERT-based Topic Classification Model for Documents)
### 파일 구조
```
wanso/
├── 01_make_dataset.ipynb
└── 02_Multilingual_BERT.ipynb
```
### 데이터셋
AI-Hub에서 제공하는 [주제별 텍스트 일상 대화 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100)를 활용하여 분류 모델을 학습하였습니다.</br>
10개의 주제를 선정하여 train.csv와 validation.csv 파일을 구축하였습니다.
### 학습 결과: Validation Set
|모델|Acc|
|:---:|:---:|
|Multilingual BERT|0.91|
