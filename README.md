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

Then, go to **Our Analytics -> Jaya Jaya Institution -> Jaya Jaya Institution Dashboard**.

## Runnning The Machine Learning System
The machine learning inference is made through streamlit library, where it can predict if a student is more likely to dropout based on the important features that gotten from the random forest model. The machine learning inference can be accessed through the following [link](https://google.com)


## Conclusion

The HR analytics dashboard of Jaya Jaya Maju provides clear insights into the key factors contributing to the company’s high employee attrition rate. Based on the visualized data, the highest attrition is observed in the Sales and Research & Development departments, particularly among job roles such as Sales Executive, Sales Representative, and Laboratory Technician. This indicates that job stress, workload, or lack of growth opportunities in these roles might be driving higher employee turnover.

Further analysis shows that younger employees (aged 18–25) have the highest attrition rate (34.92%), despite having the least average tenure, suggesting dissatisfaction or lack of engagement among new hires. Moreover, employees living more than 21 km from the office experience the highest attrition (22.19%), implying that commuting distance may also be a contributing factor. Salary hike trends reveal that even with higher salary increases, some salary groups still show significant attrition, suggesting that financial incentives alone may not effectively retain employees. Overall, these insights can help HR target retention strategies more precisely, by improving employee support, onboarding experience, and work-life balance, especially for the identified high-risk segments.

### Rekomendasi Action Items (Optional)

Here are several recommended action items that Jaya Jaya Maju can take to reduce attrition and improve employee retention:

- Improve policies and work environment in departments with high attrition, especially in Sales and R&D, by conducting employee satisfaction surveys and offering better support programs or work flexibility.

- Provide better support and onboarding programs for young and new employees, especially those aged 18–25, to help them adapt and feel more engaged with the company.

- Consider hybrid work options or transportation allowances for employees who live far from the office to reduce the burden of long commutes.