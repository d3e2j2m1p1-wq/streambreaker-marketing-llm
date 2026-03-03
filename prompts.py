"""
Prompt templates for generating marketing strategies based on prediction results
"""

SYSTEM_PROMPT = """You are an expert music marketing advisor specializing in independent artists. 
Your role is to create actionable, budget-conscious marketing strategies for demo tracks.

You provide:
1. Platform prioritization (Spotify, Instagram, TikTok, YouTube)
2. Specific budget allocation
3. Week-by-week action plans
4. Realistic expectations and key metrics to track

Always consider:
- Artist's current social presence
- Genre-specific tactics
- Budget constraints
- Predicted success probability
"""

STRATEGY_PROMPT_TEMPLATE = """
Generate a detailed marketing strategy for an independent artist with the following profile:

**TRACK PREDICTION:**
- Probability of reaching 1,000 streams in 90 days: {prediction_probability}%
- Confidence level: {confidence_level}

**ARTIST PROFILE:**
- Genre: {genre}
- Current Instagram followers: {instagram_followers}
- Current Spotify monthly listeners: {spotify_listeners}
- Has existing fanbase: {has_fanbase}
- Artist career stage: {career_stage}

**TRACK CHARACTERISTICS:**
- Energy level: {energy}/10
- Danceability: {danceability}/10
- Tempo: {tempo} BPM

**LYRIC ANALYSIS** (from Model 2 - NLP):
- Sentiment: {sentiment} (positive/negative/neutral)
- Lexical Diversity: {lexical_diversity}/1.0 (vocabulary richness)
- Hook Repetition: {hook_repetition}/1.0 (catchiness potential)
- Semantic Coherence: {semantic_coherence}/1.0 (lyrical consistency)
- Contains Profanity: {profanity_detected}

**Marketing Implications from Lyrics:**
- {sentiment_marketing_note}
- {lexical_diversity_note}
- {hook_repetition_note}

**BUDGET:**
- Total marketing budget: ${budget}
- Budget flexibility: {budget_flexibility}

**MARKETING STRATEGY REQUIREMENTS:**

1. **Investment Recommendation**
   - Should the artist invest in marketing this track? (Yes/No/Maybe)
   - Rationale based on prediction probability and budget

2. **Platform Prioritization** (Rank 1-4 with budget allocation)
   - Spotify (playlist pitching, ads)
   - Instagram (Reels, Stories, paid promotion)
   - TikTok (organic content, creator partnerships)
   - YouTube (music video, lyric video, shorts)

3. **4-Week Action Plan**
   Week 1: [Specific actions]
   Week 2: [Specific actions]
   Week 3: [Specific actions]
   Week 4: [Specific actions]

4. **Budget Breakdown**
   - Platform 1: $X (specific tactics)
   - Platform 2: $X (specific tactics)
   - Platform 3: $X (specific tactics)
   - Reserve fund: $X

5. **Key Success Metrics**
   - Week 1 target: X streams, X saves, X playlist adds
   - Week 2 target: [metrics]
   - Week 3 target: [metrics]
   - Week 4 target: [metrics]

6. **Risk Mitigation**
   - What could go wrong?
   - Pivot strategies if underperforming by Week 2

Be specific, actionable, and realistic. Consider the {prediction_probability}% probability when setting expectations.
"""

def create_marketing_prompt(
    prediction_probability: float,
    budget: int,
    genre: str = "Indie Pop",
    instagram_followers: int = 500,
    spotify_listeners: int = 100,
    youtube_subscribers: int = 0,
    has_fanbase: bool = False,
    energy: float = 7.0,
    danceability: float = 6.5,
    tempo: float = 120.0,
    # New parameters from Model 2 (Stephanie's NLP analysis)
    sentiment: str = "positive",
    lexical_diversity: float = 0.5,
    hook_repetition: float = 0.5,
    semantic_coherence: float = 0.5,
    profanity_detected: bool = False,
    career_stage: str = "emerging"
):
    """
    Create a formatted prompt for the LLM
    
    Args:
        prediction_probability: Model 1's prediction (0-100%)
        budget: Marketing budget in USD
        sentiment: Lyric sentiment from Model 2 (positive/negative/neutral)
        lexical_diversity: Vocabulary richness (0-1)
        hook_repetition: Catchiness score (0-1)
        semantic_coherence: Lyrical consistency (0-1)
        Other params: Artist and track characteristics
    
    Returns:
        Formatted prompt string
    """
    
    # Determine confidence level
    if prediction_probability >= 85:
        confidence_level = "Very High"
    elif prediction_probability >= 70:
        confidence_level = "High"
    elif prediction_probability >= 50:
        confidence_level = "Moderate"
    else:
        confidence_level = "Low"
    
    # Determine budget flexibility
    if budget >= 3000:
        budget_flexibility = "High - can test multiple channels"
    elif budget >= 1000:
        budget_flexibility = "Moderate - focus on 2-3 channels"
    else:
        budget_flexibility = "Low - must prioritize single best channel"
    
    # Generate marketing insights from NLP features
    if sentiment == "positive":
        sentiment_marketing_note = "Positive sentiment → Good for mainstream playlists, wider appeal"
    elif sentiment == "negative":
        sentiment_marketing_note = "Negative/dark sentiment → Target alternative/emo playlists, niche audiences"
    else:
        sentiment_marketing_note = "Neutral sentiment → Versatile, can target multiple playlist types"
    
    if lexical_diversity >= 0.7:
        lexical_diversity_note = "High lyrical complexity → Appeal to lyrics-focused blogs, Genius annotations"
    elif lexical_diversity >= 0.4:
        lexical_diversity_note = "Moderate lyrical complexity → Balance between accessibility and depth"
    else:
        lexical_diversity_note = "Simple, repetitive lyrics → Good for TikTok, catchy radio potential"
    
    if hook_repetition >= 0.7:
        hook_repetition_note = "Strong hook repetition → HIGH TikTok/viral potential, prioritize short-form video"
    elif hook_repetition >= 0.4:
        hook_repetition_note = "Moderate hook strength → Standard playlist approach"
    else:
        hook_repetition_note = "Weak hook → Focus on production quality, mood-based playlists"
    
    return STRATEGY_PROMPT_TEMPLATE.format(
        prediction_probability=prediction_probability,
        confidence_level=confidence_level,
        genre=genre,
        instagram_followers=instagram_followers,
        spotify_listeners=spotify_listeners,
        has_fanbase="Yes" if has_fanbase else "No",
        career_stage=career_stage,
        energy=energy,
        danceability=danceability,
        tempo=tempo,
        sentiment=sentiment,
        lexical_diversity=lexical_diversity,
        hook_repetition=hook_repetition,
        semantic_coherence=semantic_coherence,
        profanity_detected="Yes" if profanity_detected else "No",
        sentiment_marketing_note=sentiment_marketing_note,
        lexical_diversity_note=lexical_diversity_note,
        hook_repetition_note=hook_repetition_note,
        budget=budget,
        budget_flexibility=budget_flexibility
    )
