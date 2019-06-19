import glob 


def convert24(str1): 
 
    if str1.split(' ')[1]  == "AM" and str1.split(':')[0] == "12": 
        return "00" + ':'+str1.split(' ')[0].split(':')[1]+':'+str1.split(' ')[0].split(':')[2]           
   
    elif str1.split(' ')[1]  == "AM": 
        return str1.split(' ')[0]      
  
    elif str1.split(' ')[1] == "PM" and str1.split(':')[0] == "12": 
        return str1.split(' ')[0]  
          
    else: 
          
        return str(int(str1.split(':')[0]) + 12) + ':'+str1.split(' ')[0].split(':')[1]+':'+str1.split(' ')[0].split(':')[2] 
  
    
def return_time(in_file):

    file = open(in_file)
    lines = file.readlines()

    if 'PM' in lines[2].split(',')[0]:
        my_str = lines[2].split(',')[0].split(' ')[1]+' PM'

        return convert24(my_str)+' PM'

    else:
        return lines[2].split(',')[0].split(' ')[1]+' PM'

fs  = glob.glob('*.csv')


dic = {}


for f in fs:
    time_string = return_time(f)
    print f,'--->',(24*60*60)-float(time_string.split(' ')[0].split(':')[0])*60*60+float(time_string.split(' ')[0].split(':')[1])*60+float(time_string.split(' ')[0].split(':')[2])

 
    