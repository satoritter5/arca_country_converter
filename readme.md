아카라이브 국가제한 변환기
======================

# 사용방법
[**Python 3.8**](https://www.python.org/)을 기준으로 작성되었습니다.

[**Selenium**](https://pypi.org/project/selenium/)이 설치 되어 있어야 합니다.


기본적으로 IDE나 메모장 등으로 arcc_cc.py를 열고 유저 설정 부분에 필요한 부분을 채워 넣어서 사용하시면 됩니다.

# 주의사항
1페이지는 공지사항도 게시글로 취급되어서 공지사항까지 삭제됩니다.
가급적이면 2페이지 부터 작업 해 주십시오.

현재 국가제한은 하나의 지역만 가능합니다.

지역코드는 숫자로만 입력 가능하며, 아래에 해당하는 지역코드를 입력해 주시면 됩니다.

# 지역코드

	1  가나
	2  가봉
	3  가이아나
	4  감비아
	5  건지섬
	6  과들루프
	7  과테말라
	8  괌
	9  그레나다
	10 그리스
	11 그린란드
	12 기니
	13 기니비사우
	14 나미비아
	15 나우루
	16 나이지리아
	17 남극
	18 남수단
	19 남아프리카 공화국
	20 네덜란드
	21 네팔
	22 노르웨이
	23 노퍽섬
	24 누벨칼레도니
	25 뉴질랜드
	26 니우에
	27 니제르
	28 니카라과
	29 대한민국
	30 덴마크
	31 도미니카 공화국
	32 도미니카 연방
	33 독일
	34 동티모르
	35 라오스
	36 라이베리아
	37 라트비아
	38 러시아
	39 레바논
	40 레소토
	41 레위니옹
	42 루마니아
	43 룩셈부르크
	44 르완다
	45 리비아
	46 리투아니아
	47 리히텐슈타인
	48 마다가스카르
	49 마르티니크
	50 마셜 제도
	51 마요트
	52 마카오
	53 말라위
	54 말레이시아
	55 말리
	56 맨섬
	57 멕시코
	58 모나코
	59 모로코
	60 모리셔스
	61 모리타니
	62 모잠비크
	63 몬테네그로
	64 몬트세랫
	65 몰도바
	66 몰디브
	67 몰타
	68 몽골
	69 미국
	70 미국령 군소 제도
	71 미국령 버진아일랜드
	72 미얀마
	73 미크로네시아 연방
	74 바누아투
	75 바레인
	76 바베이도스
	77 바티칸 시국
	78 바하마
	79 방글라데시
	80 버뮤다
	81 베냉
	82 베네수엘라
	83 베트남
	84 벨기에
	85 벨라루스
	86 벨리즈
	87 보네르섬
	88 보스니아 헤르체고비나
	89 보츠와나
	90 볼리비아
	91 부룬디
	92 부르키나파소
	93 부베섬
	94 부탄
	95 북마리아나 제도
	96 북마케도니아
	97 불가리아
	98 브라질
	99 브루나이
	100사모아
	101사우디아라비아
	102사우스조지아 사우스샌드위치 제도
	103산마리노
	104상투메 프린시페
	105생마르탱
	106생바르텔레미
	107생피에르 미클롱
	108서사하라
	109세네갈
	110세르비아
	111세이셸
	112세인트루시아
	113세인트빈센트 그레나딘
	114세인트키츠 네비스
	115세인트헬레나
	116소말리아
	117솔로몬 제도
	118수단
	119수리남
	120스리랑카
	121스발바르 얀마옌
	122스웨덴
	123스위스
	124스페인
	125슬로바키아
	126슬로베니아
	127시리아
	128시에라리온
	129신트마르턴
	130싱가포르
	131아랍에미리트
	132아루바
	133아르메니아
	134아르헨티나
	135아메리칸사모아
	136아이슬란드
	137아이티
	138아일랜드
	139아제르바이잔
	140아프가니스탄
	141안도라
	142알바니아
	143알제리
	144앙골라
	145앤티가 바부다
	146앵귈라
	147에리트레아
	148에스와티니
	149에스토니아
	150에콰도르
	151에티오피아
	152엘살바도르
	153영국
	154영국령 버진아일랜드
	155영국령 인도양 지역
	156예멘
	157오만
	158오스트레일리아
	159오스트리아
	160온두라스
	161올란드 제도
	162왈리스 푸투나
	163요르단
	164우간다
	165우루과이
	166우즈베키스탄
	167우크라이나
	168이라크
	169이란
	170이스라엘
	171이집트
	172이탈리아
	173인도
	174인도네시아
	175일본
	176자메이카
	177잠비아
	178저지섬
	179적도 기니
	180조선민주주의인민공화국
	181조지아
	182중국
	183중앙아프리카 공화국
	184중화민국
	185지부티
	186지브롤터
	187짐바브웨
	188차드
	189체코
	190칠레
	191카메룬
	192카보베르데
	193카자흐스탄
	194카타르
	195캄보디아
	196캐나다
	197케냐
	198케이맨 제도
	199코모로
	200코스타리카
	201코코스 제도
	202코트디부아르
	203콜롬비아
	204콩고 공화국
	205콩고 민주 공화국
	206쿠바
	207쿠웨이트
	208쿡 제도
	209퀴라소
	210크로아티아
	211크리스마스섬
	212키르기스스탄
	213키리바시
	214키프로스
	215타지키스탄
	216탄자니아
	217태국
	218터크스 케이커스 제도
	219터키
	220토고
	221토켈라우
	222통가
	223투르크메니스탄
	224투발루
	225튀니지
	226트리니다드 토바고
	227파나마
	228파라과이
	229파키스탄
	230파푸아뉴기니
	231팔라우
	232팔레스타인
	233페로 제도
	234페루
	235포르투갈
	236포클랜드 제도
	237폴란드
	238푸에르토리코
	239프랑스
	240프랑스령 기아나
	241프랑스령 남방 및 남극 지역
	242프랑스령 폴리네시아
	243피지
	244핀란드
	245필리핀
	246핏케언 제도
	247허드 맥도널드 제도
	248헝가리
	249홍콩