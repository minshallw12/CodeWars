def past(h, m, s):
    hour = h*3600*1000;
    min = m*60000;
    sec = s*1000;
    return hour + min + sec;