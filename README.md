# CS-499 ePortfolio

## Introduction
This portfolio represents my senior project for my undergraduate degree in Computer Science. I have been studying at Southern New Hampshire University since 2023, and this work is the culmination of my studies at this university and extracircicular studies.

## Education
The coursework at Southern New Hampshire University has helped me continue my education. Before studying at SNHU, I was a mathematics major at the University at Buffalo. Studying computer science was attractive to me because I consider it an extension of the mathematics studies that I was already enjoying. My general focus was pure mathematics, and computer science is a great application of many of the topics that I was interested in, mainly abstract algebra and linear algebra. Several of my courses at SNHU were math focused, such as Discrete Mathemtics and Data Structures and Algorithms. Specifically, in Data Structures and Algorithms, we learned about the abstract data type tree which mirrors the concept of a tree from graph theory. Making these connections between my areas of study was exciting and encouraged me to learn more outside of my classes. The most enjoyable class was the machine learning class taught at SNHU. The class I took was an introductory undergraduate course, but even at that level, I found neural networks interesting and wanted to learn more. This has motivated me to search out additional texts and projects that use machine learning algorithms. This additional learning will be discussed in the enhancement section of this portfolio.

As my knowledge of computer science grew, I because more comfortable with topics in software engineering and databases. Understanding best practices like the separation of concerns and relevant design patterns made me confident in creating applications for others to use. While I have not yeat created something that I ahve monetized, I have made several applications for friends and family. Even this process has helped me to understand the need to understand stakeholder requirements, create prototypes for initial feedback, employ rigorous software security measures, and test software in a controlled environment before rolling it out to the end users. I have even collaborated with others for a few of these projects whic has given me confidence in developing in a team which was reinforced by the collaborative nature of the classes at SNHU.

While I am most interested in machine learning topics, I want to stay sharp in areas throughout the software development space. Studying at SNHU has helped me to understand the software development lifecycle in traditional and agile methodoligies. It has also introduced me to different frameworks and technologies that allow the efficient creation of professional products. These include the Spring framework for Java, the MEAN stack for JavaScript, and the Android Application Programming Interface for creating mobile applications. I have used the groundwork laid by these courses to pursue other frameworks as well. I have spent time learning Django for Python and Actix for Rust. I hope to continue to develop in these areas spanning the computer science field while focusing on my main interest of machine learning.

## Artifacts
For this portfolio, I have chosen to enhance a single artifact. In the machine learning class taught at SHNU, we used a neural network trained on the MNIST dataset which contains images of handwritten digits. The assignment asked us to explore the effect on model accuracy when we changed training parameter values. This was an effective introduction to the topic, but the exploration was surface level, made use of only the single machine learning algorithm, and did not consider new data from outside the MNIST dataset. For my culminating project of my computer science degree, I chose to expand upon this concept while also demonstrating my capabilities in software engineering and databases.

The first goal was to establish an algorithm that performed well on the MNIST dataset. While neural networks are powerful, there are other simpler algorithms that can also perform classification tasks. For this project, the logistic regression and k-nearest neighbors algorithms were also considered. Each algorithm was wrapped in a class that helped to automate the testing of several different model parameters. The keras library was used for training the neural network. I chose to code the other simpler algorithms. While libraries exist that implement these algorithms, I chose to code them myself. This was done to both demonstrate my understanding of the algorithsm and to practice machine learning topics.

Since the original artifact did not classify any new data, I wanted to create a command line interface that would allow a user to classify their own handwritten digits. The images in the MNIST dataset were collected in a structured manner. I wanted to see how well a model trained on this consistent dataset would perform when presented with images from various sources. Of course, we expect the performance to decrease when the quality of the input decreases; however, I wanted this project to be an exploration of how useful these models can still be. The command line interface makes use of secure coding practices and error handling that protects the user and ensures seamless operation.

Because the intention of the project is to explore model performance and not just classify new information, a database was added. SQLite was chosen because of its portability. Ideally, the database file could be shared with others so that those interested can benefit from the information gained. Additionally, well tagged data is especially important in machine learning. The command line interface represents an opportunity to obtain tagged image files from the users. The database stores this along with the model performance data that can be accessed by the user to evaluate model performance.

These enhancements demonstrate an understanding of software engineering principles and database usage, as well as machine learning topics and data structures and algorithms more broadly.

The original artifact is linked below:
<a href="https://github.com/TylerGlover-SNHU/TylerGlover-SNHU.github.io/blob/95ba1a3bb0a88d37eeca1481896ffef1c27d7c26/CS-370Artifact.ipynb" target="_blank">CS-370 Artifact</a>

## Code Review
The below link leads to a YouTube video reviewing the original artifact created in class. The purpose of the original artifact and potential improvements are discussed.
<a href="https://youtu.be/3gjH3afCyv4" target="_blank">YouTube - Code Review</a>

## Enhancement One: Algorithms and Data Structures

## Enhancement Two: Software Design and Engineering

## Enhancement Three: Databases
