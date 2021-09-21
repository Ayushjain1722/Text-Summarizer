# Text-Summarizer
A webapp that summarizes the given text and returns the result.

## Welcome to the Text Summarizer

## Live Link

https://text-summarizer-ayush.herokuapp.com/


## Novelty

1. Data Generation: Used NLP to generate summary of a given long text and return a downloadable text file.
2. Hybrid Methodology: Used 8 different approaches (cue phrases, numeric data, sentence length, sentence position, word frequency, word frequency, upper case, proper noun, heading matching) for feature extraction and including the sentences whose sum of above features > 1.5*average.
3. Preprocessing: on the document to remove stopwords, converting all words into lowercase, tokenizing the document ans stemming the words using Porter Stemmer.

## Technology Used

1. Flask (Backend) 

![image](https://user-images.githubusercontent.com/42894689/133317407-dc868f47-fbcb-4799-be73-b25313e65b0d.png)

2. HTML (Frontend)  

![image](https://user-images.githubusercontent.com/42894689/133317464-d798e31b-8622-46be-909c-a264e34b7d31.png)

3. CSS (Frontend) 

![image](https://user-images.githubusercontent.com/42894689/133317498-05875c94-9f66-47c4-b2d3-bc5a09d1361b.png)

4. Libraries: nltk, Pandas

<img src="https://user-images.githubusercontent.com/42894689/134191189-67b97351-6107-44ce-a9c7-470e76cdf439.png" width=250px>

![image](https://user-images.githubusercontent.com/42894689/134191138-fd2b9206-827a-4392-9dcf-db3f43f992a2.png)


5. Heroku (Hosting wensite)

![image](https://user-images.githubusercontent.com/42894689/133317602-42753fcb-f12e-45b5-8983-715964902754.png)


## Steps involved:

1. Import libraries
2. Pre-processing the document
3. Convert all words to lower case and removing stopWords
4. Feature Extraction

  A. Sentence Features:

    i. Cue-Phrases like example, therefore, important, according to, etc.
    ii. Numerical Data like dates, transactions, year, age, etc.
    iii. Sentence Length like too long or too short sentence are of little worth
    iv. Sentene Position like starting and ending sentences are of more importance
  
  B. Word Features:
  
    i. Word Frequency
    ii. Upper Case
    iii. Proper Noun
    iv. Heading Match
  
5. Compiling all features to get the summary.

## Flowchart Methodology

## UI Screenshots

![image](https://user-images.githubusercontent.com/42894689/134193094-a99d02a5-daab-4f74-a52f-b5b711736411.png)

![image](https://user-images.githubusercontent.com/42894689/134193192-f3d985d6-55cb-4bbb-a4e9-f470932efe81.png)

## GIF showing the process for sample text

## Input example

```
World Health Assembly charts course for COVID-19 response and global health priorities.
As health leaders prepare to gather for a virtual session of the resumed 73rd World Health Assembly (WHA), WHO has three messages to share. First, we can beat COVID-19 with science, solutions and solidarity. More than 47 million COVID-19 cases have now been reported to WHO, and more than 1.2 million people have lost their lives. Although this is a global crisis, many countries and cities have successfully prevented or controlled transmission with a comprehensive, evidence-based approach. For the first time, the world has rallied behind a plan to accelerate the development of the vaccines, diagnostics and therapeutics we need, and to ensure they are available to all countries on the basis of equity. The Access to COVID-19 Tools (ACT) Accelerator is delivering real results. Second, we must not backslide on our critical health goals. The COVID-19 pandemic is a sobering reminder that health is the foundation of social, economic and political stability. It reminds us why WHO’s ‘triple billion’ targets are so important, and why countries must pursue them with even more determination, collaboration and innovation. Since May, Member States have adopted a number of decisions – the Immunization Agenda 2030, the Decade of Healthy Ageing 2020-2030, as well as initiatives to tackle cervical cancer, tuberculosis, eye care, food safety, intellectual property and influenza preparedness. The resumed session will discuss a 10-year-plan for addressing neglected tropical diseases, as well as efforts to address meningitis, epilepsy and other neurological disorders, maternal infant and young child nutrition, digital health, and the WHO Global Code of Practice on the International Recruitment of Health Personnel, adopted in 2010. Third, we must prepare for the next pandemic now. We’ve seen this past year that countries with robust health emergency preparedness infrastructure have been able to act quickly to contain and control the spread of the SARS-CoV-2 virus. The WHA will consider a draft resolution (EB146.R10) that strengthens Member States’ preparedness for health emergencies, such as COVID-19, through more robust compliance with the International Health Regulations (2005). This resolution calls on the global health community to ensure that all countries are better equipped to detect and respond to cases of COVID-19 and other dangerous infectious diseases.
```
![image](https://user-images.githubusercontent.com/42894689/134231752-c670bb1c-184e-497b-aeb6-f79392d759e9.png)

## Output example

```
The WHA will consider a draft resolution (EB146.R10) that strengthens Member States’ preparedness for health emergencies, such as COVID-19, through more robust compliance with the International Health Regulations (2005).
```
![image](https://user-images.githubusercontent.com/42894689/134231941-fe9f7591-8b01-411c-ba4f-48971ca4a096.png)


## Challenges

