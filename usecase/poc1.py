import easyquotation

def getdata(stock_code):

    # 新浪 ['sina'] 腾讯 ['tencent', 'qq'] 
    q1 = easyquotation.use('sina') 

    q2 = easyquotation.use('tencent') 

    q3 = easyquotation.use('hkquote') 

    # 支持直接指定前缀，如 'sh000001'
    r1 = q1.real(stock_code) 
    r2 = q2.real(stock_code) 
    r3 = q3.real(stock_code) 

    print( 'sina ==>', r1 )
    print( 'tencent ==>', r2 )
    print( 'hkquote ==>', r3 )


    #r3 = q3.etfindex(index_id="513050", 
    #            min_volume=0, 
    #            max_discount=None, 
    #            min_discount=None)


    #print( u'中概互联指数 ==>', r3 )

