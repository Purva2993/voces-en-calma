"""
Script to populate the database with realistic test stories
Run this to add sample data for testing the dashboard
"""

from utils.database import save_story, update_story_emotion
from utils.nlp_model import detect_emotion
from datetime import datetime, timedelta
import random

# Sample stories representing real community experiences
SAMPLE_STORIES = [
    {
        "story": "I feel so overwhelmed trying to balance work, taking care of my kids, and helping my aging parents. Everyone needs something from me and I don't know how to say no without feeling guilty.",
        "supports": ["Virtual group circles", "One-on-one coaching", "Journaling prompts"],
        "note": "I need help setting boundaries without feeling like I'm abandoning my family"
    },
    {
        "story": "This week has been exhausting. I'm working two jobs to support my family and I barely have time to sleep. I feel like I'm running on empty but I can't stop.",
        "supports": ["Massage/bodywork", "Quiet self-study resources", "Spiritual/faith-rooted support"],
        "note": "Need something that doesn't require more energy from me"
    },
    {
        "story": "I'm tired of always being the strong one. My family expects me to handle everything - all the emotional labor, all the planning, all the caregiving. Sometimes I just want to fall apart.",
        "supports": ["One-on-one coaching", "Virtual group circles", "Art/creative therapy"],
        "note": "Want to connect with others who understand"
    },
    {
        "story": "I feel guilty for wanting time for myself. When I take a break or do something just for me, I feel selfish. But I'm so burned out that I don't recognize myself anymore.",
        "supports": ["Journaling prompts", "One-on-one coaching", "Movement/somatic practices"],
        "note": "Learning to prioritize myself without the guilt"
    },
    {
        "story": "My anxiety has been really high lately. Between work stress and family expectations, I feel like I'm constantly on edge. I worry about everything and can't seem to relax.",
        "supports": ["Virtual group circles", "Spiritual/faith-rooted support", "Quiet self-study resources"],
        "note": "Looking for calming practices that fit my culture"
    },
    {
        "story": "I'm struggling with the pressure to be the perfect daughter, mother, and wife. The cultural expectations are so heavy and I feel like I'm failing at everything.",
        "supports": ["One-on-one coaching", "Virtual group circles", "Journaling prompts"],
        "note": "Need help navigating cultural expectations"
    },
    {
        "story": "Things are getting a little better. I started setting small boundaries and it's scary but I'm learning to prioritize my own wellbeing. Still have a long way to go though.",
        "supports": ["Virtual group circles", "Journaling prompts", "Movement/somatic practices"],
        "note": "Want to continue this growth"
    },
    {
        "story": "I love my family but sometimes I feel invisible. Everyone takes and takes but no one asks what I need. I'm angry but I don't know how to express it without causing drama.",
        "supports": ["Art/creative therapy", "One-on-one coaching", "Movement/somatic practices"],
        "note": "Need healthy ways to express anger"
    },
    {
        "story": "My body is telling me to slow down but I don't know how. I have headaches, my back hurts, I can't sleep well. I know it's stress but I can't stop the cycle.",
        "supports": ["Massage/bodywork", "Movement/somatic practices", "Spiritual/faith-rooted support"],
        "note": "Physical healing and stress relief"
    },
    {
        "story": "I feel lonely even though I'm surrounded by people. No one really sees me or understands what I'm going through. I smile and pretend everything is fine but inside I'm struggling.",
        "supports": ["Virtual group circles", "One-on-one coaching", "Art/creative therapy"],
        "note": "Need genuine connection and understanding"
    },
    {
        "story": "The weight of intergenerational trauma feels so heavy. I want to break these patterns for my children but I don't know where to start. I see my mother's pain in myself.",
        "supports": ["One-on-one coaching", "Spiritual/faith-rooted support", "Virtual group circles"],
        "note": "Healing ancestral wounds"
    },
    {
        "story": "Work has been incredibly stressful and when I come home there's no rest. I'm expected to cook, clean, and take care of everyone else's emotional needs. When do I get to rest?",
        "supports": ["Virtual group circles", "Journaling prompts", "One-on-one coaching"],
        "note": "Need practical strategies for balance"
    },
    {
        "story": "I'm learning to honor both my heritage and my own path. It's hard when traditions clash with my personal needs, but I'm finding my way slowly.",
        "supports": ["Virtual group circles", "Journaling prompts", "Spiritual/faith-rooted support"],
        "note": "Navigating cultural identity"
    },
    {
        "story": "My kids are struggling and I don't know how to help them while also taking care of myself. I feel pulled in every direction and nothing feels like enough.",
        "supports": ["One-on-one coaching", "Virtual group circles", "Quiet self-study resources"],
        "note": "Parenting support that honors our culture"
    },
    {
        "story": "I'm grateful for the healing journey I'm on. It's not easy but I'm starting to see glimpses of peace. I want to keep growing and learning.",
        "supports": ["Virtual group circles", "Spiritual/faith-rooted support", "Movement/somatic practices"],
        "note": "Continuing my healing path"
    },
    {
        "story": "Financial stress is eating me alive. I'm working so hard but it never feels like enough. The worry keeps me up at night and affects everything else in my life.",
        "supports": ["One-on-one coaching", "Virtual group circles", "Spiritual/faith-rooted support"],
        "note": "Need emotional support around money stress"
    },
    {
        "story": "I lost someone important to me and the grief feels unbearable. My family expects me to be strong but I need to fall apart sometimes. I need space to grieve.",
        "supports": ["One-on-one coaching", "Spiritual/faith-rooted support", "Art/creative therapy"],
        "note": "Grieving in a way that honors our traditions"
    },
    {
        "story": "I'm tired of code-switching and pretending to be someone I'm not at work. The microaggressions and cultural isolation are wearing me down.",
        "supports": ["Virtual group circles", "One-on-one coaching", "Art/creative therapy"],
        "note": "Dealing with workplace cultural stress"
    },
    {
        "story": "My relationship is struggling under all the stress. We love each other but we're both so overwhelmed that we have nothing left to give. We need help.",
        "supports": ["One-on-one coaching", "Virtual group circles", "Movement/somatic practices"],
        "note": "Relationship support"
    },
    {
        "story": "I'm proud of the small steps I'm taking. Today I said no to something that would have drained me. It felt scary and liberating at the same time.",
        "supports": ["Virtual group circles", "Journaling prompts", "Spiritual/faith-rooted support"],
        "note": "Celebrating small wins"
    }
]


