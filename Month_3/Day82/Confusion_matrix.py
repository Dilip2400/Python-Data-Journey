actual = [1, 1, 1, 1, 0, 0, 0, 0]
prediction = [1, 1, 0, 0, 1, 0, 0, 0]
TP = 0
TN = 0
FP = 0
FN = 0
for i in range(len(actual)):
    if actual[i] == 1 and prediction[i] == 1:
        TP = TP+1
    elif actual[i] == 0 and prediction[i] == 0:
        TN = TN+1
    elif actual[i] == 0 and prediction[i] == 1:
        FP = FP+1
    else:
        FN = FN+1
        
print("TP: ", TP, "\n TN: ", TN, "\n FP: ", FP, "\n FN: ", FN )

#accuracy = (TP+TN)/(TP+TN+FP+FN)
#precision = TP/(TP+FP)
#recall = TP/(TP+FN)
#f1 = 2(precision*recall)/(precision + recall)

#print("Accuracy: ", accuracy, "\nPrecision: ", precision, "\nRecall: ", recall, "\nF1 Score: ", f1)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score)
cm = confusion_matrix(actual, prediction)
accuracy = accuracy_score(actual, prediction)
precision = precision_score(actual, prediction)
recall = recall_score(actual, prediction)
f1 = f1_score(actual, prediction)
print(cm)
print("Accuracy: ", accuracy, "\nPrecision: ", precision, "\nRecall: ", recall, "\nF1 Score: ", f1)