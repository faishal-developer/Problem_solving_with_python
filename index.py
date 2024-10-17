class Phone:
    price = 19000
    color='blue'
    brand='samsung'
    features=["camera","speaker","hammer"]

    def call(self):{
        print("call")
    }

    def send_sms(self,phone,sms):
        text=f'sending sms to:{phone} and {sms}'
        return text
    

my_phone=Phone()
my_phone.call()
print(my_phone.send_sms(5586,"kdfjdkf"))