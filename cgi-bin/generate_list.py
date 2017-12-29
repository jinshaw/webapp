import glob
import test

import templates.yate as yate

data_files = glob.glob("C:/Users/jinxiao/PycharmProjects/webapp/data/*.txt")
athletes = test.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("Coach Kelly's list of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))