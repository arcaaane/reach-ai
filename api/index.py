<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .chat-container {
            width: 400px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        .chat-box {
            height: 300px;
            overflow-y: auto;
            padding: 10px;
            border-bottom: 1px solid #ccc;
        }
        .input-box {
            display: flex;
            padding: 10px;
        }
        .input-box input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .input-box button {
            margin-left: 10px;
            padding: 10px;
            border: none;
            background: #007bff;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-box" id="chat-box"></div>
        <div class="input-box">
            <input type="text" id="user-input" placeholder="Type a message...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        async function sendMessage() {
            const inputField = document.getElementById("user-input");
            const chatBox = document.getElementById("chat-box");
            const message = inputField.value.trim();
            if (!message) return;
            
            chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
            inputField.value = "";
            chatBox.scrollTop = chatBox.scrollHeight;

            let retries = 3;  // Number of retries
            let success = false;

            while (retries > 0 && !success) {
                try {
                    const response = await fetch(`https://flask-reach.vercel.app/chat?message=${encodeURIComponent(message)}`);
                    if (!response.ok) throw new Error("Response not OK");
                    const data = await response.json();
                    chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                    success = true;
                } catch (error) {
                    retries--;
                    if (retries > 0) {
                        chatBox.innerHTML += `<div><strong>Bot:</strong> Reach is taking longer than expected (${3 - retries})</div>`;
                        chatBox.scrollTop = chatBox.scrollHeight;
                    } else {
                        chatBox.innerHTML += `<div><strong>Bot:</strong> Error fetching response after multiple attempts.</div>`;
                        chatBox.scrollTop = chatBox.scrollHeight;
                    }
                }
            }
        }
    </script>
</body>
</html>
