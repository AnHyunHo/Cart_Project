import sys

def database_sort(barcode):
      database = barcode[0]
      table = barcode[1:3]
      name = barcode[3:6]
      if database == "9": #database(food)
            if table == "00": #table(snack)
                  if name == "000": #name(포카칩)
                        return '음식' , '스낵류' , '포카칩'
                  elif name == "001":
                        return '음식' , '스낵류' , '수미칩'
                  elif name == "002":
                        return '음식' , '스낵류' , '새우깡'
            elif table == "01": #table(fork)
                  if name == "000":
                        return '음식' , '육류' , '소고기'
                  elif name == "001":
                        return '음식' , '육류' , '닭고기'
                  elif name == "002":
                        return '음식' , '육류' , '돼지고기'
            elif table == "02" :#table(vagetable)
                  if name == "000":
                        return '음식' , '야채' , '당근'
                  elif name == "001":
                        return '음식' , '야채' , '청양 고추'
                  elif name == "002":
                        return '음식' , '야채' , '배추'
            elif table == "03" : #table(see_food)
                  if name == "000":
                        return '음식' , '해산물' , '고등어'
                  if name == "001":
                        return '음식' , '해산물' , '참치'
                  if name == "002":
                        return '음식' , '해산물' , '오징어'
      elif database == "8":#database(가전)
            if table == "00":#컴퓨터
                  if name == "000":
                        return '가전' , '컴퓨터' , '모니터'
                  elif name == "001":
                        return '가전' , '컴퓨터' , '노트북'
                  elif name == "002":
                        return '가전' , '컴퓨터' , '데스크탑'
                  elif name == "003":
                        return '가전' , '컴퓨터' , '마우스'
            if table == "01":#게이밍
                  if name == "000":
                        return '가전' , '게이밍' , '스위치'
                  elif name == "001":
                        return '가전' , '게이밍' , '플레이스테이션'
                  elif name == "002":
                        return '가전' , '게이밍' , '엑스박스'
                  elif name == "003":
                        return '가전' , '게이밍' , '닌텐도'
            if table == "02":#휴대폰
                  if name == "000":
                        return '가전' , '휴대폰' , '아이폰'
                  elif name == "001":
                        return '가전' , '휴대폰' , '갤럭시'
                  elif name == "002":
                        return '가전' , '휴대폰' , '아이패드'
                  elif name == "003":
                        return '가전' , '휴대폰' , '갤럭시탭'
            if table == "03":#tv
                  if name == "000":
                        return '가전' , 'tv' , '삼성 TV'
                  elif name == "001":
                        return '가전' , 'tv' , 'LG TV'
                  elif name == "002":
                        return '가전' , 'tv' , '한성 TV'
                  elif name == "003":
                        return '가전' , 'tv' , '이노스 TV'
      elif database == "7":#database(의류)
            if table == "00":#상의
                  if name == "000":
                        return '의류' , '상의' , '코트'
                  elif name == "001":
                        return '의류' , '상의' , '티셔츠'
                  elif name == "002":
                        return '의류' , '상의' , '조끼'
                  elif name == "003":
                        return '의류' , '상의' , '재킷'
            if table == "01":#신발
                  if name == "000":
                        return '의류' , '신발' , '구두'
                  elif name == "001":
                        return '의류' , '신발' , '운동화'
                  elif name == "002":
                        return '의류' , '신발' , '슬리퍼'
                  elif name == "003":
                        return '의류' , '신발' , '로퍼'
            if table == "02":#쥬얼리
                  if name == "000":
                        return '의류' , '쥬얼리' , '반지'
                  elif name == "001":
                        return '의류' , '쥬얼리' , '목걸이'
                  elif name == "002":
                        return '의류' , '쥬얼리' , '시계'
                  elif name == "003":
                        return '의류' , '쥬얼리' , '귀걸이'
            if table == "03":#하의
                  if name == "000":
                        return '의류' , '하의' , '반바지'
                  elif name == "001":
                        return '의류' , '하의' , '청바지'
                  elif name == "002":
                        return '의류' , '하의' , '슬랙스'
                  elif name == "003":
                        return '의류' , '하의' , '패션바지'
      elif database == "6":#database(생필품)
            if table == "00":#영양제
                  if name == "000":
                        return '생필품' , '영양제' , '비타민'
                  elif name == "001":
                        return '생필품' , '영양제' , '밀크씨슬'
                  elif name == "002":
                        return '생필품' , '영양제' , '유산균'
                  elif name == "003":
                        return '생필품' , '영양제' , '종합영양제'
            if table == "01":#욕실용품
                  if name == "000":
                        return '생필품' , '욕실용품' , '락스'
                  elif name == "001":
                        return '생필품' , '욕실용품' , '샤워기'
                  elif name == "002":
                        return '생필품' , '욕실용품' , '하수구트랩'
                  elif name == "003":
                        return '생필품' , '욕실용품' , '청소솔'
            if table == "02":#위생용품
                  if name == "000":
                        return '생필품' , '욕실용품' , '손소독제'
                  elif name == "001":
                        return '생필품' , '욕실용품' , '샴푸'
                  elif name == "002":
                        return '생필품' , '욕실용품' , '로션'
                  elif name == "003":
                        return '생필품' , '욕실용품' , '바디워시'
            if table == "03":#화장지
                  if name == "000":
                        return '생필품' , '화장지' , '각티슈'
                  elif name == "001":
                        return '생필품' , '화장지' , '롤화장지'
                  elif name == "002":
                        return '생필품' , '화장지' , '키친타월'
                  elif name == "003":
                        return '생필품' , '화장지' , '타월'