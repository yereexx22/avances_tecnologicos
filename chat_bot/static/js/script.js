document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('chat-form');
  const chatLog = document.getElementById('chat-log');
  const userInput = document.getElementById('user-message');

  // Función para agregar un mensaje al historial
  function appendMessage(text, sender) {
    const messageBubble = document.createElement('div');
    messageBubble.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageBubble.textContent = text;
    chatLog.appendChild(messageBubble);
    chatLog.scrollTop = chatLog.scrollHeight; // Auto-scroll
  }

  // Manejar envío del formulario
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    appendMessage("Tú: " + userMessage, 'user');

    fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: 'user_message=' + encodeURIComponent(userMessage)
    })
    .then(response => response.json())
    .then(data => {
      appendMessage("Bot: " + data.response, 'bot');
      userInput.value = '';
    });
  });
});
