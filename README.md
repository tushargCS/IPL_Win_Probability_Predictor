
# [IPL Win Probability Predictor](https://ipl-match.onrender.com/ "IPL Win Probability Predictor")


<div align="center" style="border: 10px solid black;">
  <img src="https://wallpapercave.com/wp/wp4059913.jpg" alt="IPL Logo" height=200 width="400" />
</div>
<p align="center">
  <img src="https://wallpapercave.com/wp/wp4059913.jpg" alt="IPL Logo" style="border: 10px solid black;" height="200" width="400" />
</p>


The Indian Premier League (IPL) is a cricket tournament that attracts millions of fans and viewers. Predicting the outcome of an IPL match can be challenging due to the unpredictable nature of the game. This machine learning project uses the Python programming language and the logistic regression algorithm from the scikit-learn library to develop a model that predicts the winning probability of both teams in the second innings of IPL matches.

## Datasets

This project utilizes two datasets. The first dataset contains information on every match played between 2009 and 2019. The second dataset contains data on every delivery in each match after 2009 to 2019. These datasets are preprocessed using the Pandas and NumPy libraries to extract relevant features such as the batting team, bowling team, wickets left, runs left, current run rate, required run rate, current score, and total score of the first inning.

## Model Training

The model is trained on the preprocessed dataset using the logistic regression algorithm, which is a powerful algorithm for binary classification problems. The accuracy of the model is evaluated using the accuracy_score function from the scikit-learn library to ensure that the model is providing reliable predictions.

## User Interface

To deploy the model, the Streamlit library is used to create a user-friendly web interface that allows users to input the relevant features and obtain a prediction for the winning probability of both teams in the second innings. The interface is designed to be intuitive and easy to use, allowing users to quickly obtain predictions for upcoming matches.

## Libraries Used

* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Streamlit

## Conclusion

This project showcases the power of machine learning in predicting the outcome of complex events such as IPL matches. By leveraging the capabilities of Python libraries, this project provides a robust and reliable solution for predicting the winning probability of both teams in the second innings of an IPL match.

