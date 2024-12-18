class node:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
        self.high = 1

class AVL:
    def __init__(self):
         self.root = None
    def level(self, x):#внутриклассовая вспомогательная
        if x == None:
            return 0
        else: return x.high
    def bal(self,x):#внутриклассовая вспомогательная
        if x == None:
            return 0
        return self.level(x.left) - self.level(x.right)
          
    def leftrot(self,x):#внутриклассовая вспомогательная
            r = x.right
            l = r.left
            r.left = x
            x.right = l
            x.high = max(self.level(x.left), self.level(x.right))+1
            r.high = max(self.level(r.left), self.level(r.right))+1
            return r
    def rightrot(self,x):#внутриклассовая вспомогательная
            l = x.left
            r = l.right
            l.right = x
            x.left = r
            x.high = max(self.level(x.left), self.level(x.right))+1
            l.high = max(self.level(l.left), self.level(l.right))+1
            return l
    def add(self,x):#основная
        if self.root == None:
            self.root = node(x)
        else: self.addknot(self.root,x)
    def addknot(self,knot,x):#внутриклассовая вспомогательная
        if x == knot.val:
             return
        if x < knot.val:
            if knot.left == None:
                knot.left = node(x)
            else: self.addknot(knot.left,x)
        if x > knot.val:
            if knot.right == None:
                knot.right = node(x)
            else: self.addknot(knot.right,x)
        knot.high = max(self.level(knot.left),self.level(knot.right))+1
        blnc = self.bal(knot)
        if blnc > 1:
             if x < knot.left.val:
                  return self.rightrot(knot)
             else:
                  knot.left = self.leftrot(knot.left)
                  return self.rightrot(knot)
        if blnc < -1:
             if x > knot.right.val:
                  return self.leftrot(knot)
             else:
                  knot.right = self.rightrot(knot.right)
                  return self.leftrot(knot)
        return knot
    def bestchange(self,knot):#внутриклассовая вспомогательная
        def closemin(knot):
            if knot == None or knot.left == None:
                return knot
            return closemin(knot.left)
        def closemax(knot):
            if knot == None or knot.right == None:
                return knot
            return closemax(knot.right)
        mn = closemin(knot.right)
        mx = closemax(knot.left)
        if knot.val - mn.val <= mx.val - knot.val:
             return mn
        else: return mx
    def delete(self,x):#основная
         return self.deletenode(self.root,x)
    def deletenode(self,knot,x):#внутриклассовая вспомогательная
        if knot == None:
             return
        elif x > knot.val:
             knot.right = self.deletenode(knot.right,x)
        elif x < knot.val:
             knot.left = self.deletenode(knot.left, x)
        else:
            if knot.left == None:
                cng = knot.right
                knot = None
                return cng
            elif knot.right ==  None:
                cng = knot.left
                knot = None
                return cng
            cng = self.bestchange(knot)
            k = knot.val
            c = cng.val
            knot.val = cng.val
            if k > c:
                knot.right = self.deletenode(knot.right,cng.val)
            else: 
                knot.left = self.deletenode(knot.left,cng.val)
        if knot == None:
            return knot
        knot.high = max(self.level(knot.left),self.level(knot.right))+1
        blnc = self.bal(knot)
        if blnc > 1:
             if self.bal(knot.left) >= 0:
                  return self.rightrot(knot)
             else:
                  knot.left = self.leftrot(knot.left)
                  return self.rightrot(knot)
        if blnc < -1:
             if self.bal(knot.right) >= 0:
                  return self.leftrot(knot)
             else:
                  knot.right = self.rightrot(knot.right)
                  return self.leftrot(knot)
    def search(self,x):#основная
        if self.root == None:
             return print("Дерево пусто")
        elif self.root.val == x:
            return self.root
        else: return self.searchnode(self.root,x)
    def searchnode(self, knot,x):#внутриклассовая вспомогательная
         if knot == None:
              return print('Элемента нет в дереве')
         if knot.val == x:
              return knot
         elif knot.val < x:
              return self.searchnode(knot.right,x)
         else: return self.searchnode(knot.left,x)
    def getinarray(self,arr):
        return self.getinarray_(self.root,arr)
    def getinarray_(self,knot,array):#внутриклассовая вспомогательная
        if knot != None:
            array.append(knot.val)
            if knot.left == None and knot.right == None:
                return array
        if knot.left != None and knot.right != None:
            return self.getinarray_(knot.right,array) + self.getinarray_(knot.left,array)
        elif knot.left != None and knot.right == None:
            return self.getinarray_(knot.left,array)
        elif knot.left == None and knot.right != None:
            return self.getinarray_(knot.right ,array)





                    
