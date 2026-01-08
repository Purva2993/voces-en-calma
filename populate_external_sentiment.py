"""
Script to collect and populate external sentiment data
Run this to add external Latina wellness content for comparative analysis
"""

from utils.web_scraper import collect_external_content
from utils.database import save_external_sentiment
from utils.nlp_model import detect_emotion


def populate_external_sentiment():
    """
    Collect external content and analyze sentiment
    """
    print("=" * 80)
    print("EXTERNAL SENTIMENT COLLECTION")
    print("=" * 80)
    
    # Collect external content (using synthetic for demo)
    print("\n🌐 Collecting external content...")
    external_posts = collect_external_content(use_synthetic=True)
    
    if not external_posts:
        print("❌ No external content collected")
        return
    
    print(f"\n🧠 Analyzing emotions for {len(external_posts)} posts...\n")
    
    success_count = 0
    
    for i, post in enumerate(external_posts, 1):
        try:
            # Analyze emotion
            emotion, confidence, _ = detect_emotion(post['content'])
            
            # Save to database
            sentiment_id = save_external_sentiment(
                text_snippet=post['content'][:500],  # Limit to 500 chars
                emotion_label=emotion,
                theme=post['theme'],
                source_type=post['source_type']
            )
            
            if sentiment_id:
                print(f"✅ Post {i}/{len(external_posts)}: {emotion} | Theme: {post['theme']}")
                print(f"   Source: {post['source_type']} - {post['source']}")
                print(f"   Preview: {post['content'][:60]}...")
                print()
                success_count += 1
            else:
                print(f"❌ Post {i}/{len(external_posts)}: Failed to save")
                
        except Exception as e:
            print(f"❌ Post {i}/{len(external_posts)}: Error - {e}")
    
    print(f"\n🎉 Successfully added {success_count}/{len(external_posts)} external sentiment entries!")
    print(f"📊 Your dashboard can now show comparative analysis.\n")


if __name__ == "__main__":
    import sys
    
    response = input("Collect and analyze external Latina wellness content? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        populate_external_sentiment()
    else:
        print("\n❌ Cancelled. No external content was collected.")