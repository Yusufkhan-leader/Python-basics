def ortacha_ball(*ballar):
    yigindi=sum(ballar)
    ortacha=yigindi/len(ballar)
    return f"O'rtacha qiymat: {ortacha}"
print(ortacha_ball(5,6,9,10,0))
