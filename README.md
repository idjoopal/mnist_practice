# python - tensorflow mnist 예제

- HW 환경
  - Windows 10
  - i3 6세대 스카이레이크
  - GPU 없음


1. Anaconda 최신버전 설치
   1. 19년 2월 기준으로 Python 최신 버전은 3.7이다.
   2. 19년 2월 기준으로 Tensorflow가 원활하게 지원되는 Python 버전은 3.6이다.
   3. Anaconda를 통해 Python 3.7을 설치하고, 가상환경을 3.6으로 구현하는 방법을 사용한다.

2. Tensorflow 설치
   1. [https://www.tensorflow.org/install/pip](https://www.tensorflow.org/install/pip)  Windows 기준 설치 방법
   2. 가상환경(virtual environment, venv)를 사용하는 이유는, 파이썬 인터프리터의 버전에 따라 파이썬으로 구성된 프로그램이 실행이 달라질 수 있기 때문이다. 가상환경으로, 파이썬이 돌아가는 환경을 구분해주는 것이다.
   3. anaconda를 사용했으므로 가상환경을 생성하기 위해 다음의 코드를 입력한다.
        > `conda create -n venv pip python=3.6  # select python version`
   4. 가상환경을 활성화 한다.
        > `source activate venv`
   5. 가상환경 내에서 tensorflow 설치. 나는 GPU가 없으므로 -gpu가 붙지 않은 것을 선택했다.
        > `pip install --upgrade tensorflow`
   6. 나중에 가상환경을 비활성화하려면 아래의 코드를 입력한다.
        > `source deactivate`


