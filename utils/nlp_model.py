"""
NLP Emotion Detection Module
Analyzes stories and tags them with emotional themes
"""

#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from vaderSentiment import SentimentIntensityAnalyzer
import re

# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

# Emotion keyword dictionaries (culturally relevant for Latina community)
EMOTION_KEYWORDS = {
    'anxiety': [
        'anxious', 'anxiety', 'worried', 'worry', 'nervous', 'panic', 
        'overwhelm', 'overwhelmed', 'scared', 'fear', 'afraid', 'stress',
        'tense', 'restless', 'on edge'
    ],
    'sadness': [
        'sad', 'sadness', 'depressed', 'depression', 'down', 'low',
        'unhappy', 'miserable', 'crying', 'tears', 'hopeless', 'empty',
        'lonely', 'alone', 'isolated', 'grief', 'loss'
    ],
    'exhaustion': [
        'exhausted', 'tired', 'fatigue', 'drained', 'worn out', 'burnout',
        'burned out', 'depleted', 'weary', 'sleep', 'sleepless', 'overworked',
        'no energy', 'cant keep up', "can't keep up"
    ],
    'guilt': [
        'guilt', 'guilty', 'shame', 'ashamed', 'should', 'shouldnt', 
        'bad mother', 'bad daughter', 'not enough', 'failing', 'selfish',
        'let down', 'disappointed'
    ],
    'anger': [
        'angry', 'anger', 'mad', 'furious', 'frustrated', 'frustration',
        'irritated', 'annoyed', 'resentful', 'resentment', 'bitter',
        'unfair', 'fed up'
    ],
    'hope': [
        'hope', 'hopeful', 'better', 'improve', 'healing', 'growth',
        'trying', 'working on', 'learning', 'grateful', 'thankful',
        'peace', 'calm', 'relief'
    ],
    'overwhelm': [
        'overwhelm', 'overwhelmed', 'too much', 'cant handle', "can't handle",
        'drowning', 'suffocating', 'pressure', 'burden', 'heavy',
        'juggling', 'everything', 'all at once'
    ],
    'family_stress': [
        'family', 'mother', 'daughter', 'sister', 'abuela', 'mama',
        'expectations', 'tradition', 'cultural', 'obligations',
        'take care', 'caretaker', 'caregiving', 'responsible for everyone'
    ]
}


def detect_emotion(text):
    """
    Detect primary and secondary emotions in text
    Returns: (primary_emotion, confidence, all_emotions_dict)
    """
    text_lower = text.lower()
    
    # Get VADER sentiment scores
    vader_scores = vader_analyzer.polarity_scores(text)
    
    # Count emotion keywords
    emotion_scores = {}
    for emotion, keywords in EMOTION_KEYWORDS.items():
        count = sum(1 for keyword in keywords if keyword in text_lower)
        if count > 0:
            emotion_scores[emotion] = count
    
    # Determine primary emotion
    if emotion_scores:
        # Get emotion with highest keyword count
        primary_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Calculate confidence based on keyword density
        word_count = len(text_lower.split())
        confidence = min(emotion_scores[primary_emotion] / max(word_count / 20, 1), 1.0)
        
        return primary_emotion, confidence, emotion_scores
    
    # If no specific emotion keywords, use VADER sentiment as fallback
    elif vader_scores['compound'] <= -0.3:
        return 'sadness', abs(vader_scores['compound']), {'sadness': 1}
    elif vader_scores['compound'] >= 0.3:
        return 'hope', vader_scores['compound'], {'hope': 1}
    else:
        return 'neutral', 0.5, {'neutral': 1}


def get_emotion_summary(text):
    """
    Get a detailed emotion analysis summary
    Returns a dictionary with all detected emotions and their context
    """
    primary_emotion, confidence, all_emotions = detect_emotion(text)
    
    # Sort emotions by score
    sorted_emotions = sorted(all_emotions.items(), key=lambda x: x[1], reverse=True)
    
    summary = {
        'primary_emotion': primary_emotion,
        'confidence': round(confidence, 2),
        'all_emotions': dict(sorted_emotions),
        'emotion_count': len(all_emotions),
        'is_mixed': len(all_emotions) > 2,  # Multiple conflicting emotions
        'vader_sentiment': vader_analyzer.polarity_scores(text)
    }
    
    return summary


