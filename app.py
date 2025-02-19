import streamlit as st

# Display the main title
st.markdown('<h2 style="text-align: right; direction: rtl;">📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h2>', unsafe_allow_html=True)

# Introduction
st.markdown('''<h3 style="text-align: right; direction: rtl;">قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية، 
            وهدفنا هو تقديم نظرة شاملة على الوضع الوظيفي في المملكة من خلال تحليلات تتعلق بالرواتب، توزيع الوظائف حسب المناطق، 
            توزيع الوظائف حسب الخبرات المطلوبة، بالإضافة إلى توزيع عقود العمل.</h3>''', unsafe_allow_html=True)

# Proportion of Job Postings by Region
st.markdown('''<h3 style="text-align: right; direction: rtl;">🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style="text-align: right; direction: rtl;">من خلال تحليل بيانات الوظائف، نلاحظ أن معظم الإعلانات الوظيفية تأتي من منطقة الرياض،
            تليها مكة المكرمة والمنطقة الشرقية. بينما تكون المناطق الأخرى مثل عسير وتبوك وغيرها تساهم بنسب أقل بكثير في الإعلانات.</h4>''', unsafe_allow_html=True)
st.image("images/1.png", caption="Proportion of Job Postings by Region in Saudi Arabia")

# Gender Preference in Job Postings
st.markdown('''<h3 style="text-align: right; direction: rtl;">👨‍💻 توزيع الإعلانات الوظيفية حسب الجنس</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style="text-align: right; direction: rtl;">هناك تفضيل واضح في بعض الإعلانات الوظيفية لاستقطاب جميع الأجناس (كلا الجنسين)، 
            بينما هناك بعض الوظائف المخصصة فقط للذكور أو الإناث. لكن بشكل عام، تهيمن الإعلانات التي تقبل كلا الجنسين.</h4>''', unsafe_allow_html=True)
st.image("images/2png", caption="Gender Preference in Job Postings")

# Salary Distribution for Fresh Graduates
st.markdown('''<h3 style="text-align: right; direction: rtl;">💼 توزيع الرواتب للخريجين الجدد</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style="text-align: right; direction: rtl;">توزيع الرواتب يظهر أن الغالبية العظمى من الخريجين الجدد يتقاضون رواتب تتراوح بين 5000 و 10000 ريال، 
            مع بعض الحالات التي تتجاوز هذا المدى. لكن تظل الرواتب بشكل عام منخفضة مقارنة ببقية الخبرات.</h4>''', unsafe_allow_html=True)
st.image("images/3.png", caption="Salary Distribution for Fresh Graduates")

# Proportion of Job Postings for Fresh Graduates vs Experienced Candidates
st.markdown('''<h3 style="text-align: right; direction: rtl;">👩‍🎓 الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style="text-align: right; direction: rtl;">الوظائف الموجهة للخريجين الجدد هي الأكثر انتشارًا، حيث تشكل أكثر من نصف الإعلانات الوظيفية،
            مقارنة بالإعلانات التي تطلب خبرات متعددة التي تشكل نسبة أقل بكثير.</h4>''', unsafe_allow_html=True)
st.image("images/4.png", caption="Proportion of Job Postings for Fresh Graduates vs Experienced Candidates")

# Contract Type Distribution
st.markdown('''<h3 style="text-align: right; direction: rtl;">📝 توزيع نوع العقد في الإعلانات الوظيفية</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style="text-align: right; direction: rtl;">فيما يتعلق بنوع العقد، نجد أن غالبية الوظائف المعروضة هي بعقود دوام كامل، 
            بينما هناك عدد قليل من الوظائف التي تقدم عقودًا للعمل عن بعد.</h4>''', unsafe_allow_html=True)
st.image("images/5.png", caption="Contract Type Distribution in Job Postings")

# Conclusion
st.markdown('''<h3 style="text-align: right; direction: rtl;">💬 الخاتمة</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style="text-align: right; direction: rtl;">باستخدام هذا التحليل، يمكننا ملاحظة توجهات مهمة مثل التوزيع غير المتكافئ للإعلانات 
            الوظيفية بين المناطق في المملكة، بالإضافة إلى الرواتب التي تهيمن عليها الرواتب الأقل للخريجين الجدد.
            كما أن تحليل الخبرات المطلوبة يبرز التحديات التي يواجهها الباحثون عن وظائف ذوي الخبرة. هذه الرؤية توفر لنا معطيات تساعدنا 
            في اتخاذ قرارات أكثر استراتيجية حول مستقبلنا المهني أو نوع الوظائف التي نرغب في التقديم لها.</h4>''', unsafe_allow_html=True)

