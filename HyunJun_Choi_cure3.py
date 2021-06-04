import sys
import heapq
from heapq import heappush, heappop
import numpy as np
import collections

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def calDistance(callocalnewClusterCand,calelem,callocaltotalPoint):
    
    heapCal=[]
    
    if type(callocalnewClusterCand)==type(list()):
        callocalnewClusterCand=flatten(callocalnewClusterCand)
        
    if type(calelem)==type(list()):
        calelem=flatten(calelem)    
    
#     flat_localnewClusterCand = [item for sublist in localnewClusterCand for item in sublist]
    if type(calelem)==type(int()):
        for elem in callocalnewClusterCand:
            
#             if elem==0:
#                 print(0)
            
            distCal=np.sum((callocaltotalPoint[elem-1][1] - callocaltotalPoint[calelem-1][1]) **2)
            pairIndex=[elem,calelem]
            dataCal=[distCal,str(pairIndex)]
            heappush(heapCal, dataCal)
    
    if type(calelem)==type(list()):
        for elem in callocalnewClusterCand:
            for inElem in calelem:
            
#                 if elem==0:
#                     print(0)
            
                distCal=np.sum((callocaltotalPoint[elem-1][1] - callocaltotalPoint[inElem-1][1]) **2)
                pairIndex=[elem,inElem]
                dataCal=[distCal,str(pairIndex)]
                heappush(heapCal, dataCal)
                
    closestdistA=heappop(heapCal)   
    return closestdistA[0]

def addPairsForNewCluster(localnewClusterCand,localclusterSet,localtotalPoint):
    

    totalData=[]
    for elem in localclusterSet:
        
        dist=calDistance(localnewClusterCand,elem,localtotalPoint)
#         dist=1
        pair=[localnewClusterCand,elem] 
#         pair=[elem,localnewClusterCand]        
        data=[dist,str(pair)]
        totalData.append(data)
        
    return totalData

# def maxDis(subrepresentatives,subsubtotalPoint,subindN):
#     
#     curre=np.inf*-1
#     if len(subrepresentatives)==1:
#         
#         for indSUB in range(len(subsubtotalPoint)):
#             
#             mdist=np.sum((subsubtotalPoint[indSUB][1] - subsubtotalPoint[subrepresentatives[0]-1][1]) **2)
#             if mdist>curre:
#                 curre=mdist
#                 pointFartest=subsubtotalPoint[indSUB][0]
#                 
#     if len(subrepresentatives)!=1:
#         checkMinIsMax=1
#         
#         mheap=[]
#         anmheap=[]
#         for indTPoint in range(len(subsubtotalPoint)):
#             mheap=[]
#             for indRe in range(len(subrepresentatives)):
#                 if subsubtotalPoint[indTPoint][0] not in subrepresentatives:
#                     mdist=np.sum((subsubtotalPoint[indTPoint][1] - subsubtotalPoint[subrepresentatives[indRe]-1][1]) **2)
#                     mpoint=[subsubtotalPoint[indTPoint][0],subrepresentatives[indRe]]
#                     mdata=[mdist,str(mpoint)]
#                     heappush(mheap, mdata)
#             
#             if mheap !=[]:
#                 mminDis=heappop(mheap)
#             
#             for anindTPoint in range(len(subsubtotalPoint)):
#                 
# #                 anmheap=[]
#                 
#                 if subsubtotalPoint[indTPoint][0]!=subsubtotalPoint[anindTPoint][0]:
#                     for reindRe in range(len(subrepresentatives)):
#                         if subsubtotalPoint[anindTPoint][0] not in subrepresentatives:
#                             anmdist=np.sum((subsubtotalPoint[anindTPoint][1]-subsubtotalPoint[subrepresentatives[reindRe]-1][1]) ** 2)
#                             anmpoint=[subsubtotalPoint[anindTPoint][0],subsubtotalPoint[subrepresentatives[reindRe]-1][0]]
#                             anmdata=[anmdist,str(anmpoint)]
#                             heappush(anmheap, anmdata)
#                     
#                     if anmheap!=[]:
#                         maxAother=heapq.nlargest(1, anmheap)
#                         
# #                         print(maxAother)
# #                         if maxAother==[[3.591978965474, '[65, 66]']]:
# #                             print('')
#                         if mminDis[0]>=maxAother[0][0]:
#                             checkMinIsMax=0
#                             tempP=eval(mminDis[1])
#                             pointFartest=tempP[0]
# #                             if pointFartest==93:
# #                                 print('')
#         
# #         if checkMinIsMax==0:
# #             print('')        
#     return pointFartest


