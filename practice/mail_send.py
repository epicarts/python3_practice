import smtplib


#아이디 설정에 모르는 앱허용 (하) 로 설정 해야함
from_addr = '0505zxc@gmail.com'
to_addrs =  '0505zxc@naver.com'
msg = 'test youngho'

username = '0505zxc'
password = ''

server = smtplib.SMTP('smtp.gmail.com:587')
server

# 서버 구동
server.starttls()

server.login(username,password)


server.sendmail(from_addr, to_addrs, msg)

#서버종료
server.quit()
