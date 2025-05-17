# Submission Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut is a higher education institution that has been operating since the year 2000. Over the past two decades, the institute has produced many graduates who have gone on to build successful careers, earning the institution a strong reputation in the field of education. Despite this track record, Jaya Jaya Institut continues to face a significant challenge related to student retention.

A considerable number of students fail to complete their studies and drop out before graduation. This high dropout rate not only impacts the students’ future prospects but also reflects negatively on the institution’s performance, reputation, and long-term sustainability. Each dropout represents a potential loss of investment—in terms of both resources and educational efforts—and can affect funding, accreditation, and public perception.

To address this challenge, the academic affairs department is seeking to identify students who are at risk of dropping out as early as possible. By proactively detecting at-risk students, the institution aims to implement targeted support programs, provide academic and personal guidance, and improve student engagement and success rates. A dataset containing various academic, demographic, and socioeconomic features has been prepared to support this analysis.

### Business Problem

The business problems that will be addressed in this project include:

- High student dropout rate, which may indicate academic difficulties, financial challenges, or lack of student engagement.

- Limited understanding of the key factors that contribute to students leaving before completing their education.

- Lack of an early warning system to proactively identify and support at-risk students.

- Potential reputational and financial impact on the institution if dropout rates remain high, affecting accreditation, funding, and enrollment growth.

### Project Scope

The scope of this project includes:

- Analyzing the provided student dataset to identify patterns and key factors associated with dropout behavior.

- Building a predictive model to determine which features most strongly influence the likelihood of a student dropping out.

- Developing an interactive dashboard using Metabase to help academic staff and administrators monitor critical indicators and student risk levels.

- Providing actionable insights and recommendations based on the analysis to support targeted interventions and improve student retention rates.

### Preparation

Data source: [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Environment setup:

```
pip install -r requirements.txt
```

To run the metabase dashboard:
```
docker run -d \
  -v $(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db \
  -p 3000:3000 \
  --name metabase \
  metabase/metabase
```
## Business Dashboard

The business dashboard provides a clear overview of the key factors influencing student dropout at **Jaya Jaya Institut**. It focuses on six important features identified through a Random Forest model: tuition payment status, grade change, age at enrollment, completion ratio change, approval rate change, and scholarship status. The visualizations help the institute understand how these factors relate to student dropout, such as whether students who are behind on tuition or who experience a drop in grades are more likely to leave.

By highlighting trends across different student groups—such as age categories, academic performance, and financial support—the dashboard enables school administrators to identify at-risk students early. This allows them to take proactive steps, like offering extra academic support or financial counseling, to help students stay enrolled and complete their education.

After running the metabase dashboard, you need to login using:  

email: root@mail.com  
password: root123

Then, go to **Jaya Jaya Institution -> Jaya Jaya Institution Dashboard**.

## Runnning The Machine Learning System
The machine learning inference is made through streamlit library, where it can predict if a student is more likely to dropout based on the important features that gotten from the random forest model. The machine learning inference can be accessed through the following [link](https://finalprojectdropoutstudent-cchsum5ntt6djzcpeamappq.streamlit.app/).

to run locally, use

`streamlit run app.py`

## Conclusion

The dashboard reveals several key insights into student dropout trends at Jaya Jaya Institution. Most students fall within the 18–25 age group, which also has the highest number of dropouts, highlighting the need for targeted support for younger students.

Students who are not up-to-date with tuition payments show a significantly higher dropout rate, suggesting financial difficulties play a major role in student retention. Similarly, students with stable or worsening approval and grade changes tend to drop out more frequently, indicating that academic performance is another major contributing factor. Students with no scholarships also show a higher dropout count compared to those receiving financial aid.

Finally, a similar pattern is observed in completion ratio change—students whose academic progress worsens are more likely to drop out. These findings suggest that Jaya Jaya Institution should prioritize academic support, financial assistance, and early intervention strategies to reduce dropout rates.

To better identify the possibility of student dropouts, a machine learning model using Random Forest has been deployed to predict the likelihood of a student dropping out based on key features such as tuition payment status, grade change, age at enrollment, completion ratio change, approval rate change, and scholarship status. This model provides early warnings that enable the institution to proactively identify and support at-risk students before they decide to drop out.


### Action Items

Here are several recommended action items that Jaya Jaya Maju can take to reduce attrition and improve employee retention:

- Provide tutoring, mentoring, or academic counseling for students showing a decline in grades or completion rates. Monitoring grade changes can help identify students who need support early on.

- Since tuition payment status and scholarship holding are significant indicators, consider expanding financial aid options, flexible payment plans, or creating an emergency fund for students facing financial difficulties.

- Use age at enrollment and academic performance metrics to segment students and tailor communication. For example, older students may need flexible learning options or career guidance.

- Build a system that continuously tracks changes in approval and completion rates. Notify academic advisors when a student’s metrics begin to drop below a safe threshold.

- Ensure that scholarship criteria don’t unintentionally add pressure or risk dropout. Consider offering counseling to scholarship recipients to help them manage academic expectations.