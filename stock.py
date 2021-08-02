import requests
from lxml import html

url = str(input("Enter the url"))
page = requests.get(url)
tree = html.fromstring(page.content)


def stock_basic():
 stock_name = tree.xpath('/html/body/div/div[3]/div/div/div[1]/div[1]/h3/text()')
 print(stock_name)

 stock_price = tree.xpath('/html/body/div/div[3]/div/div/div[1]/div[3]/span[1]/text()')

 for i in stock_price:
     print("\n"'Current Price: ',i)
 
 stock_pe = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[3]/div/div/div[1]/div[2]/text()')
 print("STOCK PE: ")

 stock_pb = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/div[2]/text()')
 print("STOCK PB: ",stock_pe)
 
 divedend_yeild = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[3]/div/div/div[3]/div[2]/text()')
 print("DIVEDEND YEILD: ",divedend_yeild)
 
stock_basic()

user_choice_1 = int(input('''press 1 for veiwing our statment toward stock
press 0 for not veiwing our statment toward stock : '''))



def version_statment():

   print("*******************************************************************")
   analyist_stament = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[4]/div/div[1]/div/span/text()')
   print("\nAnalyist suggest to buy  : ", analyist_stament,'%')

   print("\nINVESTMENT CHECKLIST")
   intrinsic_value = tree.xpath('/html/body/div/div[3]/div/div/div[1]/div[5]/section/div[1]/div[1]/div/p/text()')
   print(intrinsic_value)

   print("\nRETURN VS FD RETURN")
   return_vs_FD_rate = tree.xpath('/html/body/div/div[3]/div/div/div[1]/div[5]/section/div[1]/div[2]/div/p/text()')
   print(return_vs_FD_rate)

   print("\nDIVIDEND RETURN")
   dividend_return = tree.xpath('/html/body/div/div[3]/div/div/div[1]/div[5]/section/div[1]/div[3]/div/p/text()')
   print(dividend_return)
 
   print("\nENTERY POINT")
   entry_point = tree.xpath('/html/body/div/div[3]/div/div/div[1]/div[5]/section/div[1]/div[4]/div/p/text()')
   print(entry_point)
   print("*******************************************************************") 
  
if user_choice_1 == 1:
    version_statment()

else:
    print("THANK YOU")

user_choice_2 = int(input('''Press 1 for veewing peers
Press 0 for not vewing peers: '''))


def peers():
    peers_1 = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[7]/div/div/div/a[1]/div[1]/span/text()')
    print("\n 1.",peers_1)
    peers_2 = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[7]/div/div/div/a[2]/div[1]/div/h4/text()')
    print("\n 2.",peers_2)
    peers_3 = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[7]/div/div/div/a[3]/div[1]/div/h4/text()')
    print("\n 3.",peers_3)
    peers_4 = tree.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[7]/div/div/div/a[4]/div[1]/div/h4/text()')
    print("\n 4.",peers_4)

if user_choice_2 == 1:
    peers()
else:
    print("THANK YOU")
    
def brand():
    brand_1 = tree.xpath("/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[5]/div/div/div[1]/div[1]/div[2]/h3/text()")
    print("1 >",brand_1)
    brand_2 = tree.xpath("/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[5]/div/div/div[1]/div[2]/div[2]/h3/text()")
    print("2 >",brand_2)    
    brand_3 = tree.xpath("/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[5]/div/div/div[1]/div[3]/div[2]/h3/text()")
    print("3 >",brand_3) 
    brand_4 = tree.xpath("/html/body/div/div[3]/div/div/div[2]/div[2]/div[3]/div[5]/div/div/div[1]/div[4]/div[2]/h3/text()")
    print("4 >",brand_4) 
    
user_choice_3 = int(input("Enter 1 for vewing brands|| 0 for not veiwing brand"))

if user_choice_3 == 1:
    brand()
    
else:
    print("THANK YOU")
    
#financial 

