import matplotlib.pyplot as plt

def plot_file(id):
    textfile=open("ids/ID {}.txt".format(id),"r")
    lines=list()
    while True:
        line=textfile.readline()
        if line==None:
            break
        lines.append(line)

    x, y=zip(*lines)
    plt.plot(x, y)
    plt.show()
    
        
