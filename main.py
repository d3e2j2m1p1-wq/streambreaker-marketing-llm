"""
Marketing Strategy Generator using OpenAI GPT
Miguel Davila - StreamBreaker AI Project
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, create_marketing_prompt

# Load environment variables
load_dotenv()

class MarketingStrategyGenerator:
    """
    Generates marketing strategies using GPT-3.5-turbo or GPT-4
    """
    
    def __init__(self, model="gpt-3.5-turbo", temperature=0.7):
        """
        Initialize the generator
        
        Args:
            model: OpenAI model to use (gpt-3.5-turbo or gpt-4)
            temperature: Creativity level (0.0-1.0)
        """
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature
        
    def generate_strategy(
        self,
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
        # New parameters from Model 2 (Stephanie's NLP)
        sentiment: str = "positive",
        lexical_diversity: float = 0.5,
        hook_repetition: float = 0.5,
        semantic_coherence: float = 0.5,
        profanity_detected: bool = False,
        career_stage: str = "emerging"
    ) -> dict:
        """
        Generate a marketing strategy based on track prediction and artist profile
        
        Returns:
            dict with 'strategy' (text) and 'metadata' (usage stats)
        """
        
        # Create the prompt
        user_prompt = create_marketing_prompt(
            prediction_probability=prediction_probability,
            budget=budget,
            genre=genre,
            instagram_followers=instagram_followers,
            spotify_listeners=spotify_listeners,
            youtube_subscribers=youtube_subscribers,
            has_fanbase=has_fanbase,
            energy=energy,
            danceability=danceability,
            tempo=tempo,
            sentiment=sentiment,
            lexical_diversity=lexical_diversity,
            hook_repetition=hook_repetition,
            semantic_coherence=semantic_coherence,
            profanity_detected=profanity_detected,
            career_stage=career_stage
        )
        
        # Call OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=self.temperature,
                max_tokens=2000
            )
            
            strategy_text = response.choices[0].message.content
            
            return {
                "success": True,
                "strategy": strategy_text,
                "metadata": {
                    "model": self.model,
                    "tokens_used": response.usage.total_tokens,
                    "cost_estimate": self._estimate_cost(response.usage.total_tokens)
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "strategy": None
            }
    
    def _estimate_cost(self, tokens: int) -> float:
        """
        Estimate API cost based on tokens used
        GPT-3.5-turbo: ~$0.002 per 1K tokens
        GPT-4: ~$0.03 per 1K tokens
        """
        if "gpt-4" in self.model:
            return (tokens / 1000) * 0.03
        else:
            return (tokens / 1000) * 0.002
    
    def generate_strategy_json(
        self,
        prediction_probability: float,
        budget: int,
        **kwargs
    ) -> dict:
        """
        Generate marketing strategy with structured JSON output
        For integration with Reddy's web app (Model 4)
        
        Returns:
            dict with structured strategy data for easy UI display
        """
        # Get the full text strategy
        result = self.generate_strategy(
            prediction_probability=prediction_probability,
            budget=budget,
            **kwargs
        )
        
        if not result["success"]:
            return result
        
        # Parse into structured format
        strategy_text = result["strategy"]
        
        # Extract recommendation (simplified parsing)
        recommendation = "maybe"
        if "yes" in strategy_text.lower()[:500] or "invest" in strategy_text.lower()[:500]:
            recommendation = "invest"
        elif "no" in strategy_text.lower()[:500] or "skip" in strategy_text.lower()[:500]:
            recommendation = "skip"
        
        # Determine confidence based on prediction
        if prediction_probability >= 85:
            confidence = "very_high"
        elif prediction_probability >= 70:
            confidence = "high"
        elif prediction_probability >= 50:
            confidence = "moderate"
        else:
            confidence = "low"
        
        # Create structured output for web app
        structured_output = {
            "success": True,
            "recommendation": recommendation,
            "confidence": confidence,
            "prediction_probability": prediction_probability,
            "budget": budget,
            "strategy_text": strategy_text,
            "platforms": self._extract_platforms(strategy_text),
            "budget_allocation": self._estimate_budget_allocation(budget, strategy_text),
            "metadata": result["metadata"]
        }
        
        return structured_output
    
    def _extract_platforms(self, strategy_text: str) -> list:
        """Extract recommended platforms from strategy text"""
        platforms = []
        text_lower = strategy_text.lower()
        
        if "spotify" in text_lower:
            platforms.append("spotify")
        if "instagram" in text_lower or "reels" in text_lower:
            platforms.append("instagram")
        if "tiktok" in text_lower:
            platforms.append("tiktok")
        if "youtube" in text_lower:
            platforms.append("youtube")
        
        return platforms
    
    def _estimate_budget_allocation(self, total_budget: int, strategy_text: str) -> dict:
        """
        Estimate budget split across platforms
        This is a simplified version - in production, the LLM should output structured data
        """
        platforms = self._extract_platforms(strategy_text)
        
        if not platforms:
            return {}
        
        # Simple equal split for now (can be improved with better parsing)
        allocation = {}
        platform_budget = int(total_budget * 0.9 / len(platforms))  # 90% allocated, 10% reserve
        
        for platform in platforms:
            allocation[platform] = platform_budget
        
        allocation["reserve"] = total_budget - sum(allocation.values())
        
        return allocation


def main():
    """
    Example usage - test the generator
    """
    print("🎵 StreamBreaker AI - Marketing Strategy Generator")
    print("=" * 60)
    
    # Initialize generator
    generator = MarketingStrategyGenerator(model="gpt-3.5-turbo")
    
    # Example scenario: High prediction, moderate budget
    print("\n📊 SCENARIO: High-potential indie pop track, $1500 budget\n")
    
    result = generator.generate_strategy(
        prediction_probability=87.5,  # High confidence from Model 1
        budget=1500,
        genre="Indie Pop",
        instagram_followers=1200,
        spotify_listeners=350,
        youtube_subscribers=800,
        has_fanbase=True,
        energy=7.5,
        danceability=7.0,
        tempo=125.0,
        # Model 2 NLP outputs
        sentiment="positive",
        lexical_diversity=0.72,
        hook_repetition=0.85,
        semantic_coherence=0.78,
        profanity_detected=False,
        career_stage="emerging"
    )
    
    if result["success"]:
        print(result["strategy"])
        print("\n" + "=" * 60)
        print(f"✅ Tokens used: {result['metadata']['tokens_used']}")
        print(f"💰 Estimated cost: ${result['metadata']['cost_estimate']:.4f}")
    else:
        print(f"❌ Error: {result['error']}")


if __name__ == "__main__":
    main()
