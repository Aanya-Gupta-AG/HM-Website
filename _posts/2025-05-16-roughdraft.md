---
layout: post
title: Final Project
subtitle: By Aanya Gupta
cover-img: /assets/purple.png
thumbnail-img: /assets/pizza.png
share-img: /assets/pizza.png
tags: [Social Media, Motivation, Data Science, AOD]
---

# Introduction + How and Why I Chose this Topic

Picture this: you have a Calculus test tomorrow, which you have not studied for. You get home, sit down at your desk, and start solving some problems. After what feels like 5 hours have passed, you take a break by using social media on your phone. Why do you do this? Would you feel more or less motivated to study after your break? 

Like many students, I have experienced the preceding scenario. Social media has become one of the biggest threats to our generation, hindering our attention spans and abilities to concentrate, hurting our mental health, and much more. A study found that 67% of teenagers use 3+ hours of social media per day, and coupling these facts with my experiences, I decided that for my final project, I wanted to do something related to adolescent usage of social media. 

In my junior year, I conducted independent, scientific research outside of school regarding mental health. Hence, I initially thought of doing something related to mental health and social media. However, I'd previously read a lot about that topic, so it didn't interest me as much. With the recent rise in the field of decision sciences, and the Class of 2025's collective senioritis, I decided that motivation might be interesting to study. 

After reading many scientific papers about the intersections between social media, mental health, and motivation, I decided that I would seek to determine the relationship between hours of social media usage and subsequent motivation to study, whilst also creating my own intervention. 

# Methodology

I hypothesized that as both male and female students used more social media during their breaks, their subsequent motivation to study would decrease. In order to test this hypothesis, I created two surveys (with the exact same questions) that I would send out to 35 males and 35 females; the reasoning behind sending my survey to a total of 70 students was that I had to pick a sample size which had a quantity of participants which was less than 10% of the total, UD student population. There are 722 students in the UD this year, and 10% of that is 72. Hence, I picked a multiple of ten close to that value (70). Since I wanted to control for gender, I divided 70 by 2 to see how many males and females to whom I would send my survey (35 each). To gather the names, I emailed Mr. Garrison, and he selected 35 random males and females from 9th - 12th grade (year groups were completely randomized, but ended up being roughly even). 

In terms of the actual survey itself, I went through multiple iterations to reduce biases in the questions I asked, and any biases participants might project onto the results they submitted. Since the attention span of HM students for random surveys is quite low, I decided that I would write a maxmimum of three questions. 

1. During a study break, for how long do you use social media?
2. After your break, how motivated do you feel to continue studying?
3. Can I reach out to you if I have more questions?

Then, I sent out my survey and awaited responses from my participants. I sent follow-up emails to people who did not respond to their survey.  

# Data

17 out of 35 females responded to their survey, while 16 out of 35 males responded to their survey. Respondents who said they did not use social media during their breaks were omitted from the dataset prior to analysis--which applied to 4 males. 

## Females:

![fgraph1](/assets/FEMALE.jpg)

From the histogram, it was found that 5-10 mins and 10-30 mins were the most selected answers (each 7 times) for how much social media was used during female students' study breaks. The minimum social media usage was 5-10 minutes and the maximum was 1 hour+. Since no responses listed 1-5 minutes despite it being an option, it was omitted from the graph. As shown by the distribution, this isn’t a normal distribution; it's skewed way right! From the graph, it can be concluded that the students were not distributed equally across the social media usage gathered.

![fgraph2](/assets/FEMALE2.jpg)

From the histogram, it was found that 3 was the most selected answer (8 times) for how motivated female students felt after study breaks involving social media. The minimum motivation was 1 and the maximum was 4. Since no responses listed 5 despite it being an option, it was omitted from the graph. As shown by the distribution, this isn’t a normal distribution either; it's skewed left! From the graph, it can be concluded that the students were not distributed equally across the motivation levels gathered.

![fgraph3](/assets/fgraph3.jpg)

From the scatter plot–as shown by the generally downward trend in the points and the negative slope of the linear regression line–as hours of social media usage during sudy breaks increased, motivation to study decreased. Coupled with the determined correlation coefficient of -0.75, it could be determined that a significant, inverse, and negative relationship exists between social media usage and motivation. This makes sense not only because other studies have validated this relationship, but also because social media is extremely addictive; when you watch social media, you brain produces short, bursts of dopamine. Hence, the more you watch, the harder it will be to stop watching, leading to decreased motivation when you force yourself to stop using social media and focus on something that (probably) doesn't induce as much dopamine production in your brain: studying. 

