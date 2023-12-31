# Goku-Multiclass-Image-Classification 
(Learned from and used code from Udacity course "Intro To Tensorflow for Deep Learning" under Apache License Version 2.0) 

With this project, I first scraped hundreds of images of the character in three different forms and created a dataset. The dataset contained 1000+ images taken from the web. From there, I split the data such that 80% of the images were used for training and 20% were for validation.

Now a problem that I encountered during the dataset creation was that I simply scraped them from google images. As a result, many of the images were very similar and had no variation. To try to fix this, I used image augmentation and a 20% chance of dropout (when neurons are disconnected from the nueral network and thus force the model to rely on all neurons as balanced as possible). 

For this project I used a model that consisted of two main layers: the convoluted neural network layer and the fully connected dense layer. The convoluted neural network consisted of 3 blocks of convoluted 2d layers and a max pooling layer. After the CNN block, the model was flattened and made into a 512 fc dense layer. These layers all used the Relu function. Finally the model ends with a 3 neuron dense output layer using the softmax function. 

Overall, the project taught me a lot about data augmentation/collection and deep learning (especially convoluted neural networks). The model was able to achieve low 70% accuracy. Some reasons for this are that the images were all similar. Additionally, after further research, I learned that some of the images under "Goku Form 2" were actually images of the character in form 2 because of google images' behavior. 

Some ways to improve the model could be to further refine the dataset and try to get a more diverse range of data. Additionally, according to the graphs, it seems the validation loss started increasing by a little at the end of the training. This hints at potential overfitting and could be fixed by training it for a lower number of epochs. Finally, I could also use transfer learning to use a previously trained model and get higher accuracy. 

