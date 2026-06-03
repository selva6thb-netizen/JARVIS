from dotenv import load_dotenv
load_dotenv()
import os

from livekit import agents
from livekit.agents import JobContext, AgentSession, Agent, RoomInputOptions
from livekit.plugins import ai_coustics
from livekit.plugins import deepgram, openai
from prompt import AGENT_INSTRUCTIONS
from tools import search_web, get_weather, send_whatsapp, get_news

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            tools=[search_web, get_weather, send_whatsapp, get_news]
        )

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(
            model="nova-3",
            language="en",
            endpointing_ms=200,
        ),
        llm=openai.LLM(
            model="openai/gpt-oss-20b",
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY"),
        ),
        tts=deepgram.TTS(model="aura-orion-en"),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            video_enabled=False,
            noise_cancellation=ai_coustics.AICousticsPlugin()
        ),
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))