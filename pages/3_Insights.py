"""
Insights Dashboard - For Latina wellness practitioners
Basic analytics view (will enhance with emotion tagging in Week 2)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.database import (
    get_all_stories, 
    get_story_count, 
    get_support_distribution,
    get_emotion_distribution,
    get_external_sentiment,
    get_external_emotion_distribution,
    get_theme_distribution
)
from utils.nlp_model import get_emotion_label_display
from utils.export_data import (
    export_stories_to_csv,
    export_emotion_distribution_to_csv,
    export_support_distribution_to_csv,
    export_external_sentiment_to_csv,
    generate_summary_report,
    get_filename_with_timestamp
)
from utils.translations import get_text, get_language_toggle, set_language
from utils.ui_helpers import add_custom_css, show_loading
from utils.auth import check_admin_access, logout, get_current_user
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Community Insights - Voces en Calma",
    page_icon="📊",
    layout="wide"
)

# Add custom CSS
add_custom_css()

# Check admin access before showing dashboard
if not check_admin_access():
    st.stop()

# Show welcome message with current user
current_user = get_current_user()
if current_user:
    st.sidebar.success(f"👋 Welcome, {current_user}!")

# Get current language (set globally in Home.py)
lang = get_language_toggle()

# Header
st.title(get_text('dashboard_title', lang))
st.markdown(f"### {get_text('dashboard_subtitle', lang)}")

st.markdown("---")

# Key metrics
col1, col2, col3, col4 = st.columns(4)

story_count = get_story_count()
support_dist = get_support_distribution()
emotion_dist = get_emotion_distribution()
external_sentiments = get_external_sentiment()
external_emotion_dist = get_external_emotion_distribution()

with col1:
    st.metric(
        label=get_text('community_stories', lang),
        value=story_count
    )

with col2:
    st.metric(
        label=get_text('external_sources', lang),
        value=len(external_sentiments)
    )

with col3:
    # Most common emotion
    if emotion_dist:
        top_emotion = max(emotion_dist, key=emotion_dist.get)
        st.metric(
            label=get_text('top_emotion', lang),
            value=emotion_dist[top_emotion],
            delta=get_text(top_emotion, lang)
        )
    else:
        st.metric(label=get_text('top_emotion', lang), value="N/A")

with col4:
    # Calculate stories from last 7 days
    all_stories = get_all_stories()
    recent_stories = [s for s in all_stories 
                     if datetime.fromisoformat(s['timestamp']) > datetime.now() - timedelta(days=7)]
    st.metric(
        label="Stories This Week",
        value=len(recent_stories)
    )

st.markdown("---")

# Emotion Distribution Visualization
st.markdown(f"## {get_text('emotional_landscape', lang)}")
st.markdown(get_text('emotional_landscape_desc', lang))

if emotion_dist:
    # Create emotion dataframe with display names
    emotion_data = []
    for emotion, count in emotion_dist.items():
        emotion_data.append({
            'Emotion': get_emotion_label_display(emotion),
            'Count': count,
            'Percentage': round(count / story_count * 100, 1)
        })
    
    emotion_df = pd.DataFrame(emotion_data).sort_values('Count', ascending=False)
    
    # Horizontal bar chart - much more readable!
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=emotion_df['Emotion'],
        x=emotion_df['Count'],
        orientation='h',
        text=emotion_df.apply(lambda row: f"{row['Count']} {get_text('stories', lang)} ({row['Percentage']}%)", axis=1),
        textposition='auto',
        marker=dict(
            color=emotion_df['Count'],
            colorscale='Sunset',
            showscale=False
        ),
        hovertemplate='<b>%{y}</b><br>' + get_text('count', lang) + ': %{x}<br><extra></extra>'
    ))
    
    fig.update_layout(
        title=get_text('emotion_distribution_title', lang),
        xaxis_title=get_text('num_stories_axis', lang),
        yaxis_title="",
        height=400,
        yaxis={'categoryorder':'total ascending'},
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Summary stats in clean metric cards
    st.markdown("### 📊 Key Emotion Insights")
    
    cols = st.columns(min(len(emotion_df), 4))
    for idx, (_, row) in enumerate(emotion_df.head(4).iterrows()):
        with cols[idx]:
            st.metric(
                label=row['Emotion'],
                value=f"{row['Count']} stories",
                delta=f"{row['Percentage']}% of total"
            )
else:
    st.info("No emotion data yet. Stories need to be submitted first.")

st.markdown("---")

# Comparative Analysis: Internal vs External
st.markdown("## 🌍 Community Voice vs Broader Conversations")
st.markdown("*How do our community emotions compare to broader Latina wellness discussions?*")

if emotion_dist and external_emotion_dist:
    # Prepare data for comparison
    all_emotions = set(list(emotion_dist.keys()) + list(external_emotion_dist.keys()))
    
    comparison_data = []
    for emotion in all_emotions:
        internal_count = emotion_dist.get(emotion, 0)
        external_count = external_emotion_dist.get(emotion, 0)
        
        # Calculate percentages
        internal_pct = (internal_count / story_count * 100) if story_count > 0 else 0
        external_pct = (external_count / len(external_sentiments) * 100) if len(external_sentiments) > 0 else 0
        
        comparison_data.append({
            'Emotion': get_emotion_label_display(emotion),
            'Our Community': internal_pct,
            'Broader Discussions': external_pct
        })
    
    comp_df = pd.DataFrame(comparison_data).sort_values('Our Community', ascending=False)
    
    # Side-by-side grouped bar chart
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name=get_text('our_community', lang),
        x=comp_df['Emotion'],
        y=comp_df['Our Community'],
        marker_color='#D4846E',
        text=comp_df['Our Community'].round(1),
        texttemplate='%{text}%',
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name=get_text('broader_discussions', lang),
        x=comp_df['Emotion'],
        y=comp_df['Broader Discussions'],
        marker_color='#8B9D83',
        text=comp_df['Broader Discussions'].round(1),
        texttemplate='%{text}%',
        textposition='outside'
    ))
    
    fig.update_layout(
        title=get_text('comparison_title', lang),
        xaxis_title="",
        yaxis_title=get_text('percentage_axis', lang),
        barmode='group',
        height=500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Insights box
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {get_text('key_insights', lang)}")
        
        # Find emotions more prevalent in community vs external
        community_higher = comp_df[comp_df['Our Community'] > comp_df['Broader Discussions']].head(3)
        if not community_higher.empty:
            st.write(get_text('more_prominent', lang))
            for _, row in community_higher.iterrows():
                diff = row['Our Community'] - row['Broader Discussions']
                st.write(f"• {row['Emotion']}: +{diff:.1f}% {get_text('higher', lang)}")
    
    with col2:
        st.markdown(f"### {get_text('opportunities', lang)}")
        
        # Find emotions more prevalent externally
        external_higher = comp_df[comp_df['Broader Discussions'] > comp_df['Our Community']].head(3)
        if not external_higher.empty:
            st.write(get_text('gaining_traction', lang))
            for _, row in external_higher.iterrows():
                st.write(f"• {row['Emotion']}: {get_text('consider_offerings', lang)}")
    
elif emotion_dist:
    st.info("📊 External sentiment data available. Community emotions show strong presence of " + 
            f"{get_text(max(emotion_dist, key=emotion_dist.get), lang)}.")
else:
    st.info(get_text('need_stories_comparison', lang))

st.markdown("---")

# Theme Analysis from External Sources
if external_sentiments:
    st.markdown("## 📚 Themes in Broader Latina Wellness Conversations")
    st.markdown("*What topics are being discussed in public Latina wellness spaces?*")
    
    theme_dist = get_theme_distribution()
    
    if theme_dist:
        # Create theme dataframe
        theme_data = []
        for theme, count in theme_dist.items():
            theme_display = theme.replace('_', ' ').title()
            theme_data.append({
                'Theme': theme_display,
                'Count': count,
                'Percentage': round(count / len(external_sentiments) * 100, 1)
            })
        
        theme_df = pd.DataFrame(theme_data).sort_values('Count', ascending=False)
        
        # Donut chart for themes
        fig = go.Figure(data=[go.Pie(
            labels=theme_df['Theme'],
            values=theme_df['Count'],
            hole=0.4,
            marker=dict(colors=px.colors.sequential.Teal),
            textinfo='label+percent',
            textposition='outside'
        )])
        
        fig.update_layout(
            title=get_text('theme_distribution_title', lang),
            height=500,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Theme insights
        st.info(f"""
        {get_text('theme_insights', lang)} 
        **{theme_df.iloc[0]['Theme']}** ({theme_df.iloc[0]['Percentage']}%). 
        {get_text('align_differ', lang)}
        """)

st.markdown("---")

# Trend Analysis - Emotions Over Time
st.markdown(f"## {get_text('trend_analysis', lang)}")
st.markdown(get_text('trend_analysis_desc', lang))

# Get all stories for trend analysis
all_stories_trend = get_all_stories()

if len(all_stories_trend) > 0:
    # Prepare data for trend analysis
    trend_data = []
    for story in all_stories_trend:
        if story['emotion_label']:
            # Parse date and get week number
            story_date = datetime.fromisoformat(story['timestamp'])
            week_start = story_date - timedelta(days=story_date.weekday())
            week_label = week_start.strftime('%Y-%m-%d')
            
            trend_data.append({
                'Week': week_label,
                'Emotion': get_text(story['emotion_label'], lang),
                'Count': 1
            })
    
    if trend_data:
        trend_df = pd.DataFrame(trend_data)
        
        # Group by week and emotion
        weekly_trends = trend_df.groupby(['Week', 'Emotion']).size().reset_index(name='Count')
        
        # Check if we have enough weeks
        unique_weeks = weekly_trends['Week'].nunique()
        
        if unique_weeks >= 2:
            # Multi-select for emotions to track
            available_emotions = sorted(weekly_trends['Emotion'].unique())
            
            selected_emotions = st.multiselect(
                get_text('select_emotions', lang),
                options=available_emotions,
                default=available_emotions[:3] if len(available_emotions) >= 3 else available_emotions
            )
            
            if selected_emotions:
                filtered_trends = weekly_trends[weekly_trends['Emotion'].isin(selected_emotions)]
                
                # Create line chart
                fig = px.line(
                    filtered_trends,
                    x='Week',
                    y='Count',
                    color='Emotion',
                    markers=True,
                    title=get_text('emotion_trends_title', lang)
                )
                
                fig.update_layout(
                    xaxis_title=get_text('week', lang),
                    yaxis_title=get_text('count', lang),
                    height=400,
                    hovermode='x unified'
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Show trend insights
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"### {get_text('key_insights', lang)}")
                    
                    # Calculate trends for each emotion
                    for emotion in selected_emotions:
                        emotion_data = filtered_trends[filtered_trends['Emotion'] == emotion].sort_values('Week')
                        if len(emotion_data) >= 2:
                            first_week = emotion_data.iloc[0]['Count']
                            last_week = emotion_data.iloc[-1]['Count']
                            change = last_week - first_week
                            
                            if change > 0:
                                st.write(f"📈 **{emotion}**: ↑ {change} " + get_text('stories', lang))
                            elif change < 0:
                                st.write(f"📉 **{emotion}**: ↓ {abs(change)} " + get_text('stories', lang))
                            else:
                                st.write(f"➡️ **{emotion}**: Stable")
                
                with col2:
                    st.markdown(f"### {get_text('opportunities', lang)}")
                    
                    # Find emotions with increasing trends
                    increasing = []
                    for emotion in selected_emotions:
                        emotion_data = filtered_trends[filtered_trends['Emotion'] == emotion].sort_values('Week')
                        if len(emotion_data) >= 2:
                            first_week = emotion_data.iloc[0]['Count']
                            last_week = emotion_data.iloc[-1]['Count']
                            if last_week > first_week:
                                increasing.append(emotion)
                    
                    if increasing:
                        if lang == 'es':
                            st.write("**Emociones en aumento:**")
                        else:
                            st.write("**Increasing emotions:**")
                        for emotion in increasing:
                            st.write(f"• {emotion}")
                        if lang == 'es':
                            st.write("Considera expandir ofertas para estas áreas.")
                        else:
                            st.write("Consider expanding offerings for these areas.")
            else:
                st.info(get_text('select_emotions', lang))
        else:
            st.info(get_text('need_data_trends', lang))
    else:
        st.info(get_text('need_data_trends', lang))
else:
    st.info(get_text('need_data_trends', lang))

st.markdown("---")

# Support Distribution Chart
st.markdown("## 🤝 Support Preferences")
st.markdown("*What types of support is the community asking for?*")

if support_dist:
    # Create dataframe for plotting
    support_df = pd.DataFrame(
        list(support_dist.items()), 
        columns=[get_text('support_type', lang), get_text('count', lang)]
    ).sort_values(get_text('count', lang), ascending=False)
    
    # Horizontal bar chart with Plotly
    fig = px.bar(
        support_df, 
        x=get_text('count', lang), 
        y=get_text('support_type', lang),
        orientation='h',
        title=get_text('requested_support_types', lang),
        color=get_text('count', lang),
        color_continuous_scale='Tealgrn'
    )
    fig.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Table view
    with st.expander(get_text('view_breakdown', lang)):
        st.dataframe(support_df, use_container_width=True)
else:
    st.info("No stories submitted yet. Check back once community members start sharing.")

st.markdown("---")

# External Sentiment Samples
if external_sentiments:
    st.markdown("## 🌐 Sample External Conversations")
    st.markdown("*Recent discussions from Latina wellness blogs, forums, and communities*")
    
    # Show latest 5 external sentiments
    for sentiment in external_sentiments[:5]:
        with st.expander(f"💬 {sentiment['source_type'].title()} | Theme: {sentiment['theme'].replace('_', ' ').title()}"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(sentiment['text_snippet'])
            
            with col2:
                st.markdown(get_text('analysis', lang))
                if sentiment['emotion_label']:
                    emotion_display = get_text(sentiment['emotion_label'], lang)
                    st.write(f"😊 {emotion_display}")
                st.write(f"📅 {sentiment['timestamp'][:10]}")
                st.write(f"🔖 {get_text('theme', lang)} {sentiment['theme'].replace('_', ' ').title()}")

st.markdown("---")

# Recent Stories Overview (anonymized view)
st.markdown("## 📝 Recent Community Voices")
st.markdown("*Anonymous story excerpts to understand community needs*")

# Get all stories first
all_stories = get_all_stories()

# Time filter
time_filter = st.radio(
    "Show stories from:",
    ["Last 7 days", "Last 30 days", "All time"],
    horizontal=True
)

if time_filter == "Last 7 days":
    cutoff = datetime.now() - timedelta(days=7)
elif time_filter == "Last 30 days":
    cutoff = datetime.now() - timedelta(days=30)
else:
    cutoff = datetime.min

filtered_stories = [
    s for s in all_stories 
    if datetime.fromisoformat(s['timestamp']) > cutoff
]

st.markdown("---")

# Emotion-Support Cross Analysis (moved here after filtered_stories is defined)
st.markdown("## 🔗 Emotion-Support Matching")
st.markdown("*Which emotions are paired with which support requests?*")

if filtered_stories and len(filtered_stories) >= 3:
    # Create cross-analysis data
    emotion_support_data = []
    
    for story in filtered_stories:
        if story['emotion_label']:
            emotion_display = get_emotion_label_display(story['emotion_label'])
            for support in story['support_choices']:
                emotion_support_data.append({
                    'Emotion': emotion_display,
                    'Support': support
                })
    
    if emotion_support_data:
        es_df = pd.DataFrame(emotion_support_data)
        
        # Create heatmap data
        heatmap_data = es_df.groupby(['Emotion', 'Support']).size().reset_index(name='Count')
        heatmap_pivot = heatmap_data.pivot(index='Emotion', columns='Support', values='Count').fillna(0)
        
        # Create heatmap with text annotations
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_pivot.values,
            x=heatmap_pivot.columns,
            y=heatmap_pivot.index,
            colorscale='Blues',
            text=heatmap_pivot.values,
            texttemplate='%{text:.0f}',
            textfont={"size": 14, "color": "white"},
            hovertemplate='<b>%{y}</b><br>%{x}<br>' + get_text('count', lang) + ': %{z}<extra></extra>',
            colorbar=dict(title=get_text('count', lang))
        ))
        
        fig.update_layout(
            title=get_text('emotion_support_heatmap', lang),
            xaxis_title=get_text('support_type', lang),
            yaxis_title=get_text('emotion', lang),
            height=500,
            xaxis={'side': 'bottom', 'tickangle': -45},
            yaxis={'side': 'left'}
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(get_text('heatmap_help', lang))
    else:
        st.info(get_text('need_emotion_tags', lang))
else:
    st.info(get_text('need_stories_heatmap', lang))

st.markdown("---")

st.markdown("---")

# Display filtered stories
if filtered_stories:
    st.info(f"📊 {len(filtered_stories)} {get_text('total_stories_period', lang)}")
    
    # Initialize pagination in session state
    if 'story_page' not in st.session_state:
        st.session_state.story_page = 0
    
    # Stories per page
    STORIES_PER_PAGE = 5
    total_pages = (len(filtered_stories) - 1) // STORIES_PER_PAGE + 1
    
    # Get current page stories
    start_idx = st.session_state.story_page * STORIES_PER_PAGE
    end_idx = start_idx + STORIES_PER_PAGE
    current_page_stories = filtered_stories[start_idx:end_idx]
    
    # Display stories in expandable cards (cleaner than table for full text)
    for story in current_page_stories:
        # Create a compact header for the expander
        emotion_display = get_emotion_label_display(story['emotion_label']) if story['emotion_label'] else "No emotion"
        preview = story['story_text'][:80] + "..." if len(story['story_text']) > 80 else story['story_text']
        
        with st.expander(f"📝 Story #{story['id']} | {story['timestamp'][:10]} | {emotion_display}"):
            # Two column layout
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(get_text('full_story', lang))
                st.write(story['story_text'])
                
                if story['practitioner_note']:
                    st.markdown(get_text('additional_context', lang))
                    st.info(story['practitioner_note'])
            
            with col2:
                st.markdown(get_text('details', lang))
                st.write(f"📅 {get_text('date', lang)} {story['timestamp'][:10]}")
                st.write(f"🆔 **ID:** #{story['id']}")
                
                if story['emotion_label']:
                    confidence = story['emotion_confidence']
                    st.write(f"😊 {get_text('detected_emotion_label', lang)}")
                    st.write(emotion_display)
                    st.write(f"📊 {get_text('confidence', lang)} {confidence:.0%}")
                
                st.markdown(get_text('support_requested', lang))
                for support in story['support_choices']:
                    st.write(f"• {support}")
    
    st.markdown("---")
    
    # Pagination controls
    col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
    
    with col1:
        if st.button(get_text('first', lang), disabled=(st.session_state.story_page == 0)):
            st.session_state.story_page = 0
            st.rerun()
    
    with col2:
        if st.button(get_text('previous', lang), disabled=(st.session_state.story_page == 0)):
            st.session_state.story_page -= 1
            st.rerun()
    
    with col3:
        st.markdown(f"<div style='text-align: center; padding: 8px;'>{get_text('page', lang)} {st.session_state.story_page + 1} {get_text('of', lang)} {total_pages}</div>", unsafe_allow_html=True)
    
    with col4:
        if st.button(get_text('next', lang), disabled=(st.session_state.story_page >= total_pages - 1)):
            st.session_state.story_page += 1
            st.rerun()
    
    with col5:
        if st.button(get_text('last', lang), disabled=(st.session_state.story_page >= total_pages - 1)):
            st.session_state.story_page = total_pages - 1
            st.rerun()

else:
    st.info(get_text('no_stories_period', lang))

st.markdown("---")

# Patterns & Insights
st.markdown("## 💡 Key Patterns")

if len(filtered_stories) >= 3:
    # Common themes (basic text analysis for now)
    all_text = " ".join([s['story_text'].lower() for s in filtered_stories])
    
    # Common words (simple version)
    stress_words = ['stress', 'overwhelm', 'anxiety', 'tired', 'exhausted', 
                   'pressure', 'family', 'work', 'guilt', 'worry']
    
    found_themes = {}
    for word in stress_words:
        count = all_text.count(word)
        if count > 0:
            found_themes[word] = count
    
    if found_themes:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Common Themes Mentioned")
            sorted_themes = sorted(found_themes.items(), key=lambda x: x[1], reverse=True)
            for theme, count in sorted_themes[:5]:
                st.write(f"• **{theme.title()}**: mentioned {count} times")
        
        with col2:
            st.markdown("### Support Gaps to Consider")
            st.write("🔍 Analyze if high-frequency themes have corresponding support options.")
            st.write("💡 Consider creating offerings that specifically address repeated concerns.")
    else:
        st.info("Not enough data yet to identify clear patterns. Check back as more stories are shared.")
else:
    st.info("Need at least 3 stories to identify patterns. Encourage community to share!")

st.markdown("---")

# Action Items
st.markdown("## 🎯 Suggested Actions")

if story_count > 0:
    suggestions = []
    
    # Check for high-demand supports
    if support_dist:
        top_3 = sorted(support_dist.items(), key=lambda x: x[1], reverse=True)[:3]
        suggestions.append(f"**High Demand**: {top_3[0][0]} is most requested ({top_3[0][1]} times). Consider expanding offerings in this area.")
    
    # Check for low representation
    if support_dist and len(support_dist) < 5:
        suggestions.append("**Low Awareness**: Some support types are rarely selected. Consider educating community about these options.")
    
    # Recent activity
    if len(recent_stories) > 5:
        suggestions.append(f"**Active Community**: {len(recent_stories)} stories this week shows strong engagement. Great time to launch new offerings!")
    
    for suggestion in suggestions:
        st.success(suggestion)
else:
    st.info("Start by promoting the platform to your community. Share the link to encourage story submissions.")

st.markdown("---")

# Export Section - Moved to end
st.markdown(f"## {get_text('export_data', lang)}")
st.markdown(get_text('export_desc', lang))

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Export all stories
    if story_count > 0:
        all_stories_for_export = get_all_stories()
        csv_stories = export_stories_to_csv(all_stories_for_export)
        if csv_stories:
            st.download_button(
                label=get_text('stories_csv', lang),
                data=csv_stories,
                file_name=get_filename_with_timestamp("community_stories", "csv"),
                mime="text/csv",
                use_container_width=True,
                help=f"Download all {story_count} community stories"
            )
    else:
        st.button(get_text('stories_csv', lang), disabled=True, use_container_width=True)

with col2:
    # Export emotion distribution
    if emotion_dist:
        csv_emotions = export_emotion_distribution_to_csv(emotion_dist)
        if csv_emotions:
            st.download_button(
                label=get_text('emotions_csv', lang),
                data=csv_emotions,
                file_name=get_filename_with_timestamp("emotion_distribution", "csv"),
                mime="text/csv",
                use_container_width=True,
                help="Download emotion distribution data"
            )
    else:
        st.button(get_text('emotions_csv', lang), disabled=True, use_container_width=True)

with col3:
    # Export support distribution
    if support_dist:
        csv_support = export_support_distribution_to_csv(support_dist)
        if csv_support:
            st.download_button(
                label=get_text('support_csv', lang),
                data=csv_support,
                file_name=get_filename_with_timestamp("support_distribution", "csv"),
                mime="text/csv",
                use_container_width=True,
                help="Download support preferences data"
            )
    else:
        st.button(get_text('support_csv', lang), disabled=True, use_container_width=True)

with col4:
    # Export external sentiment
    if external_sentiments:
        csv_external = export_external_sentiment_to_csv(external_sentiments)
        if csv_external:
            st.download_button(
                label=get_text('external_csv', lang),
                data=csv_external,
                file_name=get_filename_with_timestamp("external_sentiment", "csv"),
                mime="text/csv",
                use_container_width=True,
                help="Download external sentiment data"
            )
    else:
        st.button(get_text('external_csv', lang), disabled=True, use_container_width=True)

# Generate summary report
if story_count > 0:
    st.markdown(f"### {get_text('comprehensive_report', lang)}")
    
    theme_dist_export = get_theme_distribution()
    report_text = generate_summary_report(
        story_count=story_count,
        emotion_dist=emotion_dist,
        support_dist=support_dist,
        external_count=len(external_sentiments),
        external_emotion_dist=external_emotion_dist,
        theme_dist=theme_dist_export
    )
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.info(get_text('report_desc', lang))
    
    with col2:
        st.download_button(
            label=get_text('download_report', lang),
            data=report_text,
            file_name=get_filename_with_timestamp("voces_insights_report", "txt"),
            mime="text/plain",
            use_container_width=True
        )

st.markdown("---")

# Footer
st.markdown(f"""
    <div style="text-align: center; color: #8B9D83; font-size: 0.9em;">
    {get_text('footer_privacy', lang)}
    </div>
""", unsafe_allow_html=True)

# Logout button
if st.button(get_text('logout', lang)):
    logout()
    st.rerun()