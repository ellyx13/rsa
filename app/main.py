from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Literal
from services import generate_key, encrypt, decrypt

app = FastAPI(title="RSA Nhom 7 Backend")

@app.get("/ping")
async def ping(request: Request):
    return {'ping': 'pong'}



class GenerateKeyRequest(BaseModel):
    key_length: Literal[4, 8, 16]

class GenerateKeyResponse(BaseModel):
    public_key: int
    private_key: int
    n: int

@app.post("/generate-key", response_model=GenerateKeyResponse)
async def generate_public_private_key(request: Request, data: GenerateKeyRequest):
    data = data.model_dump()
    n, e, d = generate_key(data['key_length'])
    results = {}
    results['public_key'] = e 
    results['private_key'] = d 
    results['n'] = n 
    return GenerateKeyResponse(**results)



class EncryptMessageRequest(BaseModel):
    public_key: int
    n: int
    message: str

class EncryptMessageResponse(BaseModel):
    message_encrypt: str

@app.post("/encrypt", response_model=EncryptMessageResponse)
async def encrypt_message(request: Request, data: EncryptMessageRequest):
    data = data.model_dump()
    message = encrypt(data['message'], data['public_key'], data['n'])
    results = {}
    results['message_encrypt'] = message 
    return EncryptMessageResponse(**results)


class DecryptMessageRequest(BaseModel):
    private_key: int
    n: int
    message: str

class DecryptMessageResponse(BaseModel):
    message_decrypt: str

@app.post("/decrypt", response_model=DecryptMessageResponse)
async def decrypt_message(request: Request, data: DecryptMessageRequest):
    data = data.model_dump()
    message = decrypt(data['message'], data['private_key'], data['n'])
    results = {}
    results['message_decrypt'] = message 
    return DecryptMessageResponse(**results)
