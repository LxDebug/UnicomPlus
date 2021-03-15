# -*- coding: utf-8 -*-

import requests

#获取 encrymobile，用于抽奖
def get_encryptmobile():
    page = client.post('https://m.client.10010.com/dailylottery/static/textdl/userLogin')
    page.encoding='utf-8'
    match = re.search('encryptmobile=\w+',page.text,flags=0)
    usernumber = match.group(0)[14:]
    return usernumber

#天天抽奖
#我的 --> 我的金币 --> 天天抽好礼
def luckDraw_task():
    try:
        numjsp = get_encryptmobile()
        #加上这一堆，看中奖率会不会高点
        client.post('https://m.client.10010.com/mobileservicequery/customerService/share/defaultShare.htm')
        client.get('https://m.client.10010.com/dailylottery/static/doubleball/firstpage?encryptmobile=' + numjsp)
        client.get('https://m.client.10010.com/dailylottery/static/outdailylottery/getRandomGoodsAndInfo?areaCode=076')
        client.get('https://m.client.10010.com/dailylottery/static/active/findActivityInfo?areaCode=076&groupByType=&mobile=' + numjsp)
        for i in range(3):
            luck = client.post('https://m.client.10010.com/dailylottery/static/doubleball/choujiang?usernumberofjsp=' + numjsp)
            luck.encoding='utf-8'
            res = luck.json()
            logging.info('【天天抽奖】: ' + res['RspMsg'] + ' x' + str(i+1))
            #等待1秒钟
            time.sleep(1)
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【天天抽奖】: 错误，原因为: ' + str(e))
