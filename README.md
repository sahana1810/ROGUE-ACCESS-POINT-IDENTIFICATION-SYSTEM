# ROGUE-ACCESS-POINT-IDENTIFICATION-SYSTEM
A Machine Learning project that identifies potentially rogue Wi-Fi access points based on network characteristics.

1. Project Overview

The "Rogue Access Point Detection System" is a Machine Learning project designed to identify potentially unauthorized or suspicious Wi-Fi access points based on their network characteristics.

A rogue access point is a wireless access point that has been installed or connected without proper authorization. It may create security risks by allowing unauthorized access to a network.

This project analyzes network-related features such as encryption type, channel, signal strength, duplication status, and distance level to classify access points using a trained Machine Learning model.

The goal is to support the identification of potentially suspicious access points and improve awareness of wireless network security.

2. Objectives

- To identify potentially rogue or suspicious Wi-Fi access points.
- To collect and preprocess network-related data.
- To perform Exploratory Data Analysis (EDA).
- To train a Machine Learning classification model.
- To evaluate the model using appropriate performance metrics.
- To provide a simple interface for entering network details and viewing predictions.

3. Dataset Description

The dataset contains network-related features used for access point classification.

   Feature Description 

 Label - Target class representing the access point category 
 Is_Duplication - Indicates whether a duplicate characteristic is present 
 Distance_Level - Represents the distance category 
 Encryption - Specifies the encryption type 
 Channel - Wi-Fi channel information 
 Signal_Strength - Received signal strength, typically represented in negative dBm values 
 BSSID - Basic Service Set Identifier of the access point 
 SSID - Name of the wireless network 

The dataset is preprocessed before being used for Machine Learning.

 4. Technologies Used

    Programming Language: Python
    Data Processing: Pandas, NumPy
    Data Visualization: Matplotlib, Seaborn
    Machine Learning: Scikit-learn
    Model Persistence: Joblib
    Web Application: Streamlit
    Development Environment: VS Code

Only list the technologies that are actually used in the final implementation.

Machine Learning Algorithms

The project explores classification algorithms for identifying access point categories.

Random Forest
Random Forest combines predictions from multiple decision trees to produce a classification result. It can model relationships between different network features.

K-Nearest Neighbors (KNN)
KNN classifies an input based on the labels of nearby data points in the feature space. Feature scaling can be important for this algorithm.

Support Vector Machine (SVM)
SVM learns a decision boundary that separates classes in the feature space. Feature scaling is generally important for SVM.

The final deployed algorithm should be specified according to the model actually selected and saved for the application.

5. Project Workflow

1. Data Collection: Obtain the dataset containing access point characteristics.
2. Data Preprocessing: Handle missing values, duplicates, and categorical features as appropriate.
3. Exploratory Data Analysis: Examine feature distributions, class counts, and relationships between variables.
4. Feature Preparation: Select the input features and target label.
5. Data Splitting: Divide the dataset into training and testing sets.
6. Model Training: Train the selected classification algorithm.
7. Model Evaluation: Evaluate predictions using suitable classification metrics.
8. Model Saving: Save the trained model and any required preprocessing objects.
9. Web Application: Use Streamlit to accept input features and display the predicted class.


6. Model Evaluation

The model should be evaluated using a separate test dataset that was not used during training.

Recommended evaluation metrics include:

Accuracy: Overall proportion of correct predictions.
Precision: Proportion of predicted positive cases that are actually positive.
Recall: Proportion of actual positive cases correctly identified.
F1-score: Harmonic mean of precision and recall.
Confusion Matrix: Shows correct and incorrect predictions for each class.

For a security-related classification task, recall for the rogue or suspicious class is particularly important because missed detections may represent potential security risks.

The evaluation should also check for data leakage, class imbalance, and differences between training and test performance.

7. Results

The application is designed to generate a predicted access point category from the supplied network characteristics.

The final results should be reported after evaluating the selected model on the test dataset.

 Selected Model - To be confirmed 
 Test Accuracy - To be measured 
 Precision - To be measured 
 Recall - To be measured 
 F1-score - To be measured 

Replace these placeholders with actual test results before publishing the final version.

8. Limitations

Predictions depend on the quality and representativeness of the training dataset.
Incorrect, incomplete, or outdated input data may affect predictions.
Signal strength and distance categories can vary with the environment.
A legitimate access point may share characteristics with a suspicious one.
A Machine Learning prediction alone cannot confirm that an access point is unauthorized.
The system does not independently verify network ownership or detect every possible wireless attack.
Performance on new networks may differ from performance on the test dataset.

9. Future Scope

Integrate real-time Wi-Fi scanning through suitable wireless network interfaces.
Use authorized network monitoring data for more realistic testing.
Add a dashboard with prediction history and visual analytics.
Improve detection using additional network characteristics.
Compare classification algorithms using consistent evaluation methods.
Add alerts for potentially suspicious access points.
Test the model on independent datasets from different network environments.
Improve data validation, model monitoring, and security controls.

10. Responsible Use

This project is intended for educational purposes and authorized wireless network security monitoring.

Predictions should be treated as indicators for further investigation rather than definitive proof of malicious activity. Use network data only with appropriate authorization.


11. Conclusion

The Rogue Access Point Detection System demonstrates how Machine Learning can be applied to wireless network security classification. By combining data preprocessing, exploratory analysis, model training, evaluation, and a Streamlit interface, the project provides a foundation for investigating potentially suspicious Wi-Fi access points.

Further testing with representative real-world data is necessary before using the system for operational security decisions.
