# utilizar crontab pra executar esse script de minuto em minuto

from bs4 import BeautifulSoup
import requests
import smtplib
import email.message

url = 'https://www.brasiltronic.com.br/camera-fujifilm-x-t30-mirrorless-preto-somente-corpo-p1324086'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content,'html.parser')

title = soup.find('h1', class_ = 'name').get_text()

price = soup.find('strong', class_ = 'sale-price').find('span').get_text().strip()

num_price = price[3:8] # R$ 7.469,10 vira 7.469
num_price = num_price.replace('.','') # 7.469 vira 7469
num_price = float(num_price) # 7469 vira 7469.0

#print(title)
#print(price)
#print(num_price)

def send_email():
    email_content = """
    https://www.brasiltronic.com.br/camera-fujifilm-x-t30-mirrorless-preto-somente-corpo-p1324086
    """

    msg = email.message.Message()
    msg['Subject'] = 'Preço Camera Baixou!!'

    msg['From'] = 'valdir.junior@email.com.br'
    msg['To'] = 'valdir.junior@email.com.br'
    password = ''
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print('Sucesso ao enviar email')

if(num_price < 8000):
    send_email()




