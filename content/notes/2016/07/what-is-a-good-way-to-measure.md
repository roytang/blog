---
date: 2016-07-13 00:00:00
slug: what-is-a-good-way-to-measure
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/What-is-a-good-way-to-measure-how-good-a-software-engineer-is/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:

> [What is a good way to measure how good a software engineer is?](https://www.quora.com/What-is-a-good-way-to-measure-how-good-a-software-engineer-is/answer/Roy-Tang)


Evaluation of programmer performance is notoriously hard. There are no good, objective, universally accepted standard metrics.

It follows from the fact that there are no good, objective, universally accepted standard metrics for program size. Typically each programmer in a team will not be doing the same task or even the same type of task, so in order to produce fair evaluations you will need some standard metric of program size to normalize any evaluation. For example, you could choose to use code quality (bugs) as a metric for programmer performance, but not every programmer is assigned to do the same complexity of programs and some modules may be more poorly designed than others resulting in more bugs.

Lines of code is nice, until you realize that more lines of code does not necessarily mean a larger program or system, it may just mean your programmers don’t write particularly concise code. Often, different programmers will write the same program with different lines of code equally well. There are other possible metrics, but they all have different flaws and none of them capture the complexities of program size particularly well. Function points for example are meant to determine program size based on functional complexity but does not take into account technical complexity. Agile teams will often used a fuzzy metric called story points formed by team consensus but these are notoriously inaccurate and may change in relative size from sprint to sprint and definitely change in relative size across teams.

What complicates things even more is that even the best, most senior programmers can slip into poor program quality due to schedule pressure, unreasonable clients or requirements, and so on.

What I would suggest (and probably is unavoidable) is instead a more subjective approach, combining multiple heuristics to get as fair an evaluation as possible. I would suggest something like the following combination:</p><ul><li>Have the programmer define his own goals/targets for the evaluation period. At the end of the period, go over the goals with him and discuss how closely he came to meeting them. These may be quantitative targets or qualitative (“I feel like my code has been of reasonably good quality”). You can compare against the other feedback in this list if there’s any disagreement</li><li>Get feedback from a technical perspective from a mentor or senior developer who has worked closely with the programmer. The feedback can answer some simple questions like “Is his technical skill adequate?”, “Can he be assigned more complex functions?”, “Has he been assigned the appropriate amount of work?”, ““Has he created any problems that someone of his skill level should not be expected to do?”, “How has he contributed to the overall team?”, etc.</li><li>Get feedback from other people he has worked with. For people who haven’t worked that closely with him, the feedback will be leaning more towards soft skills rather than technical, i.e. how well he works with other people, how manageable he is, how helpful he is, and so on.</li></ul><p class="ui_qtext_para u-ltr u-text-align--start">All of the above are subjective, but in combination should give you a relatively good picture of how well the programmer is performing relative to his peers. You can combine it with whatever corporate-sanctioned metrics you need as well.