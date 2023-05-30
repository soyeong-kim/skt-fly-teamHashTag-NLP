# BERT모델 기반 문서의 토픽 분류 모델</br>(BERT-based Topic Classification Model for Documents)
### 파일 구조
```
wanso/
├── src/
│   ├── (작성중..)
│   ├── 
│   └── 
└── notebook/
    ├── 01_dataset.ipynb
    ├── 02_Multilingual_BERT.ipynb
    └── 03_KoBERT.ipynb
```
### 데이터셋
AI-Hub에서 제공하는 [주제별 텍스트 일상 대화 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100)를 활용하여 분류 모델을 학습하였습니다.</br>
10개의 주제를 선정하여 train.csv와 validation.csv 파일을 구축하였습니다.

### 실험
|모델|Acc|F1-Score|
|:---:|:---:|:---:|
|Multilingual BERT|||
|KoBERT|||

### To Do List
- [ ] src 실행 파일 구축(Multilingual BERT, KoBERT, XLM-RoBERTa, KoELECTRA, KcBERT 등을 실행하기 쉽게 코드 작성)
