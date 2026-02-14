"""
CareerForge - Terminal Voice Chat
=================================
Choose between:
  1. System Assistant (Hope - friendly helper)
  2. InterviewAI (Elon Musk -  interviewer)
"""

import os
import signal
from dotenv import load_dotenv

load_dotenv()


def main():
    api_key = os.getenv("ELEVENLABS_API_KEY")
    assistant_agent_id = os.getenv("ELEVENLABS_AGENT_ID")
    interview_agent_id = os.getenv("ELEVENLABS_INTERVIEW_AGENT_ID")

    if not api_key:
        print("❌ ELEVENLABS_API_KEY not found in .env")
        return

    print("\n🎙️  CareerForge Voice Chat")
    print("=" * 40)
    print("  1. 💬 System Assistant (Hope)")
    print("  2. 🎯  Interview")
    print("=" * 40)

    choice = input("\nChoose mode (1 or 2): ").strip()

    if choice == "2":
        agent_id = interview_agent_id
        mode_name = "InterviewAI"
        if not agent_id:
            print("❌ ELEVENLABS_INTERVIEW_AGENT_ID not set in .env")
            return
    else:
        agent_id = assistant_agent_id
        mode_name = "System Assistant (Hope)"
        if not agent_id:
            print("❌ ELEVENLABS_AGENT_ID not set in .env")
            return

    # Import here so startup is fast
    from elevenlabs.client import ElevenLabs
    from elevenlabs.conversational_ai.conversation import Conversation
    from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

    client = ElevenLabs(api_key=api_key)

    print(f"\n🚀 Starting {mode_name}...")
    if choice == "2":
        print("💡 Tip: Tell the interviewer the company and role you're targeting.")
    print("🎤 Speak into your mic. Press Ctrl+C to stop.\n")

    conversation = Conversation(
        client=client,
        agent_id=agent_id,
        requires_auth=False,
        audio_interface=DefaultAudioInterface(),
        callback_agent_response=lambda text: print(f"🤖 Agent: {text}"),
        callback_user_transcript=lambda text: print(f"👤 You: {text}"),
    )

    conversation.start_session()

    # Graceful shutdown on Ctrl+C
    signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())

    print("✅ Connected! Start talking...\n")
    conversation.wait_for_session_end()
    print("\n👋 Session ended. Thanks for using CareerForge!")


if __name__ == "__main__":
    main()
