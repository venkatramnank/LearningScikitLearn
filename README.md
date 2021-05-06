# LearningScikitLearn
This repo contains the notebooks and scripts written in the process of mastering Scikit Learn library for ML. Note repo still under construction since the learning process is still going on.

### SVM Breast Cancer Classifier
Classification of the classic breast cancer Wisconsin dataset using SVM Classifier with scikit learn. They accuracy reached was close to 95.8% .
              precision    recall  f1-score   support

    malignant       0.96      0.93      0.94        54
       benign       0.96      0.98      0.97        89

        accuracy                           0.96       143
       macro avg       0.96      0.95      0.96       143
    weighted avg       0.96      0.96      0.96       143

### SVM Face Classifier
We use the concepts of SVM to build a face classifer. Further we also use PCA in order to make the classifer better.The classification improved from 85 to 90 percent due PCA.The dataset used is Labeled Faces in the Wild from scikit-learn. It consists of more than 13,000 curated face images of more than 5,000 famous people. Each class has various numbers of image samples.
#### SVM Resutls
                   precision    recall  f1-score   support

     Colin Powell       0.89      0.88      0.88        64
     Donald Rumsfeld       0.84      0.81      0.83        32
     George W Bush       0.88      0.93      0.90       127
    Gerhard Schroeder       0.84      0.72      0.78        29
       Tony Blair       0.91      0.88      0.89        33

         accuracy                           0.88       285
        macro avg       0.87      0.84      0.86       285
     weighted avg       0.88      0.88      0.88       285
 #### PCA Results

                    precision    recall  f1-score   support

     Colin Powell       0.91      0.95      0.93        64
    Donald Rumsfeld       0.77      0.84      0.81        32
    George W Bush       0.95      0.91      0.93       127
    Gerhard Schroeder       0.81      0.86      0.83        29
       Tony Blair       0.93      0.85      0.89        33

         accuracy                           0.90       285
        macro avg       0.87      0.88      0.88       285
     weighted avg       0.90      0.90      0.90       285
