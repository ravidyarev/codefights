def bankRequests(accounts, requests):
    err=[]
    print(accounts)
    for i in range(0,len(requests)):
      print(requests[i])
      if requests[i][:2]=='tr':
        if len(accounts)==1:
          err.append(int('-'+str(requests.index(requests[i])+1)))
          return(err)
        b1p=requests[i].find(' ')
        b2p=requests[i][b1p+1:].find(' ')+b1p
        b3p=requests[i][b2p+2:].find(' ')+b2p
        print(requests[i][b3p+3:])
        print('***',b1p,b2p,b3p)
        from1=int(requests[i][b1p:b2p+1])-1
        to1=int(requests[i][b2p+2:b3p+2])-1
        amt1=int(requests[i][b3p+3:])
        print('a',from1,to1,amt1)
        if from1 >= len(accounts) or to1 >= len(accounts) :
          err.append(int('-'+str(requests.index(requests[i])+1)))
          return(err)
        if (accounts[from1]-amt1)<0:
          err.append(int('-'+str(requests.index(requests[i])+1)))
          return(err)
        accounts[from1]=accounts[from1]-amt1
        accounts[to1]=accounts[to1]+amt1
      elif requests[i][:2]=='wi':
        #print('b*',requests[i][9:10],requests[i][11:])
        b1p=requests[i].find(' ')
        b2p=requests[i][b1p+1:].find(' ')+b1p
        from1=int(requests[i][b1p:b2p+1])-1
        amt1=int(requests[i][b2p+2:])
        #print('b',from1,amt1)
        if from1 >= len(accounts):
          err.append(int('-'+str(requests.index(requests[i])+1)))
          return(err)
        if (accounts[from1]-amt1)<0:
          err.append(int('-'+str(requests.index(requests[i])+1)))
          return(err)
        accounts[from1]=accounts[from1]-amt1
      elif requests[i][:2]=='de':
        b1p=requests[i].find(' ')
        b2p=requests[i][b1p+1:].find(' ')+b1p
        to1=int(requests[i][b1p:b2p+1])-1
        amt1=int(requests[i][b2p+2:])
        print('c',to1,amt1)
        if to1 >= len(accounts) :
          err.append(int('-'+str(requests.index(requests[i])+1)))
          return(err)        
        accounts[to1]=accounts[to1]+amt1
      print(accounts)
    return(accounts)