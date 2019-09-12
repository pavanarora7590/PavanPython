def bintree (r):
    return [r,[],[]]
#simply create  a root and empty left, right
def insertLeft (root,newbranch):
    t=root.pop(1) #pop out root
    '''if already something exists, then insert on left new branch, middle root keep as it was  and right will be empty'''
    if len(t)>1:
        root.insert(1,[ newbranch,t,[] ])
    #'''insert new and push the existing one level down'''
    else:
        root.insert(1,[newbranch,[],[]])
    return root
def insertRight (root,newbranch):
    t=root.pop(2) #pop out right child
    '''if already something exists, then insert on right new branch, middle root keep as it was  and right will be empty'''
    if len(t)>1:
        root.insert(2,[newbranch,[],t])
    #'''insert new and push the existing one level down'''
    else:
        root.insert(2,[newbranch,[],[]])
    return root    
def getroot(root):
    return root[0]
def setnewroot(root,newvalue):
    root[0]=newvalue
def getleft(root):
    return root[1]
def getright(root):
    return root[2]
r=bintree(3)
insertLeft(r,4),print (r)
insertRight(r,5),print (r)
insertRight(r,6),print (r)