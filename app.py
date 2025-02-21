import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
jadarat_data = pd.read_csv("cleaned_Jadarat_data.csv")

def load_css(theme):
    """Load custom CSS with colors defined by the chosen theme."""
    custom_css = f"""
    <style>
        .stApp {{
            background: {theme['background']};
            text-align: right;
            direction: rtl;
            color: {theme['text_color']};
        }}
        h1, h2, h3 {{
            font-family: {theme['header_font']};
            color: {theme['text_color']};
        }}
        /* Hero Section Styling */
        .hero {{
            background: linear-gradient({theme['hero_overlay']}, {theme['hero_overlay']}), 
                        url('https://unsplash.com/photos/hallway-between-glass-panel-doors-yWwob8kwOCk') center/cover;
            padding: 4rem 2rem;
            border-radius: 30px;
            margin: 2rem 0;
        }}
        /* Price Card Styling */
        .price-card {{
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-right: 5px solid;
            color: {theme['text_color']};
        }}
        .price-card.apartment {{ border-color: {theme['accent1']}; }}
        .price-card.villa {{ border-color: {theme['accent2']}; }}
        .price-card.land {{ border-color: {theme['accent3']}; }}
        /* Comparison Box Styling */
        .comparison-box {{
            background: linear-gradient(135deg, #ffffff 0%, {theme['background']} 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid #e9ecef;
        }}
        /* Recommendation Box Styling */
        .recommendation-box {{
            background: {theme['recommendation_bg']};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
        }}
        /* Example Section Styling */
        .example-section {{
            margin-top: 3rem;
            font-size: 1.8rem;
            line-height: 1.7;
        }}
        .example-section h2 {{
            font-size: 2.4rem;
            margin-bottom: 1rem;
            color: {theme['text_color']};
        }}
        .highlight {{
            font-weight: bold;
            color: {theme['accent1']};
            font-size: 1.9rem;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def hero_section(theme):
    """Display the hero section with background image and title."""
    hero_html = f"""
    <div class="hero">
        <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            📊 تحليل بيانات الوظائف في المملكة العربية السعودية
        </h1>
        <h3 style="color: white;">اكتشف التوجهات الوظيفية في المملكة</h3>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def info_sections():
    """Show information sections explaining the choices and add interactive graphs."""
    st.title('تحليل بيانات الوظائف في المملكة العربية السعودية')

    st.markdown('''<div class="content-container animate-content">
                    <h3>قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية،
                    وهدفنا هو تقديم نظرة شاملة على الوضع الوظيفي في المملكة من خلال تحليلات تتعلق بالرواتب، توزيع الوظائف حسب المناطق،
                    توزيع الوظائف حسب الخبرات المطلوبة، بالإضافة إلى توزيع عقود العمل.</h3>
                </div>''', unsafe_allow_html=True)

    # Proportion of Job Postings by Region
    st.markdown('''<h3 class="animate-content">🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>من خلال تحليل بيانات الوظائف، نلاحظ أن معظم الإعلانات الوظيفية تأتي من منطقة الرياض،
                    تليها مكة المكرمة والمنطقة الشرقية. بينما تكون المناطق الأخرى مثل عسير وتبوك وغيرها تساهم بنسب أقل بكثير في الإعلانات.</h4>
                </div>''', unsafe_allow_html=True)
    region_distribution = jadarat_data['region'].value_counts().reset_index()
    region_distribution.columns = ['region', 'count']
    fig1 = px.bar(region_distribution, x='region', y='count', title='توزيع الإعلانات الوظيفية حسب المناطق')
    st.plotly_chart(fig1, use_container_width=True)

    # Gender Preference in Job Postings
    st.markdown('''<h3 class="animate-content">👨‍💻 توزيع الإعلانات الوظيفية حسب الجنس</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>هناك تفضيل واضح في بعض الإعلانات الوظيفية لاستقطاب جميع الأجناس (كلا الجنسين)،
                    بينما هناك بعض الوظائف المخصصة فقط للذكور أو الإناث. لكن بشكل عام، تهيمن الإعلانات التي تقبل كلا الجنسين.</h4>
                </div>''', unsafe_allow_html=True)
    gender_distribution = jadarat_data['gender'].value_counts().reset_index()
    gender_distribution.columns = ['gender', 'count']
    fig2 = px.pie(gender_distribution, values='count', names='gender', title='توزيع الإعلانات الوظيفية حسب الجنس')
    st.plotly_chart(fig2, use_container_width=True)

    # Average Salary by Job Title
    st.markdown('''<h3 class="animate-content">💼 متوسط الرواتب حسب العناوين الوظيفية</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>نقوم هنا بعرض متوسط الرواتب لكل عنوان وظيفي في المملكة العربية السعودية.</h4>
                </div>''', unsafe_allow_html=True)
    
    avg_salary_by_job = jadarat_data.groupby('job_title')['Salary'].mean().reset_index()
    avg_salary_by_job = avg_salary_by_job.sort_values(by='Salary', ascending=False).head(10)  # Show top 10 job titles
    fig3 = px.bar(avg_salary_by_job, x='job_title', y='Salary', title='متوسط الرواتب حسب العناوين الوظيفية')
    st.plotly_chart(fig3, use_container_width=True)

    # Proportion of Job Postings for Fresh Graduates vs Experienced Candidates
    st.markdown('''<h3 class="animate-content">👩‍🎓 الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>الوظائف الموجهة للخريجين الجدد هي الأكثر انتشارًا، حيث تشكل أكثر من نصف الإعلانات الوظيفية،
                    مقارنة بالإعلانات التي تطلب خبرات متعددة التي تشكل نسبة أقل بكثير.</h4>
                </div>''', unsafe_allow_html=True)
    experience_distribution = jadarat_data['exper'].value_counts().reset_index()
    experience_distribution.columns = ['experience', 'count']
    fig4 = px.bar(experience_distribution, x='experience', y='count', title='الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة')
    st.plotly_chart(fig4, use_container_width=True)

    # Contract Type Distribution
    st.markdown('''<h3 class="animate-content">📝 توزيع نوع العقد في الإعلانات الوظيفية</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>فيما يتعلق بنوع العقد، نجد أن غالبية الوظائف المعروضة هي بعقود دوام كامل،
                    بينما هناك عدد قليل من الوظائف التي تقدم عقودًا للعمل عن بعد.</h4>
                </div>''', unsafe_allow_html=True)
    contract_distribution = jadarat_data['contract'].value_counts().reset_index()
    contract_distribution.columns = ['contract_type', 'count']
    fig5 = px.pie(contract_distribution, values='count', names='contract_type', title='توزيع نوع العقد في الإعلانات الوظيفية')
    st.plotly_chart(fig5, use_container_width=True)

    # Conclusion
    st.markdown('''<h3 class="animate-content">💬 الخاتمة</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>باستخدام هذا التحليل، يمكننا ملاحظة توجهات مهمة مثل التوزيع غير المتكافئ للإعلانات
                    الوظيفية بين المناطق في المملكة، بالإضافة إلى الرواتب التي تهيمن عليها الرواتب الأقل للخريجين الجدد.
                    كما أن تحليل الخبرات المطلوبة يبرز التحديات التي يواجهها الباحثون عن وظائف ذوي الخبرة. هذه الرؤية توفر لنا معطيات تساعدنا
                    في اتخاذ قرارات أكثر استراتيجية حول مستقبلنا المهني أو نوع الوظائف التي نرغب في التقديم لها.</h4>
                </div>''', unsafe_allow_html=True)

    # Footer
    st.markdown('''<div class="footer">تم التحليل بواسطة مشعل الشقحاء | جميع الحقوق محفوظة 2025</div>''', unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide", page_title="تحليل بيانات الوظائف في المملكة العربية السعودية")

    # Pastel theme configuration
    pastel_theme = {
        "background": "#fdf6e3",
        "text_color": "#657b83",
        "accent1": "#b58900",
        "accent2": "#cb4b16",
        "accent3": "#268bd2",
        "hero_overlay": "rgba(38, 139, 210, 0.4)",
        "header_font": "'Tajawal', sans-serif",
        "recommendation_bg": "#657b83",
    }

    theme = pastel_theme

    load_css(theme)
    hero_section(theme)
    info_sections()

if __name__ == "__main__":
    main()
