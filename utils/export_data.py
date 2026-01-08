"""
Data Export Module
Provides functionality to export data as CSV and generate reports
"""

import pandas as pd
from datetime import datetime
import io


def export_stories_to_csv(stories):
    """
    Export stories to CSV format
    Returns a bytes buffer that can be downloaded
    """
    if not stories:
        return None
    
    # Create DataFrame
    df_data = []
    for story in stories:
        df_data.append({
            'Story_ID': story['id'],
            'Date': story['timestamp'][:10],
            'Time': story['timestamp'][11:19],
            'Story_Text': story['story_text'],
            'Emotion': story['emotion_label'],
            'Emotion_Confidence': f"{story['emotion_confidence']:.2%}" if story['emotion_confidence'] else 'N/A',
            'Support_Requested': ', '.join(story['support_choices']),
            'Practitioner_Note': story['practitioner_note'] or ''
        })
    
    df = pd.DataFrame(df_data)
    
    # Convert to CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    return csv_buffer.getvalue()


def export_emotion_distribution_to_csv(emotion_dist):
    """
    Export emotion distribution to CSV
    """
    if not emotion_dist:
        return None
    
    df = pd.DataFrame([
        {'Emotion': emotion, 'Count': count}
        for emotion, count in emotion_dist.items()
    ]).sort_values('Count', ascending=False)
    
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    return csv_buffer.getvalue()


def export_support_distribution_to_csv(support_dist):
    """
    Export support distribution to CSV
    """
    if not support_dist:
        return None
    
    df = pd.DataFrame([
        {'Support_Type': support, 'Count': count}
        for support, count in support_dist.items()
    ]).sort_values('Count', ascending=False)
    
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    return csv_buffer.getvalue()


def export_external_sentiment_to_csv(external_sentiments):
    """
    Export external sentiment data to CSV
    """
    if not external_sentiments:
        return None
    
    df_data = []
    for sentiment in external_sentiments:
        df_data.append({
            'ID': sentiment['id'],
            'Date': sentiment['timestamp'][:10],
            'Text_Snippet': sentiment['text_snippet'],
            'Emotion': sentiment['emotion_label'],
            'Theme': sentiment['theme'],
            'Source_Type': sentiment['source_type']
        })
    
    df = pd.DataFrame(df_data)
    
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    return csv_buffer.getvalue()


def generate_summary_report(story_count, emotion_dist, support_dist, 
                           external_count=0, external_emotion_dist=None, theme_dist=None):
    """
    Generate a text-based summary report
    """
    report_lines = []
    
    report_lines.append("=" * 80)
    report_lines.append("VOCES EN CALMA - COMMUNITY INSIGHTS REPORT")
    report_lines.append("=" * 80)
    report_lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Overview
    report_lines.append("=" * 80)
    report_lines.append("OVERVIEW")
    report_lines.append("=" * 80)
    report_lines.append(f"Total Community Stories: {story_count}")
    report_lines.append(f"Total External Sources Analyzed: {external_count}")
    report_lines.append(f"Unique Emotions Detected: {len(emotion_dist)}")
    report_lines.append(f"Support Types Requested: {len(support_dist)}\n")
    
    # Emotion Distribution
    if emotion_dist:
        report_lines.append("=" * 80)
        report_lines.append("COMMUNITY EMOTION DISTRIBUTION")
        report_lines.append("=" * 80)
        sorted_emotions = sorted(emotion_dist.items(), key=lambda x: x[1], reverse=True)
        for emotion, count in sorted_emotions:
            percentage = (count / story_count * 100) if story_count > 0 else 0
            report_lines.append(f"{emotion.ljust(20)}: {count:3d} stories ({percentage:5.1f}%)")
        report_lines.append("")
    
    # Support Distribution
    if support_dist:
        report_lines.append("=" * 80)
        report_lines.append("SUPPORT PREFERENCES")
        report_lines.append("=" * 80)
        sorted_support = sorted(support_dist.items(), key=lambda x: x[1], reverse=True)
        for support, count in sorted_support:
            report_lines.append(f"{support.ljust(35)}: {count:3d} requests")
        report_lines.append("")
    
    # External Sentiment Comparison
    if external_emotion_dist:
        report_lines.append("=" * 80)
        report_lines.append("EXTERNAL SENTIMENT COMPARISON")
        report_lines.append("=" * 80)
        report_lines.append(f"{'Emotion'.ljust(20)} {'Community'.ljust(15)} {'External'.ljust(15)}")
        report_lines.append("-" * 50)
        
        all_emotions = set(list(emotion_dist.keys()) + list(external_emotion_dist.keys()))
        for emotion in sorted(all_emotions):
            community_count = emotion_dist.get(emotion, 0)
            external_count_em = external_emotion_dist.get(emotion, 0)
            community_pct = (community_count / story_count * 100) if story_count > 0 else 0
            external_pct = (external_count_em / external_count * 100) if external_count > 0 else 0
            
            report_lines.append(
                f"{emotion.ljust(20)} {f'{community_pct:.1f}%'.ljust(15)} {f'{external_pct:.1f}%'.ljust(15)}"
            )
        report_lines.append("")
    
    # Theme Distribution
    if theme_dist:
        report_lines.append("=" * 80)
        report_lines.append("EXTERNAL THEMES")
        report_lines.append("=" * 80)
        sorted_themes = sorted(theme_dist.items(), key=lambda x: x[1], reverse=True)
        for theme, count in sorted_themes:
            percentage = (count / external_count * 100) if external_count > 0 else 0
            report_lines.append(f"{theme.ljust(30)}: {count:3d} mentions ({percentage:5.1f}%)")
        report_lines.append("")
    
    # Key Insights
    report_lines.append("=" * 80)
    report_lines.append("KEY INSIGHTS")
    report_lines.append("=" * 80)
    
    if emotion_dist:
        top_emotion = max(emotion_dist, key=emotion_dist.get)
        top_emotion_count = emotion_dist[top_emotion]
        top_emotion_pct = (top_emotion_count / story_count * 100) if story_count > 0 else 0
        report_lines.append(f"• Most Common Emotion: {top_emotion.title()} ({top_emotion_pct:.1f}%)")
    
    if support_dist:
        top_support = max(support_dist, key=support_dist.get)
        top_support_count = support_dist[top_support]
        report_lines.append(f"• Most Requested Support: {top_support} ({top_support_count} requests)")
    
    report_lines.append("")
    report_lines.append("=" * 80)
    report_lines.append("END OF REPORT")
    report_lines.append("=" * 80)
    
    return "\n".join(report_lines)


def get_filename_with_timestamp(base_name, extension):
    """
    Generate filename with timestamp
    Example: community_stories_2024-01-02_153045.csv
    """
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    return f"{base_name}_{timestamp}.{extension}"