def maxDisVer2(subrepresentatives,eachsubclusterSetIndL,subsubtotalPoint,subindN):
    
#     if sorted(subrepresentatives)==sorted(eachsubclusterSetIndL):

    
    curre=np.inf*-1
    
    subClusterPoints=flatten(eachsubclusterSetIndL)
    
    if len(subrepresentatives)==1:
        for tSin in subClusterPoints:
            if subsubtotalPoint[tSin-1][0]!=subrepresentatives[0]:
                 
                mdist=np.sum((subsubtotalPoint[tSin-1][1] - subsubtotalPoint[subrepresentatives[0]-1][1]) **2)
                if mdist>curre:
                    curre=mdist
                    pointFartest=subsubtotalPoint[tSin-1][0]


        #########################################        
#     for indSUB in range(len(subsubtotalPoint)):
#              
#         if subsubtotalPoint[indSUB][0] in subClusterPoints:
#             if subsubtotalPoint[indSUB][0]!=subrepresentatives:
#          
#                 mdist=np.sum((subsubtotalPoint[indSUB][1] - subsubtotalPoint[subrepresentatives[0]-1][1]) **2)
#                 if mdist>curre:
#                     curre=mdist
#                     pointFartest=subsubtotalPoint[indSUB][0]
                    
                    
                    
    tema=[]     
               
                        
    if len(subrepresentatives)!=1:
        checkMinIsMax=1
        
        mheap=[]
        anmheap=[]
        
        
        for tSin in subClusterPoints: 
            
            mheap=[]
            
            if tSin not in subrepresentatives:
                
                for tsubInd in subrepresentatives:
                    
                    mdist=np.sum((subsubtotalPoint[tSin-1][1] - subsubtotalPoint[tsubInd-1][1]) **2)
                    mpoint=[tSin,tsubInd]
                    mdata=[mdist,str(mpoint)]
                    heappush(mheap, mdata)    
        
        
        
        
        ######################################################
#         for indTPoint in range(len(subsubtotalPoint)):
#             
#             mheap=[]
#             
#             if subsubtotalPoint[indTPoint][0] in subClusterPoints:
#                 
#             
#                 for indRe in range(len(subrepresentatives)):
#                     if subsubtotalPoint[indTPoint][0] not in subrepresentatives:
#                         mdist=np.sum((subsubtotalPoint[indTPoint][1] - subsubtotalPoint[subrepresentatives[indRe]-1][1]) **2)
#                         mpoint=[subsubtotalPoint[indTPoint][0],subrepresentatives[indRe]]
#                         mdata=[mdist,str(mpoint)]
#                         heappush(mheap, mdata)    
        ########################################################





#                 if mheap==[]:
#                     print('1')
            

                        
                if mheap!=[]:
                    minTemp=heappop(mheap)
                    
                    tema.append(minTemp[1])
                    
                    heappush(anmheap,minTemp)
                
                 
#                 
#                 maxTemp=heapq.nlargest(1, mheap)
#                 heappush(anmheap,maxTemp)
        
        pointFartestTemp=heapq.nlargest(1, anmheap)
        pointFartestTemp=eval(pointFartestTemp[0][1])
        pointFartest=pointFartestTemp[0]       
        
    return pointFartest

