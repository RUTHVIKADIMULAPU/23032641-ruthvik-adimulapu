#!/usr/bin/env python
# coding: utf-8

# FUNDAMENTALS OF DATA SCIENCE

# SMALL PROJECT
# Coding assignment - Semester B 2023/24 (30 points, 30%)

# NAME: RUTHVIK ADIMULAPU

# STUDENT ID :23032641

# In[172]:


#IMPORTING NUMPY,PANDAS AND MATPLOTLIB

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[173]:


#Functions to read the data from the given CSV files
def read_data():
    #Read the 2020 exam data from the CSV file
    df_2020=pd.read_csv("2020input1.csv",header=None,sep='\s+',names=["Interval Start","Interval end","Count"])
    
    #Read the 2024 exam data from the CSV file
    df_2024=pd.read_csv("2024input1.csv",header=None,names=["Grade"])
    
    return df_2020,df_2024


# In[174]:


df_2020


# In[175]:


df_2024


# In[176]:


#Function to create histograms for the exam grades
def create_histograms(df_2020,df_2024):
    #Create histogram for 2020 exam
    plt.hist(df_2020["Interval Start"],bins=len(df_2020),weights=df_2020["Count"],alpha=0.5,label="2020 Exam")
    
    #Create histogram for 2024 exam
    plt.hist(df_2024["Grade"],bins=30,alpha=0.5,label="2024 Exam")
    
    #Add labels,legend and title to the plot
    plt.legend()
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Exam Grades")
    plt.grid(True,linestyle='--',color='gray',alpha=0.3)


# In[177]:


#Function to calculate mean values and standard deviations
def calculate_statistics(df_2020,df_2024):
    #Filter out rows with zero weights in the the 2020 dataset
    df_2020_filtered=df_2020[df_2020["Count"]!=0]
    
    #Calculate the mean and standard deviation for the 2020 distribution
    mean_2020 = np.average(df_2020_filtered["Interval Start"],weights=df_2020_filtered["Count"])
    std_dev_2020 = np.sqrt(np.average((df_2020_filtered["Interval Start"]-mean_2020)**2,weights=df_2020_filtered["Count"]))
    
    #Calculate the mean and standard deviaion for the 2024 distribution
    mean_2024=df_2024["Grade"].mean()
    std_dev_2024=df_2024[ "Grade"].std()
    
    return mean_2020,std_dev_2020,mean_2024,std_dev_2024


# In[178]:


#Function to calculate value V based on the proportion of students with the grade of 70% or higher in the 2024 exam
def calculate_V(df_2024):
    V=(df_2024["Grade"] >= 70).mean() #proportion of students with grade of 70 or higher
    return V


# In[179]:


#Function to plot the graph and save it
def plot_and_save(mean_2020,std_dev_2020,mean_2024,std_dev_2024,V):
    #Plot the histogram and add text with calculated values
    plt.text(0.04, 0.90, f"V: {V:.2f}\nStudent ID: 23032641", transform=plt.gca().transAxes)
    plt.text(0.04,0.70,f"Mean(2020):{mean_2020:.2f}\nSD(2020):{std_dev_2020:.2f}",transform=plt.gca().transAxes)
    plt.text(0.04,0.80,f"Mean(2024):{mean_2024:.2f}\nSD(2024):{std_dev_2024:.2f}",transform=plt.gca().transAxes)
    
    #Save the plot as a PNG file
    plt.savefig("23032641.png")
    plt.show()
    


# In[180]:


#Main function to execute the code written

def main():
    #Read the data from CSV files
    df_2020,df_2024=read_data()
    
    #Create histograms for the exam grades
    create_histograms(df_2020,df_2024)
    
    #Calculate mean values and standard deviations
    mean_2020,std_dev_2020,mean_2024,std_dev_2024=calculate_statistics(df_2020,df_2024)
    
    #Calculate value of V
    V=calculate_V(df_2024)
    
    #plot the graph and save it
    plot_and_save(mean_2020,std_dev_2020,mean_2024,std_dev_2024,V)
   
#Execute the main function if the script is run directly
if __name__=="__main__":
    main()


# In[ ]:




