import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import math
#in the data folder we have two csv file, one with all the codes and the other with only the available ones

def calculate_percentage(Available_Codes,All_Codes):
    """
    This function calculate the percentage of available codes
    out of all codes.

    We suppose that each code in codes_disponibles are in tous_les_codes.

    :return: percentage of available codes
    """

    # the file of available codes contains a lot of duplicate
    # so we need to remove all the duplicate codes
    # then check if each available code is in all codes to calculate the percentage
    
    Available_codes_no_duplicates=Available_Codes["codes"].drop_duplicates()
    AV_size=len(Available_codes_no_duplicates) #Available codes size
    AL_size=len(All_Codes)# All codes size

    #calculate the percentage
    return (AV_size*100)/AL_size

def frequency(code,Available_Codes):
    """
    Calculate the frequency of a given available code

    :param code: an available code 
    :param Available_Codes: DataFrame of available codes
    :return: frequency of code
    """
    #check if code exist in our dataframe
    assert code in Available_Codes.values, 'Error the code doesnt exist in the DataFrame'
    # count all the occurrences of code in the file
    # the value_counts method display for each unique code its occurrences
    # so we only have to search the occurency of code which is a key
    occ= Available_Codes.value_counts()[code]
    
    # divide the number of occurrences of code on all available codes
    data_size=len(Available_Codes)
    return occ/data_size

def rand_available(Available_Codes):
    """
    This function return a random number from the values of the DataFrame Available_Codes
    :param Available_Codes: DataFrame of available codes
    :return: random number
    """
    return random.choice(Available_Codes.values)[0]


def display_frequency(tab,Available_Codes,path="images/frequency.png"):
    """
    display a graph which compares the frequency of 5 available codes
    :param tab: a list of 5 available codes
    :param path: By default its "images/frequency.png" where the plot will be saved 

    """
    # create a dictionnary with keys as the  availables codes and their values as their frequency
    d=dict()
    tab.sort()
    for i in range(len(tab)):
        d[tab[i]]=frequency(tab[i],Available_Codes)
    
    #display the plot 
    display_plot(list(d.keys()),list(d.values()),path)
    
    

def display_plot(height,bars,path):
    """
    This function create a plot with height as y-axis and bars as x-axis
    :param height: a list of which will be displayed as y-axis
    :param bars: a list of which will be displayed as x-axis
    :param path: a path where the plot will be saved 
    :return:
    """
    y_pos = np.arange(len(bars))

    # Create bars and choose color
    plt.bar(y_pos, bars, color=(0.5,0.1,0.5,0.6))

    #add title 
    plt.title("Frequency of 5 available codes")
    plt.xlabel("available codes")
    plt.ylabel("frequency")

    # Create names on the x-axis
    plt.xticks(y_pos, height)

    #save plot
    plt.savefig(path,dpi=400)
    # Show graphic
    #plt.show()

def display_statistique_parameters(Available_Codes):
    """
    """
    # Calculate the frequency of each value of Available_codes
    fre=Available_Codes.value_counts()

    #search for the maximum of the frequencies of the available codes
    #Max=max(list(fre)) # either we try to call the function max on the list of dataFrame 

    # or since the resulting object from value_counts is descending order so that
    # the first element is the most frequently-occuring element, we can simply choose the first element as the maximum 
    Max=list(fre)[0]

    #search for the minimum of the frequencies of the available codes
    Min=list(fre)[-1] # with the same logic the minimum is the last one

    #search for the average of the frequencies of the available codes
    #two methods:
    # - Average= fre.mean() or,
    
    Average=(sum(list(fre))/len(list(fre)))
    #search for the median of the frequencies of the available codes
    #two methods:
    # - fre.median()
    Median=median(list(fre))

    #display the plot
    height=[Max,Min,Average,Median]
    x=["Maximum","Minimum","Average","Median"]
    plt.bar(x,height,tick_label=x,color=(0.5,0.1,0.5,0.6))
    #add title 
    plt.title("Statistiques parameters")
    plt.xlabel("")
    plt.ylabel("")

    plt.savefig("images/statistiques.png",dpi=400)


def median(l):
    """
    this function tries to find the median of the list given as a parameter
    :param l: list of numbers
    :return: the median of the list
    """
    assert len(l)!=0, "Can't calculate median, list empty"
    l.sort() #sort the list
    middle=math.floor(len(l)/2) # search the middle index and convert it so it will be always an integer
    return l[middle] 

def main():
    #open both csv files  so our functions are independent of the files

    Available_Codes=pd.read_csv("data/codes_disponibles.csv", usecols=["codes"])
    All_Codes=pd.read_csv("data/tous_les_codes.csv", usecols=["codes"])

    print("The percentage of available codes out of all codes is :", calculate_percentage(Available_Codes, All_Codes) ,"\n")
    
    #we use the rand_available function to have a random number to test the frequency function
    rand_code=rand_available(Available_Codes)
    print("the frequency of the code ", rand_code, " is :", frequency(rand_code,Available_Codes) ,"\n")

    print("The graph that compares the frequency of 5 available codes is available at images/frequency.png ")
    
    # create a list of 5 random available codes 
    tab=[ rand_available(Available_Codes) for i in range(5) ]
    display_frequency(tab,Available_Codes)

    print("The graph that display the statistique parameter is available at images/statistiques.png")
    display_statistique_parameters(Available_Codes)


if __name__ == "__main__":
    main()