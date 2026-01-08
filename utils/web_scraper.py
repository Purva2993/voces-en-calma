"""
Web Scraping Module for External Latina Wellness Content
Collects public content from blogs, forums, and social media
"""

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import re

# Sample public Latina wellness blogs and resources
PUBLIC_SOURCES = {
    'blogs': [
       'https://delasmias.com/blog',  # Empowerment & healthy living
        'https://www.plenilunia.com/feed',  # Women's health (Spanish)
        'https://www.delilife.mx/feed',  # Wellness and lifestyle blog
        'https://wearemitu.com/category/fierce/wellness/feed'  # Mitú's wellness vertical
    ],
    'communities_and_resources': [
        'https://www.weallgrowlatina.com/community',  # Massive network & blog
        'https://pflag.org/events/latino-community-comunidad-latina/', # LGBTQ+ wellness support
        'https://nlbha.org/resources/',  # Behavioral health resources
        'https://www.healthyamericas.org/'  # National Alliance for Hispanic Health
    ]
}

# Keywords to search for
WELLNESS_KEYWORDS = [
    'stress', 'anxiety', 'boundaries', 'caregiving', 'self-care',
    'healing', 'therapy', 'mental health', 'burnout', 'overwhelm',
    'family expectations', 'cultural pressure', 'guilt', 'balance',
    'motherhood', 'work-life balance', 'emotional health'
]


def scrape_blog_content(url, max_articles=10):
    """
    Scrape blog content from a given URL
    Returns list of articles with text and metadata
    """
    articles = []
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Generic blog post extraction (adjust selectors based on actual sites)
        posts = soup.find_all(['article', 'div'], class_=re.compile('post|article|entry'), limit=max_articles)
        
        for post in posts:
            # Extract title
            title_elem = post.find(['h1', 'h2', 'h3'], class_=re.compile('title|heading'))
            title = title_elem.get_text(strip=True) if title_elem else "No title"
            
            # Extract content
            content_elem = post.find(['div', 'p'], class_=re.compile('content|body|text|excerpt'))
            content = content_elem.get_text(strip=True) if content_elem else ""
            
            # Only include if content is substantial and relevant
            if len(content) > 100 and any(keyword in content.lower() for keyword in WELLNESS_KEYWORDS):
                articles.append({
                    'title': title,
                    'content': content,
                    'source': url,
                    'source_type': 'blog',
                    'timestamp': datetime.now().isoformat()
                })
        
        print(f"✅ Scraped {len(articles)} articles from {url}")
        
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
    
    return articles


def scrape_reddit_wellness(subreddit='LatinoPeopleTwitter', limit=20):
    """
    Scrape Reddit posts (using public JSON API, no auth needed for public posts)
    """
    posts = []
    
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
        headers = {'User-Agent': 'WellnessResearchBot/1.0'}
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        for post_data in data['data']['children']:
            post = post_data['data']
            
            # Combine title and selftext
            text = f"{post.get('title', '')} {post.get('selftext', '')}"
            
            # Filter for wellness-related content
            if any(keyword in text.lower() for keyword in WELLNESS_KEYWORDS) and len(text) > 50:
                posts.append({
                    'title': post.get('title', ''),
                    'content': text,
                    'source': f"reddit.com/r/{subreddit}",
                    'source_type': 'reddit',
                    'timestamp': datetime.fromtimestamp(post.get('created_utc', 0)).isoformat()
                })
        
        print(f"✅ Scraped {len(posts)} posts from r/{subreddit}")
        
    except Exception as e:
        print(f"❌ Error scraping Reddit: {e}")
    
    return posts


