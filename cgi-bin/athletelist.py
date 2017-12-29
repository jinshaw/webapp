def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs)=time_string.split(splitter)
    return (mins + '.' +secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
         return (sorted(set([sanitize(t) for t in self])))[0:3]

# if __name__=="__main__":
#     test=AthleteList('test y')
#     test.append('1.11')
#     print(test.top3())
#     test.extend(['2.22','3.33','4.44'])
#     print(test.top3())