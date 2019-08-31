import re
import time
import requests
from lxml import etree

mycookie='SINAGLOBAL=3421616684015.8022.1553341957702; YF-V5-G0=27518b2dd3c605fe277ffc0b4f0575b3; _s_tentry=-; Apache=7384080538721.845.1560491267723; ULV=1560491268670:2:1:1:7384080538721.845.1560491267723:1553341957713; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; TC-Page-G0=c4376343b8c98031e29230e0923842a5|1563515423|1563515423; TC-V5-G0=4e714161a27175839f5a8e7411c8b98c; login_sid_t=b8c891f44a7796ade4811399a8931ea3; cross_origin_proto=SSL; WBtopGlobal_register_version=307744aa77dd5677; wb_view_log=1920*10801; UOR=,,graph.qq.com; SCF=Ap2R5FUd7cMhzjpENYwuxB1rp5-YfOf0E-VWPgO0qXJRUVA8x6Fvxe-QkqJGrWJcPtz7jfiH6IlqzvY61phdlGE.; SUB=_2A25wbLmcDeRhGeNJ6VER8ijPyjSIHXVTG6xUrDV8PUNbmtBeLXTYkW9NS_yBOzkJhCiATvVeHwhE5Ubh0pQ8tUn6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFf1rjr6QrnVVwMgQP9Dg9f5JpX5K2hUgL.Fo-Neoe7eoq0eKn2dJLoIE2LxKML1-BLBK2LxKnLBo-LBoMLxK-L1KMLBKykSK-feKBt; SUHB=0wn1psQVQyAacV; ALF=1567753291; SSOLoginState=1567148492; un=15606907698; wb_view_log_5723026318=1920*10801; YF-Page-G0=aac25801fada32565f5c5e59c7bd227b|1567150693|1567150641; webim_unReadCount=%7B%22time%22%3A1567151129933%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
def cookieserialize(cookie):
    dict_ = {}
    ret = cookie.split(';')

    for item in ret:
        try:
            key, value = item.split('=')
            dict_[key.strip()] = value.strip()
        except ValueError:
            key, value = item.split('=', 1)
            dict_[key.strip()] = value.strip()
    return dict_

ret = cookieserialize(mycookie)




url='https://weibo.com/u/5263638242?refer_flag=1005050008_&is_all=1'
oidparttern = re.compile("https://weibo.com/u/(.*?)/")
oid = oidparttern.findall(url)[0]

url='''https://weibo.com/p/100505{0}/info?mod=pedit_more&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fu%2F{0}%3Frefer_flag%3D1005050006_%26is_hot%3D1&_t=FM_{1}'''.format(oid,int(time.time()*100000))
ret = requests.get(
    url=url,
    cookies=ret,
    data={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    },
                   )

ret.encoding='utf-8'
file=open('weibo.html','w')
file.write(ret.text)
file.close()



parttern = re.compile('<script>parent.FM.view\\((.*?)\\)</script>',flags=re.S)
parttern1 = re.compile('"html":(.*?)}',flags=re.S)
ret = parttern.findall(ret.text)



for i in ret:
    html = parttern1.findall(i)
    if html:
        html=html[0]
        dom_tree = etree.HTML(html.replace("\\",""))
        print(dom_tree)
        baseinfo = dom_tree.xpath("//div[@class='PCD_text_b PCD_text_b2']") #个人信息 浮动
        gfwinfo = dom_tree.xpath("//div[@class='PCD_counter']//strong") #关注,粉丝,点赞
        if gfwinfo:
            for gfw in gfwinfo:
                print(gfw.xpath("./text()")[0])
        if baseinfo:
            for titlepattern in baseinfo:
                print(titlepattern.xpath('.//h2/text()'))
                print(titlepattern.xpath('string(.//ul)').replace(" ","").replace('\n',"").replace('\r',"").replace('rn',''))
                print('=====')

