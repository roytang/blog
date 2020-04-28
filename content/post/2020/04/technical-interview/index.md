---
date: 2020-04-28
slug: technical-interview
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/104074130524933256
- type: twitter
  url: https://twitter.com/roytang/statuses/1254978666859163650/
tags:
- software-development
title: Technical Interview Notes
---

I've had the good fortune to be on the interviewer side of technical interviews much more often than I've been the interviewee. I've been doing a few more of these over the past couple of years and made some notes, so I thought I'd talk about technical interviews for a bit. Caveat: these are largely based on my own experiences, in the local environment here in the PH.

### Technical Exam / Screening

Many companies will ask applicants to undertake a technical exam before letting them advance to further stages of the recruitment process. This kind of screening is most useful if your applicants are mostly fresh graduates or junior programmers. The primary purpose of such a screening is to make sure that the candidate is actually a programmer, and not just someone who graduated CS while letting all his groupmates handle the programming work. This is especially useful for companies that get a lot of applicants who are fresh graduates - it lets them filter the candidate pool without using up the valuable time of their senior technical staff. I talked about these kinds of technical screenings in [a previous post](/2016/06/the-programming-application-process/) about my own experiences as an interviewee. 

As a sample statistic, I used to handle checking of technical exams for a company that had a few dozen applicants per week. The screening was a straightforward ten-question written exam, none of the questions required writing a lot of code. The questions were along the lines of "where is the problem in the loop?", or "what is the output of this program?", essentially confirming the applicant's ability to understand how code is written. Even for this simple screening, roughly 8-9 out of 10 applicants would regularly fail the screening. (I am not sure if this speaks to the general low quality of graduates in my area instead of a general trend.) There is a reason [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) has become known as screening tool.

The screening can take different forms. It may be written, requiring you to come into their office, sit at a table and answer some number of programming-related questions on paper (as described in the paragraph above). This is the most common I have encountered, especially in larger companies here. 