def populate_database(num_stories=None):
    """
    Populate database with sample stories
    If num_stories is None, adds all sample stories
    """
    stories_to_add = SAMPLE_STORIES if num_stories is None else SAMPLE_STORIES[:num_stories]
    
    print(f"\n🌱 Populating database with {len(stories_to_add)} stories...\n")
    
    success_count = 0
    
    for i, story_data in enumerate(stories_to_add, 1):
        try:
            # Save story
            story_id = save_story(
                story_text=story_data["story"],
                support_choices=story_data["supports"],
                practitioner_note=story_data["note"]
            )
            
            if story_id:
                # Detect emotion
                emotion, confidence, _ = detect_emotion(story_data["story"])
                
                # Update with emotion
                update_story_emotion(story_id, emotion, confidence)
                
                print(f"✅ Story {i}/{len(stories_to_add)}: {emotion} (confidence: {confidence:.2f})")
                print(f"   Preview: {story_data['story'][:60]}...")
                print()
                
                success_count += 1
            else:
                print(f"❌ Story {i}/{len(stories_to_add)}: Failed to save")
                
        except Exception as e:
            print(f"❌ Story {i}/{len(stories_to_add)}: Error - {e}")
    
    print(f"\n🎉 Successfully added {success_count}/{len(stories_to_add)} stories!")
    print(f"📊 Your dashboard should now have rich data to display.\n")


if __name__ == "__main__":
    import sys
    
    print("=" * 80)
    print("VOCES EN CALMA - Database Population Script")
    print("=" * 80)
    
    # Check if user wants to add specific number of stories
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            print(f"\nAdding {num} stories to the database...")
            populate_database(num)
        except ValueError:
            print("\n❌ Please provide a valid number: python populate_test_data.py 10")
    else:
        print(f"\nAdding all {len(SAMPLE_STORIES)} sample stories to the database...")
        response = input("Continue? (yes/no): ")
        
        if response.lower() in ['yes', 'y']:
            populate_database()
        else:
            print("\n❌ Cancelled. No stories were added.")