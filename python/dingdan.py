import requests
import sys
# sys.path.append(r'')
from  jiekou_1.data import duqu
class ding_dan(object ):
    def mingxi(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch"
        header = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "dcad356abf871524d1188de3bd15b985",
            'cache-control': "no-cache",
            'Postman-Token': "8fdbafc3-a3cc-4b9c-9b7f-60b06111c109"
        }
        payload="{\r\n \"pageNum\":\"%d\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}" %(num)
        response = requests.request("POST", url, data=payload, headers=header)
        print(response.json())
        return  response.json()

if __name__ == '__main__':
   for num in duqu.shuju():
     ding_dan().mingxi(num[0])
     #    print(num[0])