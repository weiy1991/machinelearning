from sklearn import svm

x = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC(kernel = "rbf")
clf.fit(x,y)

print(clf.predict([[2,2]]))
