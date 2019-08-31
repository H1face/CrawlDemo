from lxml import etree

html='''<html>
<head>
    <title>xpath test</title>
</head>
<body>
<div price="99.8">
    <div>
        <ul>
            <li>时间</li>
            <li>地点</li>
            <li>任务</li>
        </ul>
    </div>
    <div id='testid' data-h="first">
        <h2>这里是个小标题</h2>
        <ol>
            <li data="one">1</li>
            <li data="two">2</li>
            <li data="three">3</li>
        </ol>
        <ul>
            <li code="84">84</li>
            <li code="104">104</li>
            <li code="223">223</li>
        </ul>
    </div>
    <div>
        <h3>这里是H3的内容
            <a href="http://www.baidu.com">百度一下</a>
            <ul>
                <li>test1</li>
                <li>test2</li>
            </ul>
        </h3>
    </div>
    <div id="go">
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
            <li>6</li>
            <li>7</li>
            <li>8</li>
            <li>9</li>
            <li>10</li>
        </ul>
    </div>
</div>
</body>
</html>'''

# dom_tree = etree.HTML(html)
# ret = dom_tree.xpath('//li')
# for i in ret:
#     print(i.xpath('text()'))


html1='''
          <!--模块-->
                <div class="WB_cardwrap S_bg2">
                    <div class="PCD_text_b PCD_text_b2">
                        <div class="WB_cardtitle_b S_line2">
                            <div class="obj_name"><h2 class="main_title W_fb W_f14">基本信息<\/h2><\/div>
                        <\/div>
                        <div class="WB_innerwrap">
                            <div class="m_wrap clearfix">
                                <ul class="clearfix">
                                                                    <li class="li_1 clearfix"><span class="pt_title S_txt2">昵称：<\/span><span class="pt_detail">情感蚀<\/span><\/li>
                                                                                                                                    <li class="li_1 clearfix"><span class="pt_title S_txt2">所在地：<\/span><span class="pt_detail">浙江 杭州<\/span><\/li>
                                                                                                    <li class="li_1 clearfix"><span class="pt_title S_txt2">性别：<\/span><span class="pt_detail">女<\/span><\/li>
                                                                                                                                                                    <li class="li_1 clearfix"><span class="pt_title S_txt2">生日：<\/span><span class="pt_detail">2009年4月5日<\/span><\/li>
                                                                                                                                                                                                    <li class="li_1 clearfix">
                                        <span class="pt_title S_txt2">简介：<\/span>
                                                                                <span class="pt_detail">情感蚀<\/span>
                                                                            <\/li>
                                                                                                    <li class="li_1 clearfix">
                                        <span class="pt_title S_txt2">注册时间：<\/span>
                                        <span class="pt_detail">
                                                                                    2017-12-28                                                                                <\/span>
                                    <\/li>
                                                                <\/ul>
                            <\/div>
                        <\/div>
                    <\/div>
                <\/div>
                <!--\/\/模块-->

                <!--模块-->
                                <!--\/\/模块-->
                                <!--模块-->
                <div class="WB_cardwrap S_bg2">
                    <div class="PCD_text_b PCD_text_b2">
                        <div class="WB_cardtitle_b S_line2">
                            <div class="obj_name"><h2 class="main_title W_fb W_f14">工作信息<\/h2><\/div>
                        <\/div>
                        <div class="WB_innerwrap">
                            <div class="m_wrap clearfix">
                                <ul class="clearfix">


                                        <li class="li_1 clearfix"><span class="pt_title S_txt2">公司：<\/span>
                                                                                <span class="pt_detail">
                                            <a href="\/\/s.weibo.com\/user\/&work=%E6%83%85%E6%84%9F%E8%9A%80&from=inf&wvr=5&loc=infjob" target="_blank">情感蚀<\/a>
                                                                                          (2001 - 2002)
                                                                                          <br\/>
                                                                                         地区：北京 ，东城区<br\/>
                                                                                                                                     职位：情感蚀                                                                                    <\/span>
                                                                                <\/li>


                                <\/ul>
                            <\/div>
                        <\/div>
                    <\/div>
                <\/div>
                <!--\/\/模块-->
                                <!--模块-->
                                <div class="WB_cardwrap S_bg2">
                    <div class="PCD_text_b PCD_text_b2">
                        <div class="WB_cardtitle_b S_line2">
                            <div class="obj_name"><h2 class="main_title W_fb W_f14">教育信息<\/h2><\/div>
                        <\/div>
                        <div class="WB_innerwrap">
                            <div class="m_wrap clearfix">
                                <ul class="clearfix">
                                                                    <li class="li_1 clearfix"><span class="pt_title S_txt2">大学：<\/span>
                                    <span class="pt_detail">
                                                                            <a href="\/\/s.weibo.com\/user\/&school=%E5%8C%97%E4%BA%AC%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&from=inf&wvr=5&loc=infedu">北京信息科技大学<\/a> (2011年)                                        <br\/>
                                                                                                                <\/span>
                                    <\/li>
                                                                <\/ul>
                            <\/div>
                        <\/div>
                    <\/div>
                <\/div>
                <!--\/\/模块-->
                                <!--模块-->
                                <div class="WB_cardwrap S_bg2">
                    <div class="PCD_text_b PCD_text_b2">
                        <div class="WB_cardtitle_b S_line2">
                            <div class="obj_name"><h2 class="main_title W_fb W_f14">标签信息<\/h2><\/div>
                        <\/div>
                        <div class="WB_innerwrap">
                            <div class="m_wrap clearfix">
                                <ul class="clearfix">

                                    <li class="li_1 clearfix"><span class="pt_title S_txt2">标签：<\/span>
                                    <span class="pt_detail">
                                                                        <a target="_blank" node-type="tag" href="\/\/s.weibo.com\/user\/&tag=%E6%98%8E%E6%98%9F" class="W_btn_b W_btn_tag">
                                    <span class="W_arrow_bor W_arrow_bor_l"><i class="S_line3"><\/i><em class="S_bg2_br"><\/em>
                                    <\/span>
                                    明星                                    <\/a>
                                                                        <a target="_blank" node-type="tag" href="\/\/s.weibo.com\/user\/&tag=%E7%BE%8E%E6%90%AD" class="W_btn_b W_btn_tag">
                                    <span class="W_arrow_bor W_arrow_bor_l"><i class="S_line3"><\/i><em class="S_bg2_br"><\/em>
                                    <\/span>
                                    美搭                                    <\/a>
                                                                        <a target="_blank" node-type="tag" href="\/\/s.weibo.com\/user\/&tag=%E8%A1%97%E6%8B%8D" class="W_btn_b W_btn_tag">
                                    <span class="W_arrow_bor W_arrow_bor_l"><i class="S_line3"><\/i><em class="S_bg2_br"><\/em>
                                    <\/span>
                                    街拍                                    <\/a>
                                                                        <a target="_blank" node-type="tag" href="\/\/s.weibo.com\/user\/&tag=%E6%83%85%E6%84%9F" class="W_btn_b W_btn_tag">
                                    <span class="W_arrow_bor W_arrow_bor_l"><i class="S_line3"><\/i><em class="S_bg2_br"><\/em>
                                    <\/span>
                                    情感                                    <\/a>
                                                                        <\/span>
                                    <\/li>
                                <\/ul>
                            <\/div>
                        <\/div>
                    <\/div>
                <\/div>
                                <!--\/\/模块-->
    
'''

dom_tree = etree.HTML(html1.replace("\\",""))
i = dom_tree.xpath("//div[@class='PCD_text_b PCD_text_b2']")

for titlepattern in i:
    print(titlepattern.xpath('.//h2/text()'))
    print(titlepattern.xpath('string(.//ul)').replace(" ","").replace('\n',""))
    print('=====')


