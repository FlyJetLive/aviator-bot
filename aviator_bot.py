import websocket
import json

# WebSocket URL
WS_URL = "wss://game9.apac.spribegaming.com/BlueBox/websocket"

# Message handler
def on_message(ws, message):
    try:
        data = json.loads(message)
        print("📊 Data Received:", data)
        
        # Crash point extract karne ka example
        if 'crash_point' in data:
            print(f"🔥 Crash Point: {data['crash_point']}")
        
    except json.JSONDecodeError:
        print("🔄 Non-JSON data received:", message)

# Error handler
def on_error(ws, error):
    print(f"❌ Error: {error}")

# WebSocket open handler
def on_open(ws):
    print("✅ Connection Established")
    
    # Example: Subscribe command (optional)
    ws.send(json.dumps({
        "command": "subscribe",
        "channel": "aviator_data"
    }))

# WebSocket close handler
def on_close(ws, close_status_code, close_msg):
    print("🔒 Connection Closed")

# WebSocket connection start
ws = websocket.WebSocketApp(
    WS_URL,
    on_message=on_message,
    on_error=on_error,
    on_open=on_open,
    on_close=on_close
)

ws.run_forever()
