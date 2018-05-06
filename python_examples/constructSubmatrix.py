def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    for i in range(0,len(rowsToDelete)):
        del matrix[rowsToDelete[i]]
    
    #print(matrix)
    x=sorted(columnsToDelete,reverse=True)
    for j in range(0,len(matrix)):
        for i in range(0,len(columnsToDelete)):
            del matrix[j][x[i]]
    #print(matrix)
    return(matrix)