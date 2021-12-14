duration = 400153
if duration < 60:
    print(duration, 'second')
elif 60 <= duration < 3600:
    m = duration // 60
    s = duration % 60
    print(m, 'min',  s, 'sec')
elif 3600 <= duration < 86400:
    h = duration // 3600
    m = duration % 3600//60
    s = ((duration % 3600) % 60)
    print(h, 'hour', m, 'minute', s, 'second')
elif duration >= 86400:
    d = duration // 86400
    h = duration % 86400 // 3600
    m = (duration % 86400) % 3600 // 60
    s = ((duration % 86400 % 3600) % 60) % 60
    print(d, 'days', h, 'hour', m, 'minute', s, 'second')




