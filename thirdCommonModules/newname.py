names={'熙':'光明,欢喜,和乐,兴旺,通"禧（xǐ）",福','赫':'显著,盛大','晟':'光明,旺盛,兴盛','琛':'珍宝','熠(yi)':'光耀,鲜明','灿':'光彩耀眼',
'贤':'有德行的,有才能的','珉(min)':'洁白如玉的石头','达':'通达,达到,实现','伦':'道理,义理','沐':'润泽,沐日浴月,沐泽,沐仁浴义','潼':'先是水名,后有地名,亦有高、盛大之意','梓':'引申为生机勃勃、茁壮成长、自强不息、生命力顽强','煜':'积极,阳光,灿烂,光明'}
for i,j in names.items():
    for x,y in names.items():
        if i != x:
            print('胡%s%s' % (i,x))
            print('[%s:%s],[%s:%s]' % (i,j,x,y))