Some may be done remotely/online, via services such as [Codility](https://www.codility.com/). This may be the best option, as it allows the candidate to take the exam on their own time, in the comfort of their own environment. Such environments will also automatically check the results, which means the effort for the recruiting company is at a minimum and the candidate gets feedback quickly. The downside is that not all companies may be able to afford such services.

The worst option is when they do a phone screening - someone asking you technical questions over the phone. Phone screening is the worst because there are no real technical questions that can be of any practical use in evaluating a candidate over the phone. Most good technical screening questions will require a lot of text (better on paper than verbally over the phone) or may otherwise have nuance in the possible answers. For the latter case, it's probably fine if they have a senior developer doing the phone screenings, but few companies can afford that, so most likely it will be some HR person who was provided with a fixed set of answers where if you don't have the exact answer they have on their cheat sheet, you won't pass the screening. As much as possible I would suggest to avoid any companies that use phone screening, as it is an organizational smell.

### Technical Interview

The technical interview is different from a technical screening in that it usually involves face-to-face time with one or more interviewer(s). You will be usually given one or more technical problems, usually of a higher difficulty than would be present in a technical exam/screening. Usually, you will be asked to provide a solution on paper or on a whiteboard, and would be expected to walk the interviewer(s) through your solution. The purpose of this stage is for the interviewer to see personally how you think through the problem and how you devise a solution and (to a lesser extent) how well you can present it.

I used to do a lot of these styles of interviews back in the day. At my old company, we had a pool of challenging technical interview questions, many of them requiring some level of algorithm knowledge in order to provide efficient answers. Many would require things like graph traversal, binary trees, that kind of thing. Some level of optimization is expected.

There are several problems with this approach, the main one being it often doesn't really test for how well a person would perform as a software engineer. For one thing, such an environment is not reflective of actual programmer work environments. If you're interviewing for a web developer position, such complicated problems would come up in your day-to-day work maybe 5-10% of the time at best. (The numbers go up the lower level you go, such questions would be a lot more useful for systems programming work for example.) And unless you are hiring someone specifically for a high pressure position, this type of exam is biased against people with anxiety or who otherwise have trouble working with what is akin to a gun to their head. It is also effort-intensive on the part of the interviewer(s), since often you will need to sit through the candidate explaining their solution and maybe pointing out flaws or inefficiencies in the approach. So I've kind of soured on this approach and haven't done it in a while, but there are specific situations where it would be useful.

These days, what I like to do in technical interviews varies depending on the level of the role I'm interviewing for:

- for fresh graduates or junior developer roles, I will generally ask 2-3 comparatively simple programming questions. Something only a bit more difficult than FizzBuzz, maybe along the lines of a fibonacci function or some array processing or such. This is especially useful if I'm doing this for a small company that doesn't have the technical screening step, or to verify the results of the technical screening step. Afterwards, I will tend to do a short Q&A, asking some questions about projects they have worked on (maybe at school), what difficulties they have encountered, how they approach a problem etc.
- for more senior positions, I tend to skip programming questions altogether (I assume that they haven't spent 5 or so years BSing their way through programming tasks) and prefer a more detailed Q&A, usually tailored towards the expectations for the role and their specific background. Typically I will ask questions that will require the candidate to expound on technical issues such as:
  - what was the biggest technical challenge you had to overcome? 
  - what are the advantages of X over Y and vice versa? (For example, for senior frontend devs, you can ask for the differences between React/Angular/Vue, if they have that experience). If you require specific experience in a particular technology, the interviewer will need to have sufficient experience as well, enough to be able to ask deeper questions while being able to filter out BS
  - for this [past project], why did you choose this tech stack instead of [more common stack]? What are the pros and cons?
  - can you describe a time when you had to convince upper management to use a risky technical approach?
  - what was your worst technical mistake/fuck-up? (Follow-up: what did you learn, how did you recover, etc)
  - have you ever had a problematic junior developer working with you? How did you handle it? (Such types of questions are good for technical lead roles)
  - have you ever had to dive into a project with an unfamiliar tech stack without time for learning? How did you cope? What were the challenges? etc.
  - what is your preferred approach for estimation? what if you are under schedule pressure?
  - how do you prefer to onboard a new developer to a large project?
- My goal for such questions would be to look for absence of several attributes I consider important for senior developers:
  - able to communicate technical issues well (useful both when managing upwards and downwards)
  - able to adjust to unfamiliar situations/technologies easily 
  - able to admit to mistakes on his part

### Effectiveness of Technical Interviews

Ultimately, just doing the technical questions or the Q&A can't guarantee the candidate will be good for the role. Evaluating the performance of individual developers is a notoriously hard problem, even when doing annual performance reviews, what more when limited to a one hour interview? For me, the purpose of a technical interview is to act as a negative screening tool - to filter out candidates who are obviously unfit for the position: candidates who can't program, who can't communicate well, who don't have experience in the specific role or tools you need, and so on. The actual evaluation of effectiveness and fit should happen during a short probationary work period with the company.

### How to Prepare for Technical Interviews?

For candidates, how do you prepare for technical interviews?

The most important question is how confident are you in your own programming skills? If you've done any nontrivial amount of programming work, generally you won't have an issue. If you're not confident, better to practice until you are, start with simpler questions and work your way up.

For the Q&A part, in general you just need to be honest. But you also need to be able to communicate well, which is something not many people will be able to do. Good communication skill is an essential skill as a developer though, you may want to look for ways to practice and gain confidence in it. I recommend posting on a blog (like this one) to sharpen your communication skills! (Verbal is harder to practice, you need to find someone willing to listen and give you feedback.)

I would also recommend becoming familiar with the requirements for the position you are interviewing for, understanding which parts of your background are most relevant, and highlighting them during any Q&A. In fact, I would prepare a short pitch describing why you think you are a good fit for the role. Often during Q&A I like to start off with asking the candidate to give a short overview of their background, and very few actually give a good response (a lot don't even have a short response), so being prepared in this manner would be very impressive.

It would also help to ask around about the specific recruitment process for the company you're interviewing for, if you have any contacts, or sometimes there's information on the internet. (Good internet searching is an essential developer skill as well!) Just knowing what to expect can boost your confidence.

I've also given some other advice in a [Q&A last year on reddit](/2019/02/reddit-ph-software-dev-qa/). Good luck!