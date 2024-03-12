import time
import requests
import re
from threading import Thread


def buyproductblock():
    file01 = open('C:/Users/admin/Documents/WorkFiles/only_alias_compl_cat.txt')
    textdata = file01.read()
    textdata = textdata.split()
    file01.close()

    for i in textdata:
        file02 = open(f'C:/Users/admin/Documents/WorkFiles/script_execute_result/productData/{i}.txt')
        textdata_id = file02.read()
        file02.close()
        prdid = re.sub("[^\d\n]", "", textdata_id)
        prdid = prdid.split()
        print(prdid)

        for i in prdid:
            time.sleep(0.4)
            query = f'''{{
                buyAlso(product_id: {i}) {{
                title
                source
                products {{
                  algSource
                  product {{
                    id
                        }}
                        }}
                    }}
                    }}
                '''
            reqst = requests.post(
                url='https://ssss.ss/sssss', # запрос на сервис
                json={
                    'query': query,
                    'variables': None
                },
                cookies={
                    'auth': 'тут был токен'
                }
            )
            # print(reqst.json())

            data = reqst.json()
            filtered_products = [p for p in data['data']['buyAlso']['products'] if p['algSource'] == 'v9']
            for product in filtered_products:
                tempvar_01 = str(product['product'])
                edit_tempvar_01 = re.sub("[^0-9]", "", tempvar_01)
                query = f'''
                               {{
                               product(id: {edit_tempvar_01})
                               {{
                               name
                               urlForCanonical
                               }}
                               }}
                               '''

                preq = requests.post(
                    url='https://ssss.ss/sssss',
                    json={
                        'query': query,
                        'variables': None
                    },
                    cookies={
                        'auth': 'тут был токен'
                    }
                )
                with open('C:/Users/admin/Documents/WorkFiles/script_execute_result/buyAlso/buyalso2.txt', 'a+') \
                        as f:
                    tempvar = preq.json()
                    tempvar = tempvar['data']['product']['urlForCanonical']
                    tempvar = str(tempvar)
                    tempvar = tempvar + '\n'
                    f.write(tempvar)


def productblockace():
    file01 = open('C:/Users/admin/Documents/WorkFiles/only_alias_compl_cat.txt')
    textdata = file01.read()
    textdata = textdata.split()
    file01.close()

    for i in textdata:
        file02 = open(f'C:/Users/admin/Documents/WorkFiles/script_execute_result/productData/{i}.txt')
        textdata_id = file02.read()
        file02.close()
        prdid = re.sub("[^\d\n]", "", textdata_id)
        prdid = prdid.split()
        print(prdid)

        for i in prdid:
            time.sleep(0.4)
            query = f'''{{
                productAccessories(product_id: {i}) {{
                title
                source
                products {{
                  algSource
                  product {{
                    id
                        }}
                        }}
                    }}
                    }}
                '''
            reqst = requests.post(
                url='https://ssss.ss/sssss',
                json={
                    'query': query,
                    'variables': None
                },
                cookies={
                    'auth': 'тут был токен'
                }
            )
            # print(reqst.json())

            data = reqst.json()
            filtered_products = [p for p in data['data']['productAccessories']['products'] if p['algSource'] == 'v9']
            for product in filtered_products:
                tempvar_01 = str(product['product'])
                edit_tempvar_01 = re.sub("[^0-9]", "", tempvar_01)
                query = f'''
                               {{
                               product(id: {edit_tempvar_01})
                               {{
                               name
                               urlForCanonical
                               }}
                               }}
                               '''

                preq = requests.post(
                    url='https://ssss.ss/sssss',
                    json={
                        'query': query,
                        'variables': None
                    },
                    cookies={
                        'auth': 'тут был токен'
                    }
                )
                with open(
                        'C:/Users/admin/Documents/WorkFiles/script_execute_result/productAccessories/productAccessories2.txt',
                        'a+') \
                        as f:
                    tempvar = preq.json()
                    tempvar = tempvar['data']['product']['urlForCanonical']
                    tempvar = str(tempvar)
                    tempvar = tempvar + '\n'
                    f.write(tempvar)



thread1 = Thread(target=productblockace)
thread2 = Thread(target=buyproductblock)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
