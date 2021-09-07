청와대 청원 주제 분류 과제<br>
https://dacon.io/competitions/open/235597/overview/description<br>
여기 링크에서 대회 참여한거임<br>
<br>
![image](https://user-images.githubusercontent.com/77532413/132273087-e969c921-cdd2-494a-8bdd-23b2436aff29.png)
<br>
<br>
공유 돼있는 코드 중에 트랜스포머 모델 활용한거 도움을 받아 공부함
<br>
<br>
트랜스포머 모델은 구글에서 제안한 모델로 <br>
![image](https://user-images.githubusercontent.com/77532413/132273299-75f327e3-1e11-4886-8434-39f8506e2b52.png)
<br>
이런식의 구조를 가지고 있음
<br>
<br>
rnn이나 lstm같은 애들은 time sequence에 따라 학습이 진행되는데, <br>
트랜스포머 모델은 쟤네 안쓰고 attention 메커니즘을 활용해서 time sequence를 구현한 빠르고 성능좋은 모델임
<br>
<br>
그러면 attention 메커니즘이 뭐냐
<br><br>
기존에 단어들간 관계를 알기위해 사용한 seq2seq라는 메커니즘은 encoder와 decoder를 사용하여<br>
데이터를 일정한 크기의 벡터로 변환해주는 방식이었는데<br>
얘네들이 정보손실이 좀 컸음
<br>
얘네를 보완해주려고 나온 메커니즘이 attention 메커니즘임<br>
그냥 간단하게 말하면 단어별로 벡터변환해서 길이에 따라 decoding된 결과의 크기가 달라지는거
<br>
근데 자세한건 잘 모르겠어서 이번 스터디때 관련논문 읽어보고 공부하려고예
<br>
<br>

여튼 내가 사용한 모델은 <br>
![image](https://user-images.githubusercontent.com/77532413/132274608-3e311858-6628-40b2-b89f-8e6b2394757b.png)
<br><br>
이런 구조를 가지고 있음
<br>
<br>
여튼 코드 참고하삼
<br><br>
