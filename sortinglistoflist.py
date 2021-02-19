lst=[['2021/02/17', 2, '한글과컴퓨터', '25,000'], ['2021/02/16', 1, '해마로푸드서비스', '3,800'], 
     ['2021/02/15', 1, '경동나비엔', '100,000'], ['2021/02/16', 4, '케이티', '36,000'], 
     ['2021/02/15', 8, '한국항공우주', '52,000']]

lst.sort(key=lambda x: x[1],reverse=True) #sorting in descending order
#print("Price of %s is %s" % (data[1].text,data[3].text))
lst