def markingRepresentatives(subclusterSet,subtotalPoint,subn):
    
    curXCoordSmall=np.inf
    point=0
    subeachRepresentativesSet=[]
    testRe=[]
  
    
    for indL in range(len(subclusterSet)):
        
        
        flattenEachCluster=flatten(subclusterSet[indL])
        curXCoordSmall=np.inf
        
        #First point chosen
        #Find smallest X 
        for indSub in range(len(subtotalPoint)):
            for indFlat in range(len(flattenEachCluster)):
                if subtotalPoint[indSub][0]==flattenEachCluster[indFlat]:
                    # X coordinate
#                     print('')
                    if  subtotalPoint[indSub][1][0] < curXCoordSmall:
                              
                         curXCoordSmall=subtotalPoint[indSub][1][0]
                         point=flattenEachCluster[indFlat]
                         
#         for indFlat in range(len(flattenEachCluster)):
# 
#             if  subtotalPoint[flattenEachCluster[indFlat]-1][0] < curXCoordSmall:
#                      
#                  curXCoordSmall=subtotalPoint[flattenEachCluster[indFlat]-1][0]
#                  point=flattenEachCluster[indFlat]                   
                        
                         

        curYCoordSmall=subtotalPoint[point-1][1][1]                
                     
        for indFlat in range(len(flattenEachCluster)):
            if flattenEachCluster[indFlat]!=point:
                if subtotalPoint[flattenEachCluster[indFlat]-1][1][0]==curXCoordSmall:
                    if subtotalPoint[flattenEachCluster[indFlat]-1][1][1]<curYCoordSmall:
                        point=flattenEachCluster[indFlat]
                        curYCoordSmall=subtotalPoint[flattenEachCluster[indFlat]-1][1][1]
                            
        representatives=[]
        representatives.append(point)       
        
                         
        
        if type(subclusterSet[indL])==type(list()):
            
            if len(subclusterSet[indL])!=1:
            
                for indN in range(1,subn):    
            #         representatives.append(maxDis(representatives,subtotalPoint,indN))
                    
                    
                    
                    if representatives!=subclusterSet[indL]:
                        representatives.append(maxDisVer2(representatives,subclusterSet[indL],subtotalPoint,indN))
                        
                        if type(representatives)==type(list()) and type(subclusterSet[indL])==type(list()):
                            sortedRepre=sorted(representatives)
                            sortedSubClusterSet=sorted(flatten(subclusterSet[indL]))
                            
                            if sortedRepre==sortedSubClusterSet:
                                break
                        
                
                subeachRepresentativesSet.append(str(representatives))   
                testRe.append(representatives)
#             print('')
        
#         if (type(subclusterSet[indL])==type(int())):
        else:
            subeachRepresentativesSet.append(str(representatives))
            testRe.append(representatives)
#     print('')
    return subeachRepresentativesSet
    

def makingFakeRepresentatives(subtotalRepreCoor,subsetCentroidMean,subP):
    
    subfakeRepresentatives=[]
    subTotalFakeRepresentatives=[]
    for indSUC in range(len(subtotalRepreCoor)):
        mSUBRepreCoor=eval(subtotalRepreCoor[indSUC])
        
        mSUBRepreCoor=np.array(mSUBRepreCoor)
        
        subfakeRepresentatives=[]
        for inSUBReInd in range(len(mSUBRepreCoor)):
            fakeElement=mSUBRepreCoor[inSUBReInd]+subP*(subsetCentroidMean[indSUC]-mSUBRepreCoor[inSUBReInd])
            
            subfakeRepresentatives.append(str(list(fakeElement)))
            
        subTotalFakeRepresentatives.append(str(subfakeRepresentatives))
#         print('')
    
    
#     print('')
    return subTotalFakeRepresentatives


