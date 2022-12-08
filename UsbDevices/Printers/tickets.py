from time import strftime


class Tickets:
    def __init__(self, email, phone, money_h, parking_id):
        self.email = email
        self.phone = phone
        self.url = f'https://a1park.com/parking/{parking_id}'
        self.money_h = money_h
        self.parking_id = parking_id

    def entry(self, url, order_id):
        return f"""  
<text pd=6 align=left>
   <text>Парковка {self.parking_id} </text>
   <text>Дата: {strftime("%d.%m.%y Время %H:%M")} </text> 
   <text>ID заказа: <b>{order_id}</b> </text> 
   
   <text>Въезжая на паркинг вы соглащаетесь </text>
   <text>с правилами пользования парковки </text>  
   
   <text>{self.url} </text> 
   <text>Сервисный сбор НОП 3% </text>
   <text>Стоимость <b>{self.money_h}</b> Руб./час </text>
   
   <text pd=6 size=10 align=center>!Внимание!</text>
   <text pd=6 align=left></text>
   <text>----------------------------------------</text> 
   <text>Для выезда наведите камеру телефона</text> 
   <text>на QR код и пройдите на страницу</text> 
   <text>для оплаты.</text>
   <text>После оплаты появится кнопка ВЫЕЗД. </text>
   <text>Находясь ПЕРЕД ШЛАГБАУМОМ нажмите ее</text> 
   <text>и шлагбаум откроется.</text> 
   <text>----------------------------------------</text> 
   
   <text align=center><QR content={url}></text> 
    <text pd=6 align=left></text>
   <text>Телефон для справок:</text> 
   <text><b>{self.phone}</b></text>
   <text><b>{self.email}</b></text>





</text>
                """

    def notPlaces(self):
        return f"""  
<text pd=6 align=left>
   <text>Парковка {self.parking_id} </text>
   <text>Дата: {strftime("%d.%m.%y Время %H:%M")} </text>
   <text>Въезжая на паркинг вы соглащаетесь </text>
   <text>с правилами пользования парковки </text>  
   <text>{self.url}</text> 
   <text>Стоимость <b>{self.money_h}</b> Руб./час </text>
   <text>Сервисный сбор НОП 3% </text>

   <text>К сожалению нет свободных мест,</text>
   <text>попробуйте чуть позже,</text>
   <text>как места появятся - обязательно</text>
   <text>вам сообщим!</text>
   <text>или позвоните в call центр,</text>

   <text>Телефон для справок:</text> 
   <text><b>{self.phone}</b></text>
   <text><b>{self.email}</b></text>
</text>
"""
