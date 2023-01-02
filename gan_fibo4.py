# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:13:46 2022
@author: ramak
"""

import streamlit as st
import math
import pandas as pd
from datetime import datetime, timedelta,date
import numpy as np
from streamlit_autorefresh import st_autorefresh

m=st.sidebar.text_input('Option Range',value=5)
def optionchainbnf(symbol,expiry):
	import requests

	headers = {
	    'authority': 'api.stocksrin.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9',
	    'origin': 'https://www.stocksrin.com',
	    'referer': 'https://www.stocksrin.com/',
	    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
	}

	params = (
	    ('symbol', symbol),
	    ('expiry', expiry),
	    ('lastTimeStamp', ''),
	    ('forcedDataLoad', 'true'),
	)

	response = requests.get('https://api.stocksrin.com/srOptionChain/chain', headers=headers, params=params)
	return response.json()
def expirybnf(symbol):
	import requests

	headers = {
	    'authority': 'api.stocksrin.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9',
	    'origin': 'https://www.stocksrin.com',
	    'referer': 'https://www.stocksrin.com/',
	    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
	}

	params = (
	    ('symbol', symbol),
	)

	r = requests.get('https://api.stocksrin.com/srOptionChain/expiry', headers=headers, params=params)

	#NB. Original query string below. It seems impossible to parse and
	#reproduce query strings 100% accurately so the one below is given
	#in case the reproduced version is not "correct".
	# response = requests.get('https://api.stocksrin.com/srOptionChain/expiry?symbol=BankNifty', headers=headers)



	r=r.json()
	return r



#usdinr epiry
def usdinr(m):
    import requests
    
    headers = {
        'authority': 'api.stocksrin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.stocksrin.com',
        'referer': 'https://www.stocksrin.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Opera GX";v="91", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.72',
    }
    
    response = requests.get('https://api.stocksrin.com/currency/liveData/expiry', headers=headers)
    k=response.json()
    allof=[]
    
    for i in k:
        import requests
        
        headers = {
            'authority': 'api.stocksrin.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.stocksrin.com',
            'referer': 'https://www.stocksrin.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
        }
        
        params = {
            'symbol': 'USDINR',
            'expiry': i,
        }
        
        response = requests.get('https://api.stocksrin.com/currency/liveData/optionModel', params=params, headers=headers)
        #print(i)
        for j in response.json()['datums']:
            #print(j['strikePrice'])
            allof.append(j['strikePrice'])
        #print(i)
    allof=list(set(allof))
    allr={}
    for a in allof:
        allr[str(a)]={
            'CE':0,
            'PE':0,
            'CE_Change':0,
            'PE_Change':0
            
            }
    
    for i in k:
        import requests
        
        headers = {
            'authority': 'api.stocksrin.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.stocksrin.com',
            'referer': 'https://www.stocksrin.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
        }
        
        params = {
            'symbol': 'USDINR',
            'expiry': i,
        }
        
        response = requests.get('https://api.stocksrin.com/currency/liveData/optionModel', params=params, headers=headers)
        #print(i)
        for j in response.json()['datums']:
            if j['strikePrice'] in allof:
                #print(j.keys())
                if 'CE' in list(j.keys()):
                    #print(j['CE']['openInterest'])
                    #print(j['CE']['changeinOpenInterest'])
                    allr['{}'.format(j['strikePrice'])]['CE']=(allr['{}'.format(j['strikePrice'])]['CE']) +j['CE']['openInterest']
                    allr['{}'.format(j['strikePrice'])]['CE_Change']=(allr['{}'.format(j['strikePrice'])]['CE_Change']) +j['CE']['changeinOpenInterest']
                if 'PE' in list(j.keys()):
                    #print(j['PE']['openInterest'])
                    #print(j['PE']['changeinOpenInterest'])
                    allr['{}'.format(j['strikePrice'])]['PE']=(allr['{}'.format(j['strikePrice'])]['PE']) +j['PE']['openInterest']
                    allr['{}'.format(j['strikePrice'])]['CE_Change']=(allr['{}'.format(j['strikePrice'])]['PE_Change']) +j['PE']['changeinOpenInterest']
        
        #print()
        #break
        import math
        indexltp=(response.json()['underlyingValue'])*1000           
        mod=int(indexltp*100)%250
        #print(mod)
        if mod <25:
            atmstrike = int(math.floor(indexltp/250))*250/1000
        else:
            atmstrike = int(math.ceil(indexltp/250))*250/1000
        #print(atmstrike)
        allrl={}
        alk=[]
        for i in range(0,int(m)):
            alk.append(atmstrike+(i*.25))
            alk.append(atmstrike-(i*.25))
            #allrl[str(atmstrike+(i*.25))]=allr[str(atmstrike+(i*.25))]
            #allrl[str(atmstrike-(i*.25))]=allr[str(atmstrike-(i*.25))]]
        alk.sort()
        for i in alk:
            allrl[str(i)]=allr[str(i)]
        return allrl


def chaindata(symbol,expiry):
	import requests

	headers = {
	    'authority': 'api.stocksrin.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9',
	    'origin': 'https://www.stocksrin.com',
	    'referer': 'https://www.stocksrin.com/',
	    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
	}

	params = (
	    ('symbol', symbol),
	    ('expiry', expiry),
	    #('lastTimeStamp', '07-Oct-22 15:31:39'),
	    ('forcedDataLoad', 'true'),
	)

	response = requests.get('https://api.stocksrin.com/srOptionChain/chain', headers=headers, params=params)

	#NB. Original query string below. It seems impossible to parse and
	#reproduce query strings 100% accurately so the one below is given
	#in case the reproduced version is not "correct".
	# response = requests.get('https://api.stocksrin.com/srOptionChain/chain?symbol=BankNifty&expiry=2022-10-27&lastTimeStamp=07-Oct-22%2015:31:39&forcedDataLoad=true', headers=headers)
	k=response
	return k
def totaloi_bnf(symbol,r):
	global m
	#r=expirybnf(symbol)
	k=(optionchainbnf(symbol,r[0]))#.json()
	indexltp=k['srIndexQuote']['openValue']
	mod=int(indexltp)%50
	if mod <25:
	    atmstrike = int(math.floor(indexltp/100))*100
	else:
	    atmstrike = int(math.ceil(indexltp/100))*100
	#print(math.floor(k['srIndexQuote']['openValue']))
	#print(atmstrike)
	strikelvl=[]
	nextlvl={}
	for i in range(0,int(m)):
		if symbol=='Nifty':		
		    strikelvl.append(atmstrike + (i*50))
		    strikelvl.append(atmstrike - (i*50))
		else:
	    	strikelvl.append(atmstrike + (i*100))
	    	strikelvl.append(atmstrike - (i*100))
	strikelvl.append(atmstrike)
	print('strikelvl')
	print(strikelvl)


	for i in k['strikeDataModel']['strikes']:
	    #print(i)
	    if i['strikePrice'] in strikelvl:
	        nextlvl[str(i['strikePrice'])]={'CE':0,
	        'PE':0,
	        'CE_change':0,'PE_change':0}
	    #print(nextlvl)


	for expiry1 in r:

		k=chaindata(symbol,expiry1)
		#print(expiry)
		if k.status_code==200:
			#print(k)
			k=k.json()
			#print(k)
			for i in k['strikeDataModel']['strikes']:
				#print()
				if i['strikePrice'] in strikelvl:
					#print(i['strikePrice'])
					#print(nextlvl[str(i['strikePrice'])])
					#print(i)
					if str(i['strikePrice']) in list(nextlvl.keys()):
						if i['CE']==None:
							i['CE']={'oi':0
							,'oic':0
							}


						if (i['PE'])==None:
							i['PE']={'oi':0
							,'oic':0
							}
						nextlvl[str(i['strikePrice'])]={'CE': (nextlvl[str(i['strikePrice'])]['CE']+i['CE']['oi']),
						'PE':(nextlvl[str(i['strikePrice'])]['PE']+i['PE']['oi']),
						'CE_change':(nextlvl[str(i['strikePrice'])]['CE_change']+i['CE']['oic']),'PE_change':(nextlvl[str(i['strikePrice'])]['PE_change']+i['PE']['oic'])}
		return nextlvl



st_autorefresh(interval=45*1000, key="dataframerefresh")

st.sidebar.title("Fibo Level Maker")
#st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown("This application is a which gives Fibo entry levels")
def CurrencyDivider(select):
    if 'JPY' in select:
       return 1000
    elif 'XAU/USD' in select:
    	return 100
    elif 'USD' in select:
        return 100000
    elif 'INR' in select:
        return 10000
    else:
    	return 1

select=1
#st.sidebar.title("Pairs")
#select = st.sidebar.selectbox('Select a Pair', pairs, key='1')
#currency = st.sidebar.checkbox('Currency')
#st.json(response.json())


import plotly.express as px 


niftyoi = st.sidebar.checkbox('Nifty OI')
bankniftyoi = st.sidebar.checkbox('BankNifty OI')
usdinroi = st.sidebar.checkbox('USDINR OI')

if niftyoi:
	r=expirybnf('Nifty')
	nextlvl=totaloi_bnf('Nifty',r)
	#print(pd.DataFrame(nextlvl).T)
	allexp=st.multiselect('Select Nifty Expirys',r)
	print(allexp)
	if allexp:
		st.write("Custom NIFTY OI")
		nextlvl1=totaloi_bnf('Nifty',allexp)
		fig1=px.bar(pd.DataFrame(nextlvl1).T, orientation='h' ,text_auto=True,barmode='group')

		st.write(fig1)
	st.write("NIFTY TOTAL OI")
	fig=px.bar(pd.DataFrame(nextlvl).T, orientation='h' ,text_auto=True,barmode='group')

	st.write(fig)

if bankniftyoi:
	r=expirybnf('BankNifty')
	nextlvl=totaloi_bnf('BankNifty',r)
	#print(pd.DataFrame(nextlvl).T)
	#st.bar_chart(pd.DataFrame(nextlvl).T)
	allexp=st.multiselect('Select BankNifty Expirys',r)
	print(allexp)
	if allexp:
		st.write("Custom BANKNIFTY OI")
		nextlvl1=totaloi_bnf('BankNifty',allexp)
		fig1=px.bar(pd.DataFrame(nextlvl1).T, orientation='h' ,text_auto=True,barmode='group')

		st.write(fig1)
	st.write("BANKNIFTY TOTAL OI")
	fig=px.bar(pd.DataFrame(nextlvl).T, orientation='h' ,text_auto=True,barmode='group')
	st.write(fig)


if usdinroi:
	nextlvl=usdinr(m)
	#print(pd.DataFrame(nextlvl).T)
	#st.bar_chart(pd.DataFrame(nextlvl).T)
	fig=px.bar(pd.DataFrame(nextlvl).T, orientation='h' ,text_auto=True,barmode='group')
	st.write(fig)


import numpy as np
import plotly.graph_objects as go
#animals=['giraffes', 'orangutans', 'monkeys']
r=expirybnf('Nifty')
nextlvl=totaloi_bnf('Nifty',r)
k=(pd.DataFrame(nextlvl).T)
k=k.iloc[::-1]
fig = go.Figure()

fig.add_trace(go.Bar(name='CE %', x=k.index, y=k.CE_change ,offsetgroup=0,base=k.CE,marker_color = '#83C9FF'))
fig.add_trace(go.Bar(name='CE', x=k.index, y=k.CE ,offsetgroup=0,marker_color='#0068C9'))

fig.add_trace(go.Bar(name='PE', x=k.index, y=k.PE,offsetgroup=1,marker_color='#FF2B2B'))
fig.add_trace(go.Bar(name='PE %', x=k.index, y=k.PE_change,offsetgroup=1,base=k.PE,marker_color='#FFABAB'))
# Change the bar mode
#fig.update_layout(barmode='stack')
st.write(fig)
# Plot!
#st.plotly_chart(fig, use_container_width=True ,orientation='h')