def pointAssignment(subFullTotalPoint,subfakeRepresentatives):
    
    evalSubFakeRepre=[]
    
    poAssHeap=[]
    subtotalAssign=[]
    
    for indSF in range(len(subfakeRepresentatives)):
        evalSubFakeRepre.append( eval(subfakeRepresentatives[indSF]))
        
    
    for inSubFullPoint in range(len(subFullTotalPoint)):
        poAssHeap=[]
        
#         if inSubFullPoint==296 or inSubFullPoint==686 or inSubFullPoint== 1108 or inSubFullPoint== 1383 or inSubFullPoint==1948:
#             print('')
        
        for ClusterNumer in range(len(evalSubFakeRepre)):
            for representIndIneachClu in range(len(evalSubFakeRepre[ClusterNumer])):
                fakePointCoord=eval(evalSubFakeRepre[ClusterNumer][representIndIneachClu])
                fakePointCoord=np.array(fakePointCoord)
                eachPointInTotal=np.array(subFullTotalPoint[inSubFullPoint])
                poAsDist=np.sum((eachPointInTotal - fakePointCoord) **2)
                
                
                dataAss=[poAsDist,ClusterNumer]
                heappush(poAssHeap, dataAss)
        
        
        subAssign=heappop(poAssHeap)
        subtotalAssign.append([list(subFullTotalPoint[inSubFullPoint]),subAssign[1]])
#     print('')
    return subtotalAssign



        

if __name__ == "__main__":
     
    sampleData=sys.argv[1]              
    fullData = sys.argv[2]
    k = int(sys.argv[3])
    n = int(sys.argv[4])
    p = float(sys.argv[5]) 
    output = sys.argv[6]


    
    a=1
    totalPoint=[]
    clusterSet=[]
     
    with open (sampleData, "r") as sample:
        for line in sample:
            eachR=line.split(',')
            x=float(eachR[0])
            
            y = eachR[1].replace("\n", "")
            
            y=float(y)
#             total.append([x,y])
#             total.append([a,[x,y]])

            pointCord=np.array([x,y])
            totalPoint.append([a,pointCord])
            #Each point is cluster initially
            clusterSet.append(a)
            a+=1



    FullTotalPoint=[]
    
    with open (fullData, "r") as full:
        for line in full:
            eachR=line.split(',')
            x=float(eachR[0])
            
            y = eachR[1].replace("\n", "")
            
            y=float(y)
#             total.append([x,y])
#             total.append([a,[x,y]])

            pointCord=np.array([x,y])
            FullTotalPoint.append(pointCord)
            #Each point is cluster initially
            
            
    

    heap=[]       
    invalidSet=[]
    checkinv=[]
            
    for pointIndex in range(0,len(totalPoint)):
        for biggerPointIndex in range(0,len(totalPoint)): 
            if (totalPoint[pointIndex][0]) < (totalPoint[biggerPointIndex][0]):
#                 distanceBetweenPoints=np.sqrt(np.sum((totalPoint[pointIndex][1] - totalPoint[biggerPointIndex][1]) **2))
                distanceBetweenPoints=np.sum((totalPoint[pointIndex][1] - totalPoint[biggerPointIndex][1]) **2)
                pairIndex=[totalPoint[pointIndex][0],totalPoint[biggerPointIndex][0]]
                
#                 data=[(distanceBetweenPoints,pairIndex)]
#                 data=(distanceBetweenPoints,pairIndex)
                data=[distanceBetweenPoints,str(pairIndex)]
                heappush(heap, data)
    
    
        
    #Hierarchical clustering of priority queue with Lazy Deletion
    testIn=0
    testInter=0
    bur=0
    while len(clusterSet)!=k:
        testInter=testInter+1

        newClusterCand=heappop(heap)[1]
        newClusterCand=eval(newClusterCand)
#         print(newClusterCand)
#         if type(newClusterCand[0])==type(list()):
#             print('')
        testIn=testIn+1
