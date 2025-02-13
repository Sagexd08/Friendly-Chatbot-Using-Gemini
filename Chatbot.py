import google.generativeai as genai
from datetime import datetime
import json
import logging
from textblob import TextBlob
import sqlite3
from collections import deque
import re
import random
from typing import Dict, List, Optional
import hashlib

class MemoryManager:
    def __init__(self, max_size=15):
        self.short_term = deque(maxlen=max_size)
        self.user_info = {}
        self.topic_history = []
        
    def add_memory(self, interaction: dict):
        self.short_term.append(interaction)
        
        # Extract simple keywords for topic tracking
        words = interaction['user_input'].lower().split()
        common_topics = ['help', 'question', 'problem', 'thanks', 'how', 'what', 'why']
        topics = [word for word in words if word in common_topics]
        if topics:
            self.topic_history.append({
                'timestamp': interaction['timestamp'],
                'topics': topics,
                'interaction': interaction
            })
    
    def get_context(self, num_messages=5) -> List[dict]:
        return list(self.short_term)[-num_messages:]
    
    def get_relevant_memories(self, query: str) -> List[dict]:
        query_words = set(query.lower().split())
        relevant = []
        
        for memory in self.topic_history:
            memory_words = set(memory['interaction']['user_input'].lower().split())
            if query_words.intersection(memory_words):
                relevant.append(memory)
                
        return relevant[-3:]  # Return last 3 relevant memories

class EmotionDetector:
    def __init__(self):
        self.emotion_patterns = {
            'happy': ['happy', 'glad', 'great', 'good', 'excellent', 'awesome'],
            'sad': ['sad', 'unhappy', 'disappointed', 'upset', 'down'],
            'angry': ['angry', 'mad', 'frustrated', 'annoyed'],
            'curious': ['curious', 'interested', 'wonder', 'how', 'what', 'why'],
            'grateful': ['thanks', 'thank', 'appreciate', 'grateful']
        }
        
    def detect_emotion(self, text: str) -> str:
        text = text.lower()
        for emotion, patterns in self.emotion_patterns.items():
            if any(pattern in text for pattern in patterns):
                return emotion
        return 'neutral'

class PersonalityEngine:
    def __init__(self):
        self.emotion_emojis = {
            'happy': ['😊', '😄', '🌟'],
            'sad': ['😔', '🫂', '💙'],
            'angry': ['😮', '🤔', '💭'],
            'curious': ['🤔', '✨', '💡'],
            'grateful': ['💖', '🙏', '✨'],
            'neutral': ['😊', '✨', '💫']
        }
        
    def get_emoji(self, emotion: str) -> str:
        return random.choice(self.emotion_emojis.get(emotion, ['✨']))
    
    def adapt_response(self, text: str, emotion: str) -> str:
        response = text
        
        # Add emotion-appropriate emoji if not already present
        if not any(emoji in response for emojis in self.emotion_emojis.values() for emoji in emojis):
            response += f" {self.get_emoji(emotion)}"
            
        return response

class EnhancedChatbot:
    def __init__(self, api_key: str):
        self.model = self.setup_gemini(api_key)
        self.chat = None
        self.memory = MemoryManager()
        self.emotion_detector = EmotionDetector()
        self.personality = PersonalityEngine()
        self.logger = self.setup_logger()
        
    def setup_gemini(self, api_key: str):
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-pro')
    
    def setup_logger(self):
        logging.basicConfig(
            filename='chatbot.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger('Chatbot')
    
    def init_chat(self):
        context = """You are a friendly and supportive chatbot who acts as a caring friend. You should:
        - Be warm and empathetic
        - Use casual, conversational language
        - Share relevant examples when appropriate
        - Ask thoughtful follow-up questions
        - Offer encouragement and support
        - Remember details from the conversation
        - Use appropriate emojis occasionally"""
        
        self.chat = self.model.start_chat(history=[])
        self.chat.send_message(context)
    
    def sanitize_input(self, text: str) -> str:
        # Remove any potentially problematic characters
        return re.sub(r'[^\w\s.,!?()-]', '', text)
    
    def get_response(self, user_input: str) -> str:
        try:
            # Initialize chat if needed
            if not self.chat:
                self.init_chat()
            
            # Process input
            sanitized_input = self.sanitize_input(user_input)
            if not sanitized_input.strip():
                return "I didn't catch that. Could you please say it again? 😊"
            
            # Analyze emotion and get context
            emotion = self.emotion_detector.detect_emotion(sanitized_input)
            context = self.memory.get_context()
            relevant_memories = self.memory.get_relevant_memories(sanitized_input)
            
            # Prepare enhanced prompt
            prompt = f"""Context:
            - User's emotion: {emotion}
            - Recent conversation: {json.dumps(context[-2:] if context else [])}
            - Relevant past topics: {json.dumps(relevant_memories)}
            
            User message: {sanitized_input}
            
            Please provide a natural, friendly response that:
            1. Acknowledges the user's emotional state
            2. Maintains conversation flow
            3. Uses relevant context
            4. Keeps a supportive tone"""
            
            # Generate and enhance response
            response = self.chat.send_message(prompt).text
            enhanced_response = self.personality.adapt_response(response, emotion)
            
            # Update memory
            self.memory.add_memory({
                'user_input': sanitized_input,
                'bot_response': enhanced_response,
                'timestamp': datetime.now().isoformat(),
                'emotion': emotion
            })
            
            return enhanced_response
            
        except Exception as e:
            self.logger.error(f"Error generating response: {str(e)}")
            return "I'm having a bit of trouble right now. Could you try again? 🤔"

def main():
    API_KEY = "AIzaSyDpOCz5YzFKAxcjh4CkSqqVLCQkj5F1XXs"
    
    try:
        chatbot = EnhancedChatbot(API_KEY)
        print("👋 Hello! I'm your friendly AI companion! How can I help you today?")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
                print("Chatbot: Take care! Looking forward to our next chat! 👋✨")
                break
                
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")

    except Exception as e:
        print(f"Oops! Something went wrong: {str(e)}")
        print("Please try restarting the chatbot.")

if __name__ == "__main__":
    main()