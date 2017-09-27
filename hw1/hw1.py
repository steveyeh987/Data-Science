import sys
import ssl
import urllib
import matplotlib.pyplot as plt



def Parse_File(link):
    context = ssl._create_unverified_context()
    f = urllib.request.urlopen(link, context=context)
    data = f.read().decode('utf-8').split('\n')
    e = [i.split(',') for i in data[2:7]]
    a = [i.split(',') for i in data[8:11]]
    w = [i.split(',') for i in data[12:15]]
    
    E = ['Education level']
    A = ['Average monthly income']
    W = ['Working environment']
    lst = [E, A, W]
    
    for index, cl in enumerate([e, a, w]):
        total_pop = 0.0
        x_tick = []
        M = []
        F = []
        T = []
        Non_smoke = []
        
        for row in cl:
            x_tick.append(row[0])
            temp = list(map(float, row[1:]))
            M.append(temp[1])
            F.append(temp[3])
            T.append(float("{0:.1f}".format((temp[0]*temp[1]+temp[2]*temp[3])/(temp[0]+temp[2]))))
            Non_smoke.append(temp[0]*(1-temp[1]/100)+temp[2]*(1-temp[3]/100))
            total_pop += (temp[0]*(1-temp[1]/100)+temp[2]*(1-temp[3]/100))
        Non_smoke = [float("{0:.1f}".format(i/total_pop)) for i in Non_smoke]
        lst[index].extend([x_tick, M, F, T, Non_smoke])
        
    return E, A, W


def Data_Class(s):
    assert s in ['E', 'A', 'W'], "Cannot find class type {} !".format(s)
    data = []
    
    if s == 'E':
        data = E
    elif s == 'A':
        data = A
    else:
        data = W
        
    return data


def Chart(s, data):
    assert s in ['l', 'b', 'p'], "Cannot find chart type {} !".format(s)
    n = len(data[1])
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_xticks(range(n))
    ax.set_xticklabels(data[1], ha='center')
    ax.tick_params(labelsize=9)
    
    if s == 'l':
        ax.plot(range(n), data[2], marker='s', label='Male')
        ax.plot(range(n), data[3], marker='o', label='Female')
        ax.plot(range(n), data[4], marker='^', label='Total') 
        for pop in data[2:5]:
            for i, j in zip(range(n), pop):
                ax.text(i+0.1, j+0.1, str(j), ha='center', va='bottom', fontsize=10)
        ax.set_title("Smoking Percentage vs {}".format(data[0]), fontsize=11)  		
        ax.set_xlabel(data[0], fontsize=9)
        ax.set_ylabel('Smoking Percentage (%)', fontsize=9)
        ax.set_xlim([-0.5, n-0.5])
        plt.legend(loc='upper right', prop={"size":10})
        plt.show()
    
    elif s == 'b':
        width=0.15
        rects1 = ax.bar([i-1.5*width for i in range(n)], data[2], width=width, label='Male', color='b')
        rects2 = ax.bar([i-0.5*width for i in range(n)], data[3], width=width, label='Female', color='r')
        rects3 = ax.bar([i+0.5*width for i in range(n)], data[4], width=width, label='Total', color='y') 
        for rects in [rects1, rects2, rects3]:
            for rect in rects:
                    h = rect.get_height()
                    ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, h,
                            ha='center', va='bottom', fontsize=10)
        ax.set_title("Smoking Percentage vs {}".format(data[0]), fontsize=11)      	
        ax.set_xlabel(data[0], fontsize=9)
        ax.set_ylabel('Smoking Percentage (%)', fontsize=9)
        ax.set_xlim([-0.5, n-0.5])
        plt.legend(loc='upper right', prop={"size":10})
        plt.show()        
    
    else:
        ax.pie(data[5], labels=data[1], autopct='%1.1f%%',)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title("Proportion of different {} in non-smoking population".format(data[0]), fontsize=11, y=1.08)
        plt.show()



if __name__ == '__main__':
    link = "https://ceiba.ntu.edu.tw/course/481ea4/hw1_data.csv"
    E, A, W = Parse_File(link)
    
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            arg = arg[1:]
            cl = Data_Class(arg[0])
            Chart(arg[1], cl)
        