#         if testIn==5:
#             print(testIn)
        #Memorizie invalid
        
        
        tri=0
        
        for inL in range(len(newClusterCand)):
            if newClusterCand[inL] in invalidSet:
                tri=1
                
        bur=bur+tri    
        
        if tri==0:    
            for ind in range(len(newClusterCand)):
                invalidSet.append(newClusterCand[ind])
                checkinv.append(str(newClusterCand[ind]))
            for ind in invalidSet:
                if ind in clusterSet:
                    inValidIndex=clusterSet.index(ind)
                    clusterSet.pop(inValidIndex)    
                    
#                     if len(clusterSet)==10: 
#                         sorted(flatten(clusterSet))   
        ###################################################        
        
            newClusterAndOtherDistance=addPairsForNewCluster(newClusterCand,clusterSet,totalPoint)
        
            clusterSet.append(newClusterCand)
        
#             print(len(clusterSet))
            
#             if len(clusterSet)==3:
#                 print('')
            
            
            i=0
            for elem in newClusterAndOtherDistance:
                heappush(heap, elem)
            

#     print(testInter-bur)
    
    
    tempFl=[]
    tempFl.append(flatten(clusterSet))
    tempFl=tempFl[0]    
    
    totalRepreCoor=[]
    eachRepreCoor=[]
    secondeachRepreCoor=[]
    setCentroidMean=[]
    #marking representatives of each cluster
    subeachRepresentativesSet=markingRepresentatives(clusterSet,totalPoint,n)
    
    #print representatives
    for indSRT in range(len(subeachRepresentativesSet)):
        
        eachRepreCoor=[]
        secondeachRepreCoor=[]
        pointNum=[]
        
        tempSubRepresentatives = eval(subeachRepresentativesSet[indSRT])
        
        for inindSRT in range(len(tempSubRepresentatives)):
            eachRepreCoor.append(list(totalPoint[tempSubRepresentatives[inindSRT]-1][1]))
            pointNum.append(totalPoint[tempSubRepresentatives[inindSRT]-1][0])
            secondeachRepreCoor.append(totalPoint[tempSubRepresentatives[inindSRT]-1][1])
        print(eachRepreCoor)
#         print(pointNum)
        totalRepreCoor.append(str(eachRepreCoor))
    
    sumCoordXY=[]
    for indCEN in range(len(clusterSet)):    
        allPointInEachCluster=flatten((clusterSet[indCEN]))
        sumCoordXY=[]
        for pointaLLiN in allPointInEachCluster:
            sumCoordXY.append(totalPoint[pointaLLiN-1][1])
            #mean Centroid
        
        centroidMean=sum(sumCoordXY)/len(sumCoordXY)
        setCentroidMean.append(centroidMean)
#         print('')
#     print('')
    
    #Moving Fake Representatives to centrioid with p 
    #if centroid is mean of each representatives
    #Making Fake Centroid with p
    fakeRepresentatives=makingFakeRepresentatives(totalRepreCoor,setCentroidMean,p)
    
    tempRC=[]
    totalRC=[]
    for indTo in range(len(totalRepreCoor)):
        tempRC=[]
        tempTotalRe=eval(totalRepreCoor[indTo])
        for tIndTo in range(len(tempTotalRe)):
            tempRC.append(str(tempTotalRe[tIndTo]))
        
        totalRC.append(str(tempRC))
#     print('')
    
    #Point Assingment
#     fakeRepresentatives=totalRC
    totalAssign=pointAssignment(FullTotalPoint,fakeRepresentatives)
#     print('')

    temClusSeTemp=[]
    with open(output, "w") as text_file:
        for indTAS in range(len(totalAssign)): 
            
#             text_file.write("%f,%f,%d\n" %(totalAssign[indTAS][0][0],totalAssign[indTAS][0][1],totalAssign[indTAS][1]))
            text_file.write("%s,%s,%d\n" %(str(totalAssign[indTAS][0][0]),str(totalAssign[indTAS][0][1]),totalAssign[indTAS][1]))
            temClusSeTemp.append(totalAssign[indTAS][1])
            

    
    
    
    
    
