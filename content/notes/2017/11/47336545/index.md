---
date: 2017-11-16 18:15:35
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47336545/marklogic-optic-api
tags:
- marklogic
- marklogic-9
- questions
- stackoverflow
- software development
title: Marklogic Optic API
---

I've been testing migrating one of our systems to Marklogic 9 and using the Optics API.

One of our functions involves grouping claims by member_id, member_name and getting the sums and counts, so I did something like this:

    var results = op.fromView('test', 'claims')
      .groupBy(['member_id', 'member_name'], [
             op.count('num_claims', 'claim_no'),
             op.sum('total_amount', 'claim_amount')
             ])
      .orderBy(op.desc('total_amount'))
      .limit(200)
      .result()
      .toArray();

Above works fine. The results are of the form 

    [
      { 
        member_id: 1, 
        member_name: 'Bob', 
        num_claims: 10, 
        total_amount: 500
      }, 
      ...
    ]

However, we also have a field "company", where each claim is filed under a different company. Basically the relevant view columns are claim_no, member_id, member_name, company, claim_amount

I would like to be able to show a column that list the different companies for which the member_id/member_name has filed claims, and how many claims for each company.

i.e. I want my results to be something like:

    [
      { 
        member_id: 1, 
        member_name: 'Bob', 
        num_claims: 10, 
        total_amount: 500,
        companies: [
          {
            company: 'Ajax Co',
            num_claims: 8
          },
          {
            company: 'Side Gig',
            num_claims: 2
          }
        ]
      }, 
      ...
    ]

I tried something like this:

    results = results.map((member, index, array) => {
      var companies = op.fromView('test', 'claims')
        .where(op.eq(op.col('member_id'), member.member_id))
        .groupBy('company', [
          op.count('num_claims', 'claim_no')      
        ])
        .result()
        .toArray();
      member.companies = companies;
      return member;
    });

And the output seems correct, but it also executes quite slowly - almost a minute (total number of claim documents is around 120k)

In our previous ML8 implementation, we were pre-generating summary documents for each member - so retrieval was reasonably fast with the downside that whenever we got a bunch of new data, all of the summary documents had to be re-generated. I was hoping that ML9's optic API would make it easier to do the retrieval/grouping/aggregates on the fly so we wouldn't have to do that.

In theory, I could just add company to the groupBy fields, then merge the rows in the result query as needed. But the problem with that approach is that I can't guarantee I'll get the top 200 by total amount (as was my original query)

So, the question is: Is there a better way of doing this with a reasonable execution time? Or should I just stick to pre-generating the summary documents?