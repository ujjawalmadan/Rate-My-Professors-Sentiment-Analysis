# Rate My Professors Sentiment Analysis

<h6>Description</h6>
                            <p>
                                In this project, I build a sentiment analysis tool that is trained on the comments and ratings from <a href = 'https://www.ratemyprofessors.com/' target = '_blank'><i>rateprofessors.com</i></a>, a website that allow students to rate schools and professors and submit comments. 
                                I further develop a web application which returns a rating prediction based on a submitted comment by the user.
                            </p>
                            <h6>Motivation</h6>
                            <p>
                                The primary motivation for this project was that I wanted to build a "full-stack" or "end-to-end" project, whereby I go through the entire data science lifecyle from data acquisition to deployment. 
                                Given that perfectly curated datasets are practically non-existent in the real world, and wanting to create an interface for users to interact with the models I built, a sentiment analysis tool based on ratemyprof data seemed ideal.
                                Moreover, there did not seem to be any other projects on the web like this, and very little analysis conducted on the data from ratemyprofessors given that currently, the only way to obtain the data is to scrape it. 
                            </p>       
                            <h6>Business Value</h6>
                            <p>Sentiment Analysis provides value in a wide variety of contexts and scenarios and is very commonly used in social media, marketing and other facets of analytics. 
                                Having multiclass-labelling only makes the analyses more refined, allowing, for example, organizations to prioritize analyses of lowest-rated commments to highest-rated comments.
                                Specific to this project, a website such as <i><a href = 'https://www.ratemyprofessors.com/' target = '_blank'>ratemyprofessors.com</a></i> could either predict in real time what rating the user will give based on the comment they entered and automatically select the prediction as the default rating (making it more convenient for the user).
                                An extension of this project could be to build a keyword detection model which would allow for more detailed analyses and which would yield even more valuable information.<br><br>
                                I think an interesting application of sentiment analysis, which I have yet to see, would be in the surveys requested after you finish your call with a customer representative.
                                Rather than filling out some tedious survey on the phone which is quite cumbersome, if companies simply asked customers to leave a message about their experience (which would take from 10 to 20 seconds), 
                                a speech-to-text conversion could convert the message into text, and then both sentiment analysis and keyword detection could be performed on the text. The feedback could even be stratified by each customer representative and a keyword search, for example, would be able to provide the representative with more specific customer feedback. 
                                Having phoned American Airlines recently to modify an existing reservation where the representative asked me to complete the survey which was in the form of a simple - Press 1 if your experience was satisfactory, else press 0,
                                I believe this approach would provide much more information to the company at little to no additional expense to the customer.
                            </p>
                            <h6>Process</h6>
                            <ol>
                                <li>Obtaining the Data through Web Scraping - Using Scrapy and Selenium</li>
                                <li>Preprocessing - Using Python, Numpy and Pandas</li>
                                <li>Analysis - Exploratory Analysis with data from <a href = 'https://www.timeshighereducation.com/rankings/united-states/2020#!/page/0/length/-1/name/w/sort_by/rank/sort_order/asc/cols/stats' target = '_blank'><i>World University Rankings</i></a></li>
                                <li>Building Models - Built and Fine-Tuned over 10 different NLP Models</li>
                                <li>Evaluating Our Results</li>
                                <li>Deployment - Using Heroku</li>
                            </ol> 
                            <h6>Challenges</h6>
                            <p>
                                Overall, this has been the most time-consuming project I have undertaken, but also the most satisfying. 
                                Perhaps the experience gained from previous projects significantly helped, 
                                but from start to finish, I did not come across any significant or insurmountable obstacles.
                                <br><br>
                                I did find however myself feeling a bit apprehensive given that the data I was working with was not tried and tested and that there were very few analyses done on it. Did I scrape it incorrectly? What if the comments don't reflect the ratings? 
                                Ultimately, I think the experience of working on this was a bit closer to a real-life project where you may be the first person to be analyzing the dataset and the models trained on that data may not yield the results one may have come to expect with tried and tested data. 
                            </p>  
