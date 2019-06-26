
import glob,os
import pandas as pd


def Line_Exe(line):
   
    seconds = float(line.split(',')[1])*60*60+float(line.split(',')[2])*60
    time_stamp = ":".join([line.split(',')[1].split('.')[0],line.split(',')[2].split('.')[0]])
    return seconds, time_stamp

fs = glob.glob('*.csv')

Start = []
ends  = []

for f in fs:
    file = open(f)
    lines = file.readlines()
    line0 = lines[len(lines)-1]
    ends.append([f]+list(Line_Exe(line0)))
    line1 = lines[1]
    Start.append([f]+list(Line_Exe(line1)))

Start  = pd.DataFrame(Start,columns=['names','seconds','time'])
Start =  Start.sort_values(by=["seconds"],ascending=False)
ends = pd.DataFrame(ends,columns=['names','seconds','time'])
ends = ends.sort_values(by=["seconds"],ascending=False)

Start_val = Start.values.tolist()[0][2]
end_val = ends.values.tolist()[ends.shape[0]-1][2]


for f in fs:

    av_file = open(f)
    lines  = av_file.readlines()
    for s,line in enumerate(lines[1:]):

        if float(Start_val.split(':')[0])==float(line1.split(',')[1] ) and float(Start_val.split(':')[1])==float(line.split(',')[2]): 
            break
     
    for e,line in enumerate(lines[1:]):

        if float(end_val.split(':')[0])==float(line.split(',')[1] ) and float(end_val.split(':')[1])==float(line.split(',')[2]): 
            break

    #print s
    #print e

    if not os.path.exists('Corrected_data_files'):
        os.makedirs('Corrected_data_files')

    corrected_file = open(os.path.join('Corrected_data_files',f.replace('.csv','_corrected.csv')),'w')
    corrected_file.write(lines[0])
    corrected_lines = lines[1:]
    for l in corrected_lines[s:e]:
        corrected_file.write(l)