def sec(a):
    t=int(a)
    day= t//86400
    hour= (t-(day*86400))//3600
    minit= (t - ((day*86400) + (hour*3600)))//60
    seconds= t - ((day*86400) + (hour*3600) + (minit*60))
    print( day, 'days' , hour,' hours', minit, 'minutes',seconds,' seconds')
    return a
sec(15000)