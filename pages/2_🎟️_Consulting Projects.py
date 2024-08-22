import streamlit as st

st.title("ML/AI Project Details")
st.markdown("""
##### 1.	*Vernacular Voice and Text-Based AI Assistant*\n
###### *Generative AI, OpenAI LLM API, Langchain, Pinecone Vector Database, Scrapping, Data Analysis, Python*

We have developed a conversational RAG (Retrieval-Augmented Generation) application designed to assist farmers by providing answers to their queries through both voice and text interfaces. This AI assistant addresses a broad spectrum of agricultural topics, including government policies, crop cultivation practices, irrigation techniques, pest control measures, and the use of agricultural products and tools, as well as other farm-related subjects.

**Proof of Concept Completion**

The initial proof of concept has been successfully completed, utilizing cutting-edge technologies: OpenAI's API for the Large Language Model (LLM), Pinecone as the vector database, and Langchain as the orchestration framework. This phase demonstrated the application's capability to deliver accurate and contextually relevant responses to farmers' inquiries, showcasing the potential of AI in transforming agricultural support.

**Next Steps**

Building on this success, we are now advancing to the next stage of development. Our focus will be on training an open-source large language foundation model, which will then be fine-tuned under supervision using a dataset comprising real-world queries from farmers. This fine-tuning process will ensure that the AI model is highly specialized in addressing the unique challenges and needs within the agricultural sector.

**Future Vision**

In the later stages of the project, we plan to integrate a GenAI agent capable of analyzing satellite imagery to identify specific plant diseases, nutrient deficiencies, and environmental stress factors. This innovation will empower farmers to apply targeted treatments precisely where they are needed, thereby reducing chemical usage, minimizing waste, enhancing crop yield and quality, and promoting sustainable farming practices.\n

***Complete Idea & Development done by me***\n
The entire concept was conceived and developed by me, with a focus on creating value and addressing key challenges within the agricultural sector. After thorough discussions, both the investors and the founder found this idea exceptionally compelling, recognizing its potential to significantly benefit the company. The idea not only aligns with the company’s goals but also positions us strongly in the market, driving future growth and sustainability.

##### 2.	*Grain Quality Digitization Using CNN ResNet Model*\n
###### *Deep Learning, Convolutional Neural Network, ResNetTensorflow*

The Grain Quality Digitization work package aims to create an automated system for classifying maize kernel quality using Convolutional Neural Networks (CNN), particularly the pre-trained ResNet (Residual Networks) model. This work package seeks to digitize and standardize the quality assessment process, ensuring consistent, accurate, and efficient maize classification. 

***Data Collection***: 

Image Acquisition: Initial model training began with publicly available maize images. Later, we requested farmers to provide high-resolution images of maize kernels, labeled with quality grades such as A, A+ etc. These images were captured under standardized conditions to ensure uniform lighting and background. 

Dataset Preparation: The images were annotated based on predefined quality metrics, including kernel size, color, shape, and defects. To improve the model's robustness and diversify the dataset, data augmentation techniques like rotation, scaling, and flipping were applied. 

**Model Training**: 

***Training Data***: The annotated maize kernel dataset was used to train the ResNet model. Using transfer learning technique, we fine-tuned a pre-trained ResNet model on our specific maize kernel dataset. Initially, the model achieved around 50% accuracy due to the limited dataset. However, as more images were added to the dataset, the model's accuracy started to improve. 

***Optimization***: Hyperparameters such as learning rate, batch size, and the number of epochs were carefully optimized to enhance the model's performance, leading to more accurate and reliable maize quality assessments. 


##### 3.	*Inventory optimizing for a Retail Chain*\n
###### *Data Analysis, Python, PowerBI, SQL Database*
For a retail store client SaveMore, analysed & built sales & inventory dashboards. Sales dashboard helped supermarket clients in understanding identifying sales trends, seasonal fluctuations, top performing products, & customer buying pattern across all stores. And Inventory dashboards, helped in tracking inventory levels, demand forecasts, and reorder points. This prevents overstocking or under stocking thereby reducing inventory cost. 


##### 4.	*Brand Listening & Sentiment Analysis for Spring-Mattress Company*\n
###### *Machine Learning, NLP, Data Analysis, Python, PowerBI, SQL Database*
Brand Listening & Sentiment Analysis project for a client Spring-Mattress company that is based out of US. The analysis provided valuable insights into how customers perceive the brand, its products, and services. By monitoring online conversations, social media interactions, and customer reviews, the company gained a deep understanding of customer sentiment, preferences, and pain points. This information helped in identifying areas of improvement, addressing customer concerns proactively, and enhancing overall brand reputation and customer satisfaction. The actionable insights derived from the analysis guided strategic decision-making, allowing the company to optimize marketing strategies, product development, and customer engagement initiatives.
\n

##### 5.	*Clustered and Analysed data from HomeOwner Association (HOA)*\n
###### *Machine Learning, Clustering Algorithm, Data Analysis, Python, SQL Database*
Extracted and Analysed data from HomeOwner Association (HOA) PDF documents & categorized & store the data in a SQL database, paving the way for a front-end service that provides users with insights based on the uploaded HOA documents.
\n

##### 6.	*Build Sales Pipeline for Cilans systems*\n
###### *Machine Learning, NLP, Scrapping, Data Analysis, Python, PowerBI, SQL Database*
For the client Cilans system who are into corporate trainings & consulting services. The project entails scraping publically available data from specified websites to collect comprehensive information about companies & working professionals, storing this data securely in a database, and utilizing Natural Language Processing (NLP) techniques for insightful analysis. The goal was to extract meaningful insights such about company, number of employees, name decision makers etc. that can benefit the client's sales team and enhance their sales strategies. The project significantly aided the client in creating an effective sales pipeline by leveraging data scraping which led to 30% increase in leads generation. The NLP insights enabled targeted outreach and personalized communication, ensuring engagement with high-potential leads that resulted in 15-20% improvement in the conversion rate. This approach streamlined the sales process, allowing the client to prioritize opportunities and optimized follow-up actions, reducing the average sales cycle duration by 15%, resulting in faster deal closures.
\n

##### 7.	*Developed Machine Learning based Stocks Trading Strategies*\n
###### *Machine Learning, Time Series, Trading API, Scrapping, Data Analysis, Python*
For a SAAS based trading platform Investo created ML based algorithmic trading strategies. The project involved designing, implementing, and optimizing Machine Learning based algorithmic trading strategies tailored to meet the specific requirements of clients. The goal was to develop automated trading systems that can execute trades based on predefined criteria and parameters.  Conducted back testing to evaluate strategy performance using historical data & optimize strategies for maximum efficiency, profitability, and risk mitigation. Backtesting strategies resulted in a quantifiable improvement in traders' profitability, with an average increase of 10% in profits across tested strategies.
\n\n

##### 8.	*Developed Smart Stocks Screeners*\n
###### *Machine Learning, Trading API, Scrapping, Data Analysis, Python*
Developed custom trading screeners for individual retail traders & implemented these screeners on cloud servers for easier access to the traders. These screeners were designed to assist clients in identifying potential trading opportunities based on their specified filtering criteria and market conditions. The developed screeners helped traders in filtering thousands of stocks & uncover hidden gems – stocks but haven't yet garnered wider attention. It frees up valuable time for the clients so that they can focus on in-depth analysis and trade execution. It also provides real time alerts & notifications about their trade setups price movements, or market events, allowing them to act promptly and capitalize on opportunities. Screener helped client in identifying 10 times more trading opportunities compared to when client was manually filtering & following stocks his stocks.

""")

