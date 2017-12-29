import pickle

from athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temple = data.strip().split(',')
        return (AthleteList(temple.pop(0),temple.pop(0),temple))
    except IOError as ioerr:
        print('file error:' + str(ioerr))
        return None

def put_to_store(files_list):
    all_athletes={}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name]=ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    return all_athletes

def get_from_store():
    all_athletes={}
    try:
        with open('athletes.pickle','rb')as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return all_athletes

# if __name__=="__main__":
#        the_files = ['sarah.txt','james.txt','mikey.txt','julie.txt']
#        data = put_to_store(the_files)
#        for each_data in data:
#            print(data[each_data].name +"' 's fastest times are '"+ str(data[each_data].top3()))



