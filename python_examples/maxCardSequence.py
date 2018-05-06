def maxCardSequence(cards):
    seq=[]
    for i in range(0,len(cards)):
        seq.append(cards[i]%2)
    
    i=0
    j=0
    t=[]
    #print(seq)
    while i<len(seq)-1:
      if seq[i]!=seq[i+1]:
        j=j+1
      else:
        j=0
      i=i+1
      #print(i,len(seq))
      t.append(j)
    
    return(max(t))
    
print(maxCardSequence([1,2,3,1,4,7,5,6,7,8]) )   