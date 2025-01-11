def same_time (time1, time2):
      return time1.tm_year == time2.tm_year and \
             time1.tm_mon == time2.tm_mon and \
             time1.tm_mday == time2.tm_mday and \
             time1.tm_hour == time2.tm_hour and \
             time1.tm_min == time2.tm_min and \
             time1.tm_sec == time2.tm_sec