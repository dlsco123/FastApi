from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # 오타 수정
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/gpt"

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', DATABASE_URL)  # 환경변수에 없을 경우 기본값 사용

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # 여기에서 declarative_base()는 SQLAlchemy의 함수로서, 모든 모델 클래스의 슈퍼클래스를 생성합니다.