def generate_synthetic_content():
    """
    Generate synthetic external content for testing/demo purposes
    This simulates what would be scraped from real sources
    """
    synthetic_posts = [
        {
            'title': 'Setting Boundaries with Familia',
            'content': 'Learning to set boundaries with my family has been one of the hardest but most necessary things. The guilt is real but so is my need for peace.',
            'source': 'latina-wellness-blog.com',
            'source_type': 'blog',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Burnout is Real in Our Community',
            'content': 'We are taught to be strong, to carry everyone, to never complain. But burnout is affecting so many of us. We need to talk about rest as resistance.',
            'source': 'community-forum.com',
            'source_type': 'forum',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Therapy and Curanderismo Can Coexist',
            'content': 'I go to therapy AND I practice the healing traditions my abuela taught me. Both are valid. Both are powerful. We don\'t have to choose.',
            'source': 'wellness-magazine.com',
            'source_type': 'blog',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'The Weight of Being the Strong One',
            'content': 'Always being the strong one in the family is exhausting. Who holds space for us when we need to fall apart? We deserve support too.',
            'source': 'reddit.com/r/LatinxMentalHealth',
            'source_type': 'reddit',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Cultural Expectations and Mental Health',
            'content': 'The pressure to be the perfect daughter, mother, wife is suffocating. Our mental health matters just as much as fulfilling cultural expectations.',
            'source': 'latina-voices-blog.com',
            'source_type': 'blog',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Finding Joy in Small Moments',
            'content': 'Despite all the stress, I\'m learning to find joy in small moments. A good cafecito, music, dancing in my kitchen. These moments matter.',
            'source': 'wellness-community.com',
            'source_type': 'forum',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Intergenerational Trauma is Heavy',
            'content': 'Healing from intergenerational trauma while still living with the source of it is incredibly difficult. But we\'re breaking cycles.',
            'source': 'healing-blog.com',
            'source_type': 'blog',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Self-Care Isn\'t Selfish',
            'content': 'I used to feel guilty for taking time for myself. Now I understand that self-care isn\'t selfish - it\'s necessary for survival.',
            'source': 'latina-wellness-collective.com',
            'source_type': 'blog',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Work Stress and Home Expectations',
            'content': 'Between work stress and home expectations, I feel like I\'m drowning. Where is the space for me? When do I get to just breathe?',
            'source': 'community-support-forum.com',
            'source_type': 'forum',
            'timestamp': datetime.now().isoformat()
        },
        {
            'title': 'Embracing Both Cultures',
            'content': 'I\'m learning to embrace both my heritage and my individual needs. It\'s not about rejecting tradition, it\'s about honoring myself too.',
            'source': 'bicultural-wellness.com',
            'source_type': 'blog',
            'timestamp': datetime.now().isoformat()
        }
    ]
    
    return synthetic_posts


def classify_theme(text):
    """
    Classify the main theme of the text
    """
    theme_keywords = {
        'boundaries': ['boundary', 'boundaries', 'saying no', 'limits'],
        'caregiving': ['caretaker', 'caregiving', 'taking care', 'caring for'],
        'family_expectations': ['family expectation', 'cultural expectation', 'tradition', 'familia'],
        'work_stress': ['work stress', 'job', 'workplace', 'career', 'burnout'],
        'self_care': ['self-care', 'self care', 'me time', 'rest'],
        'guilt': ['guilt', 'guilty', 'shame', 'ashamed'],
        'healing': ['healing', 'therapy', 'counseling', 'growth'],
        'joy': ['joy', 'happy', 'grateful', 'peace', 'hope'],
        'cultural_identity': ['cultural', 'identity', 'heritage', 'roots', 'tradition']
    }
    
    text_lower = text.lower()
    
    # Count matches for each theme
    theme_scores = {}
    for theme, keywords in theme_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            theme_scores[theme] = score
    
    # Return primary theme or 'general'
    if theme_scores:
        return max(theme_scores, key=theme_scores.get)
    else:
        return 'general_wellness'


def collect_external_content(use_synthetic=True):
    """
    Main function to collect external content
    Set use_synthetic=True for demo/testing without real scraping
    """
    all_content = []
    
    if use_synthetic:
        print("🌱 Using synthetic content for demo...")
        all_content = generate_synthetic_content()
    else:
        print("🌐 Collecting content from public sources...")
        
        # Scrape Reddit (public API)
        reddit_posts = scrape_reddit_wellness('LatinoPeopleTwitter', limit=10)
        all_content.extend(reddit_posts)
        
        time.sleep(2)  # Rate limiting
        
        # Add more sources here as needed
        # blog_posts = scrape_blog_content('https://actual-blog-url.com')
        # all_content.extend(blog_posts)
    
    # Classify themes for all content
    for item in all_content:
        item['theme'] = classify_theme(item['content'])
    
    print(f"\n✅ Collected {len(all_content)} pieces of external content")
    return all_content


# Test function
if __name__ == "__main__":
    print("=" * 80)
    print("EXTERNAL CONTENT SCRAPER - TEST")
    print("=" * 80)
    
    content = collect_external_content(use_synthetic=True)
    
    print("\n📊 Sample Results:")
    for i, item in enumerate(content[:3], 1):
        print(f"\n{i}. {item['title']}")
        print(f"   Theme: {item['theme']}")
        print(f"   Source: {item['source_type']}")
        print(f"   Preview: {item['content'][:100]}...")