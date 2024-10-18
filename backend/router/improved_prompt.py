import os
from flask import Blueprint, jsonify, request
from utils.text2image import Text2ImageAPI
from dotenv import load_dotenv
from config import Config

load_dotenv()

improved_route = Blueprint("improved_prompt", __name__)

from langchain_ollama import ChatOllama

model_name = Config.MODEL_NAME


llm = ChatOllama(
    model=model_name,
    temperature=0.8,
    num_predict=256,
)
def _get_adpromt(message: str) -> str:
    messages = [
        (
            "system",
            "You are a helpful assistant. Improve the following prompt for generating an image: Enhance this prompt to vividly generate an image:. Only output the improved prompt, nothing else:",
        ),
        ("human", message),
    ]

    chain = llm.invoke(messages)

    return chain.content