def get_emotion_label_display(emotion):
    """
    Convert emotion code to human-readable display text
    """
    display_names = {
        'anxiety': '😰 Anxiety/Worry',
        'sadness': '😢 Sadness',
        'exhaustion': '😴 Exhaustion/Burnout',
        'guilt': '😔 Guilt/Shame',
        'anger': '😤 Anger/Frustration',
        'hope': '🌟 Hope/Positivity',
        'overwhelm': '🌊 Overwhelm',
        'family_stress': '👨‍👩‍👧‍👦 Family Stress',
        'neutral': '😌 Neutral'
    }
    return display_names.get(emotion, emotion.title())


def analyze_story_batch(stories):
    """
    Analyze a batch of stories and return emotion statistics
    Useful for dashboard analytics
    """
    emotion_counts = {}
    total_confidence = 0
    
    for story in stories:
        emotion, confidence, _ = detect_emotion(story)
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        total_confidence += confidence
    
    avg_confidence = total_confidence / len(stories) if stories else 0
    
    return {
        'emotion_distribution': emotion_counts,
        'total_stories': len(stories),
        'average_confidence': round(avg_confidence, 2),
        'most_common': max(emotion_counts, key=emotion_counts.get) if emotion_counts else None
    }


def get_support_recommendations(emotion):
    """
    Recommend support types based on detected emotion
    This helps match community needs with practitioner offerings
    """
    recommendations = {
        'anxiety': [
            'Virtual group circles',
            'Meditation & breathwork',
            'One-on-one coaching',
            'Somatic practices'
        ],
        'sadness': [
            'One-on-one coaching',
            'Art/creative therapy',
            'Spiritual/faith-rooted support',
            'Support groups'
        ],
        'exhaustion': [
            'Massage/bodywork',
            'Quiet self-study resources',
            'Rest & restoration workshops',
            'Boundary-setting coaching'
        ],
        'guilt': [
            'One-on-one coaching',
            'Virtual group circles',
            'Cultural healing circles',
            'Journaling prompts'
        ],
        'anger': [
            'One-on-one coaching',
            'Movement/somatic practices',
            'Art/creative therapy',
            'Assertiveness training'
        ],
        'overwhelm': [
            'Stress management workshops',
            'Time management coaching',
            'Boundary-setting support',
            'Self-care planning'
        ],
        'family_stress': [
            'Cultural healing circles',
            'Family dynamics coaching',
            'Boundary-setting workshops',
            'Intergenerational healing'
        ],
        'hope': [
            'Growth & empowerment groups',
            'Skill-building workshops',
            'Community celebrations',
            'Mentorship programs'
        ]
    }
    
    return recommendations.get(emotion, ['One-on-one coaching', 'Virtual group circles'])


# Test function for development
if __name__ == "__main__":
    # Test stories
    test_stories = [
        "I feel so overwhelmed by family expectations. Everyone needs something from me.",
        "I'm exhausted from working two jobs and taking care of my kids alone.",
        "I feel guilty for wanting time for myself instead of always being there for others.",
        "Things are getting better. I'm learning to set boundaries and it feels good."
    ]
    
    print("🧠 Testing Emotion Detection:\n")
    for story in test_stories:
        emotion, confidence, all_emotions = detect_emotion(story)
        print(f"Story: {story[:60]}...")
        print(f"Primary Emotion: {get_emotion_label_display(emotion)}")
        print(f"Confidence: {confidence:.2f}")
        print(f"All Emotions: {all_emotions}")
        print(f"Recommended Support: {get_support_recommendations(emotion)[:2]}")
        print("-" * 80)