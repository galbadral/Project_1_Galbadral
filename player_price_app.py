import streamlit as st
import numpy as np
import pandas as pd
import time

df = pd.read_csv("top_players_stats_country_code.csv")

st.title("Football: Market price vs Stats")

tab1, tab2 = st.tabs(["Player comparison","Country comparison"])

with tab1:

    coll1, coll2, coll3= st.columns([2,1,2])

    option1 = coll1.selectbox(
        'Your first player',
        (df['names']))

    option2 = coll3.selectbox(
        'Your second player',
        (df['names']))



    for i in range(len(df)):
        if df['names'][i]== option1:
            index1=i
        if df['names'][i]== option2:
            index2=i

    link1= 'https://countryflagsapi.com/png/'+df['code'][index1]
    link2='https://countryflagsapi.com/png/'+df['code'][index2]

    coll2.image("VS.jpg")

    coll1.image(link1,caption=df['countries'][index1])
    coll3.image(link2,caption=df['countries'][index2])
    
    col_1, col_2, col_3= st.columns([2,2,1])
    
    
    col1, col2, col3, col4, col5= st.columns(5)

    col3.subheader("Price")
    col2.subheader(df['prices'][index1])
    col4.subheader(df['prices'][index2])


    
    col3.subheader("Goals")
    col2.subheader(df['goals'][index1])
    col4.subheader(df['goals'][index2])
    
    
    gc1=df['goals'][index1]+df['assists'][index1]
    gc2=df['goals'][index2]+df['assists'][index2] 
    
    col3.write("Goal contribution")
    col2.write(str(gc1))
    col4.write(str(gc2))

    
    col3.write("Games")
    col2.write(str(df['current_matches'][index1]))
    col4.write(str(df['current_matches'][index2]))
    
    col3.write("Ranked at")
    col2.write(str(df['ranks'][index1]))
    col4.write(str(df['ranks'][index2]))
    


    p1 = ''.join(x for x in df['prices'][index1] if x.isdigit())
    p2 = ''.join(x for x in df['prices'][index2] if x.isdigit())
    
    if gc1!=0:
        p_per_gc1=float(p1)/gc1
        formatted_float1 = "{:.2f}".format(p_per_gc1/100)
        
        col2.subheader("€"+str(formatted_float1)+"m")
    else:
        col2.subheader("No Goal contribution")
        
    if gc2!=0:
        p_per_gc2=float(p2)/gc2
        formatted_float2 = "{:.2f}".format(p_per_gc2/100)
        
        col4.subheader("€"+str(formatted_float2)+"m")
        
    else:
        col4.subheader("No Goal contribution")
            
    col3.write("Price per Goal contributions")
    
    
    
    total_p_per_gc=0
    for i in range(len(df)):
        gc=df['goals'][i]+df['assists'][i]
        p = ''.join(x for x in df['prices'][i] if x.isdigit())
        if gc!=0:
            p_per_gc=int(p)/int(gc)
            total_p_per_gc =total_p_per_gc + p_per_gc 
        else:
             pass
    st.caption("Average Price per goal contribution is at €"+str(int((total_p_per_gc)/100)/len(df))+"m")
with tab2:
    coll1, coll2, coll3= st.columns([2,1,2])
    
    country_list=df['countries'].unique()

    option1 = coll1.selectbox(
        'Your first country',
        (country_list))

    option2 = coll3.selectbox(
        'Your second country',
        (country_list))



    for i in range(len(df)):
        if df['countries'][i]== option1:
            index1=i
        if df['countries'][i]== option2:
            index2=i

    link1= 'https://countryflagsapi.com/png/'+df['code'][index1]
    link2='https://countryflagsapi.com/png/'+df['code'][index2]

    coll2.image("VS.jpg")

    coll1.image(link1,caption=df['countries'][index1])
    coll3.image(link2,caption=df['countries'][index2])
    
    col_1, col_2, col_3= st.columns([2,2,1])
    
    if col_2.button('   COMPARE  '):
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
    
        eleven_counter1=0
        eleven_counter2=0
        names1=[]
        names2=[]
        price1=[]
        price2=[]
        tprice1=0
        tprice2=0
        for i in range(len(df)):
            if df['countries'][i]==option1 and eleven_counter1<11:
                names1.append(df['names'][i])
                eleven_counter1=eleven_counter1+1
                price1.append(int(''.join(x for x in df['prices'][i] if x.isdigit()))/100)
                tprice1 += int(''.join(x for x in df['prices'][i] if x.isdigit()))

            if df['countries'][i]==option2 and eleven_counter2<11:
                names2.append(df['names'][i])
                eleven_counter2=eleven_counter2+1
                price2.append(int(''.join(x for x in df['prices'][i] if x.isdigit()))/100)
                tprice2 += int(''.join(x for x in df['prices'][i] if x.isdigit()))

        if eleven_counter1<11:
            tprice1+= 1700*(11-eleven_counter1)
            for i in range(11-eleven_counter1):
                names1.append('Unknown player')
                price1.append(17)
        if eleven_counter2<11:
            tprice2+= 1700*(11-eleven_counter2)
            for i in range(11-eleven_counter2):
                names2.append('Unknown player')
                price2.append(17)
        data1={}
        data1['name']=names1
        data1['price']=price1

        data2={}
        data2['name']=names2
        data2['price']=price2

        coll_1, coll_2, coll_3= st.columns([2,1,2])

        coll_2.write("TOP PLAYERS LIST")
        coll_1.dataframe(data1)
        coll_3.dataframe(data2)

        colll_1, colll_2, colll_3= st.columns([2,1,2])

        colll_2.subheader("TOTAL PRICE")
        colll_1.subheader("€"+str(tprice1/100)+"m")
        colll_3.subheader("€"+str(tprice2/100)+"m")

        st.caption("Unknown players gets have minimum price from the data")
    