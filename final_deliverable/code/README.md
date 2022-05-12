# Code README
This is where you can document your design decisions, known bugs, and instructions to run your code.

## Model design
We decided to implement a classification model instead of regression model due to the uneven distribution of the dataset. This helps us achieve up to 30% accuracy compared to 20% accuracy from a greedy algorithm. We used a feed forward neural network with 3 dense layers and relu as the activation function. This might cause a dead relu problem but input normalization should help alleviate this problem. Lastly, we used categorical crossentropy as our model evalution.

## Known bugs
No known bugs that would break the model. However, we might be able to achieve higher performance by tuning the hyperparameters such as batch size and number of epochs or using other methods of optimization such as batch normalization.

## How to run code
Since we used a relative path to the dataset, the code must be run from the directory /code. Run the following commands in your virtual environment.

    python3 categorial_model.py
    python3 confusion_matrix.py