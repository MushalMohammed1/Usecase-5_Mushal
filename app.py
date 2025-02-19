import streamlit as st

# Custom CSS styling for a more polished look
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        h2 {
            color: #2e8b57;
            font-size: 36px;
            text-align: right;
            animation: fadeIn 1.5s ease-in-out;
        }
        h3 {
            color: #5f6368;
            font-size: 22px;
            text-align: right;
            line-height: 1.6;
            animation: fadeIn 1.5s ease-in-out;
        }
        .stButton>button {
            background-color: #32cd32;
            color: white;
            padding: 15px;
            font-size: 20px;
            border-radius: 10px;
            border: none;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #228b22;
            transform: translateY(-2px);
        }
        .stMarkdown {
            font-size: 18px;
            margin: 20px 0;
            text-align: right;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title
st.markdown('<h2>تحليل بيانات سوق العمل في السعودية 🚀📊</h2>', unsafe_allow_html=True)

# Introduction
st.markdown('''<h3>في هذا التحليل، سنأخذكم في جولة داخل بيانات سوق العمل السعودي ونكشف لكم عن أبرز الاتجاهات في الرواتب وتوزيع الوظائف عبر مناطق المملكة. كما سنتعرف على فرص العمل المتاحة للخرجين الجدد وتوزيعها حسب الخبرة والمناطق الجغرافية.</h3>''', unsafe_allow_html=True)

# Highlighting Key Insights
st.markdown('''<h3>أحد الأمور المهمة التي وجدناها هي العلاقة بين الخبرة والراتب. من خلال تحليل بيانات الرواتب، اكتشفنا أن الخبرة تلعب دورًا رئيسيًا في تحديد الرواتب في المملكة.</h3>''', unsafe_allow_html=True)

# Job Title and Salary Insights
st.markdown('''<h3>كما أن هناك العديد من الوظائف التي توفر رواتب جيدة جدًا لمن يمتلك الخبرة المناسبة. من الجدير بالذكر أن بعض الرواتب تتجاوز 15000 ريال، وهي تمثل الوظائف التي تتطلب مهارات وخبرات استثنائية.</h3>''', unsafe_allow_html=True)

# Animation Section for Visualization
st.markdown('''<h3>دعونا ننتقل الآن إلى التحليل البياني لنرى توزيع الرواتب ونحدد الفروقات بين الرواتب للخرجين الجدد مقابل ذوي الخبرة.</h3>''', unsafe_allow_html=True)

# Display Data Plot with an Animation
st.markdown('''<h3>إليك توزيع الرواتب للخرجين الجدد 🧐</h3>''', unsafe_allow_html=True)

# Add a Button to Trigger the Visualization (Optional)
if st.button('عرض التوزيع'):
    st.markdown('''<h3>انقر على الزر لعرض التحليل البياني التفاعلي!</h3>''', unsafe_allow_html=True)
    # Assuming visualization plot (such as `sns.histplot` or other charts) will be shown below

# Animated Section for Outliers Detection
st.markdown('''<h3>بعد تحليل البيانات، قمنا بتحديد بعض الرواتب التي تعتبر شاذة بسبب قيمها العالية جدًا، وتجاوزت حاجز الـ 15000 ريال. هذه الوظائف تتطلب عادة مهارات نادرة أو خبرات طويلة في مجالات متخصصة مثل الإدارة العليا أو المشاريع الاستراتيجية.</h3>''', unsafe_allow_html=True)

# Outlier Example
st.markdown('''<h3>الرواتب الشاذة التي تم تحديدها كانت في بعض الوظائف مثل المديري التنفيذي لمشاريع كبيرة وغيرها من الأدوار القيادية.</h3>''', unsafe_allow_html=True)

# Display the next section in Data Analysis
st.markdown('''<h3>بعد ذلك، قمنا بتحليل توزيع الوظائف عبر مناطق السعودية المختلفة. وبالطبع، وجدنا أن أكبر عدد من الوظائف كان في الرياض وجدة.</h3>''', unsafe_allow_html=True)

# Highlight the Geographic Distribution
st.markdown('''<h3>مناطق مثل الدمام وبريدة كانت أيضًا تحتوي على عدد لائق من الفرص الوظيفية، مما يجعلها وجهات جاذبة للباحثين عن العمل.</h3>''', unsafe_allow_html=True)

# Transitioning Thought Process
st.markdown('''<h3>أهم ما يمكن استخلاصه هو أن الفرص في السعودية تستمر في النمو خصوصًا في قطاعات مثل التقنية والهندسة، حيث نرى أن رواتب هذه الوظائف أكثر تنافسية.</h3>''', unsafe_allow_html=True)

# Final Conclusion
st.markdown('''<h3>لذلك، إذا كنت خريجًا جديدًا، يمكنك التوجه نحو المجالات التقنية والهندسية للحصول على فرص أفضل وأكثر ربحية. لكن لا تنسى أن الخبرة تظل عاملًا مهمًا في تعزيز فرصك.</h3>''', unsafe_allow_html=True)

# Final CTA
st.markdown('''<h3>استعملنا مهارات التحليل البياني والبيانات للوصول إلى هذه الاستنتاجات، ونتمنى أن يكون هذا التحليل مفيدًا لكم في اتخاذ القرارات المهنية المستقبلية.</h3>''', unsafe_allow_html=True)