## Males:

![mgraph1](/assets/MALE.jpg)

From the histogram, it was found that 5-10 mins was the most selected answers (6 times) for how much social media was used during male students' study breaks. The minimum social media usage was 5-10 minutes and the maximum was 1 hour+. Here, 1-5 minutes was omitted from the graph as well. This distribution was skewed right. 

![mgraph2](/assets/MALE1.jpg)

From the histogram, it was found that 2 and 3 were the most selected answers (each 5 times) for how motivated male students felt after study breaks involving social media. The minimum motivation was 1 and the maximum was 4. 5 was omitted from the graph as well. This distribution is not a normal one, but it is also not skewed either left or right, as seen in graph. 

![mgraph3](/assets/mgraph3.jpg)

As seen in the scatter plot for females, from this scatter plot–as seen through the generally downward trend in the points and the negative slope of the linear regression line–as hours of social media usage during study breaks increased, motivation to study decreased. Coupled with the determined correlation coefficient of -0.78, it could be determined that a significant, inverse, and negative relationship exists between social media usage and motivation. This makes sense for the same reason as for females. 

# Extending my Findings

My hypothesis was indeed proved: significant, inverse, negative relationship exists between social media usage during breaks and subsequent motivation to study. However, I wanted to create an intervention that could be used in place of social media. Hence, I did some brainstorming, and I settled on **The Social Intervention.** 

The Social Intervention is a website that I created using HTML and Javascript which students can use during their study breaks in place of other negative applications. The website includes a 5-minute timer and guided, relaxing animations that I drew by hand. The website can be found by clicking the following link:

[The Social Intervention](https://ag-aanya-gupta.github.io/social.intervention/index.html)

I spent a lot of time trying to recall what I had learned in App Development, which involved going throuugh my freshman year notes! :D I started by creating the basics on the homepage (plaing the titles, changing the background, creating a bar for redirection to multiple pages, etc). 

Then, I started creating the timer. I had a rough idea of how to make the timer, but I didn't really know how to execute my ideas in code, properly. Hence, I watched a couple of youtube videos and read a few websites. There was a lot of debugging involved, but it eventually started working! I made the timer such that people couldn't pause it, because you shouldn't be able to pause the time designated for a break if you're serious about it. Ms. Feng gave a good idea to make a sound ring when the timer was up, so I researched how to do that and edited my code so that the timer rang. 

After that, I moved on to creating the animations. I knew that I wanted it to have a Studio Ghibli vibe (even though I'm not artistic at all and cannot draw), and be something simple yet stimulating. Originally, I planned to create two vidoes; one would be a guided relaxation video (a character guides the student to do exercises, drink water, rest their eyes, etc), and the other would be an unguided relaxation video (the character plants various flowers and plants in their garden, while the student is free to just leave the video running and do what they need to during their break (except use social media!)). I've never created hand-drawn animations before, so I downloaded a new app and taught myself how to do it. However, I didn't realize that you could duplicate frames until I'd individually re-drawn many, many frames, which took up a LOT of time. As a result, I shifted my goal to making one video, which was uploaded to the website. I tried directly uploading through Github, but the file size was too big! D: Hence, I uploaded the video to a separate website to reduce the file size, and wrote some code so that the video would be able to be viewed and played on wesite.

After that, I thought I'd add a cute little "What we Do" page to the website, just to make it a little official. 

# Conclusion

In a nutshell, I found that a significant, inverse, negative relationship exists between social media usage during breaks and subsequent motivation to study. Additionally, I tried creating an intervention which students could use during break as opposed to social media. If I were to continue this project (which I probably will, since I love this topic), I would test out the efficacy of my intervention. It might involve having one group of students use my intervention during their breaks, and another group use social media during their breaks. Furthermore, I will definitely include non-binary/non-gender conforming students; I had already sent my survey out by the time I talked with Ms. Feng. Also, it might be cool to see how social media usage v. motivation differs for different age groups. 

Overall, this was a really fun project! I loved that we were able to explore what we wanted to, and that made me motivated to keep working throughout the process. The planning stage was probably the hardest, but after that, it was really cool to be able to analyze and create what I'd been planning. It's been a pleasure being in this class!! :D 
